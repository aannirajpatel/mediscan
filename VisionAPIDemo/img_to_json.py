import os, io
from google.cloud import vision
from google.cloud.vision import types
import json
import datetime
import base64

#edit .vscode settings.json possibly for python path in cloud

#rectangle_list = [(x_1,y_1,x_2,y_2, column_label)]
#current assignment is an example sample for vital_signs.png
json_input = 'JSON::{"img":"iVB...U5ErkJggg\u003d\u003d\n","fields":["kk"],"coords":[[206,368,728,685]]}'
img_base64 = json_input['img']
fields = json_input['fields']
coords = json_input['coords']
data = base64.b64decode(img_base64)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'GoogleCloudDemo-fe3700bf4625.json'
client = vision.ImageAnnotatorClient()

def image_to_dict(rect_coords, rect_labels):
    final_dict = {}
    image = vision.types.Image(content=data)
    response = client.document_text_detection(image=image) 
    texts = response.text_annotations
    stringTemp = ''
    charTemp = ''
    for num in range(len(rect_labels)):
        final_dict[rect_labels] = {}
        for page in response.full_text_annotation.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        for symbol in word.symbols:
                            if (symbol.bounding_box.vertices[0].x > rect_coords[num][0]-20 and
                                symbol.bounding_box.vertices[0].y > rect_coords[num][1]-20 and
                                symbol.bounding_box.vertices[2].x < rect_coords[num][2]+20 and
                                symbol.bounding_box.vertices[2].y < rect_coords[num][3]+20):
                                charTemp = symbol.text
                                #confidence checker for '/', edit for clarity later
                                if ((symbol.confidence < .65) and (symbol.text == '1' or symbol.text == '7') and
                                    ((rect_labels[num].lower() == "blood pressure" or rect_labels[num].lower() == "bp") or
                                    (rect_labels[num].lower() == "pain") or
                                    (rect_labels[num].lower() == "date/time" or rect_labels[num].lower() == "date" or rect_labels[num].lower() == "dob"))):
                                    charTemp = '/'
                                stringTemp += charTemp
                                charTemp = ''
                        if stringTemp:
                            #temp confidence checker
                            #if ((rect_labels[num].lower() == "temp") and (float(stringTemp) > 200)):
                                #final_dict[rect_labels[num]].append(stringTemp[0:len(stringTemp) - 1] + '.' + stringTemp[len(stringTemp) - 1])
                            #else:
                                final_dict[rect_labels[num]].append(stringTemp)
                        stringTemp = ''
        #google vision word spacing workaround, works 90% of the time
        newList = []
        if len(final_dict[rect_labels[num]]) > 3:
            count = 0
            myiter = iter(range(len(final_dict[rect_labels[num]]) - 2))
            for i in myiter:
                if (final_dict[rect_labels[num]][i].isdigit() and
                (final_dict[rect_labels[num]][i+1] == '/' or final_dict[rect_labels[num]][i+1] == '.') and
                final_dict[rect_labels[num]][i+2].isdigit()):
                    a = (final_dict[rect_labels[num]][i])
                    b = (final_dict[rect_labels[num]][i+1])
                    c = (final_dict[rect_labels[num]][i+2])
                    newList.append(a + b + c)
                    next(myiter, None)
                    next(myiter, None)
                    count += 3
                else:
                    newList.append(final_dict[rect_labels[num]][i])
                    count +=1
            for i in range(count, len(final_dict[rect_labels[num]])):
                newList.append(final_dict[rect_labels[num]][i])
        if newList:
            final_dict[rect_labels[num]] = newList
    return final_dict

print(image_to_dict(coords, fields))
json_data = json.dumps(image_to_dict(coords, fields))
with open('mediScan_data.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
#specify where to upload data ?