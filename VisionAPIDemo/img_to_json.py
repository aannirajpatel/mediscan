import os, io
from google.cloud import vision
from google.cloud.vision import types
import json
import datetime

#edit .vscode settings.json possibly for python path in cloud

#rectangle_list = [(x_1,y_1,x_2,y_2, column_label)]
#current assignment is an example sample for vital_signs.png
img = "image string input"
coordinates = "(x_1_a,y_1_a,x_2_a,y_2_a...)"
category_names = "(name_1, name_2...)"
#rectangle_list = [(264, 142, 393, 192, 'blood pressure'), (247, 198, 408, 252, 'pulse'), (239, 261, 405, 312, 'spo2'), (250, 319, 398, 380, 'weight'), (237, 381, 406, 435, 'temp'), (231, 432, 302, 466, 'pain'), (183, 465, 283, 510, 'pain')]
rectangle_list = [(269, 2065, 465, 2533, 'date'), (965, 2059, 1201, 2557, 'temp')]

#change later when given specific image input
#input_folder_path = r''
#s = 
#base64.decodestring(s)
# end of inputs

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'GoogleCloudDemo-fe3700bf4625.json'
client = vision.ImageAnnotatorClient()

image_path = r'C:\Users\justi\Code\GoogleCloudDemo\mediscan\VisionAPIDemo\photos\vital_chart.jpg'

def image_to_dict(rectangle_list):
    columns = {}
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
        image = vision.types.Image(content=content)
    response = client.document_text_detection(image=image) 
    texts = response.text_annotations
    stringTemp = ''
    charTemp = ''
    for tup in rectangle_list:
        columns[tup[4]] = []
        for page in response.full_text_annotation.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        for symbol in word.symbols:
                            if (symbol.bounding_box.vertices[0].x > tup[0] and
                                symbol.bounding_box.vertices[0].y > tup[1] and
                                symbol.bounding_box.vertices[2].x < tup[2] and
                                symbol.bounding_box.vertices[2].y < tup[3]):
                                charTemp = symbol.text
                                #confidence checker for '/', edit for clarity later
                                if ((symbol.confidence < .6) and (symbol.text == '1' or symbol.text == '7') and
                                    ((tup[4].lower() == "blood pressure" or tup[4].lower() == "bp") or
                                    (tup[4].lower() == "pain") or
                                    (tup[4].lower() == "date/time" or tup[4].lower() == "date" or tup[4].lower() == "dob"))):
                                    charTemp = '/'
                                stringTemp += charTemp
                                charTemp = ''
                        if stringTemp:
                            #temp confidence checker
                            #if ((tup[4].lower() == "temp") and (float(stringTemp) > 200)):
                                #columns[tup[4]].append(stringTemp[0:len(stringTemp) - 1] + '.' + stringTemp[len(stringTemp) - 1])
                            #else:
                                columns[tup[4]].append(stringTemp)
                        stringTemp = ''
        #google vision word spacing workaround, works 90% of the time
        newList = []
        if len(columns[tup[4]]) > 3:
            temp = 0
            myiter = iter(range(len(columns[tup[4]]) - 2))
            for i in myiter:
                print(columns[tup[4]])
                if (columns[tup[4]][i].isdigit() and
                (columns[tup[4]][i+1] == '/' or columns[tup[4]][i+1] == '.') and
                columns[tup[4]][i+2].isdigit()):
                    a = (columns[tup[4]][i])
                    b = (columns[tup[4]][i+1])
                    c = (columns[tup[4]][i+2])
                    newList.append(a + b + c)
                    next(myiter, None)
                    next(myiter, None)
                else:
                    newList.append(columns[tup[4]][i])
                print(newList)
            print(temp)
            if temp != 0:
                newList.append(columns[tup[4]][int(temp*-1)])
            print(newList)
        if newList:
            columns[tup[4]] = newList
    return columns

print(image_to_dict(rectangle_list))
#json_data = json.dumps(image_to_dict(rectangle_list)
#time = datetime.datetime.now()
##specify where to upload data
#with open('data.json' + time, 'w', encoding='utf-8') as f:
#    json.dump(json_data, f, ensure_ascii=False, indent=4)