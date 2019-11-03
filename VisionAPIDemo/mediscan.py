import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd
import json
from google.protobuf.json_format import MessageToDict

# assign variables to inputs

#rectangle_list = [(x_1,y_1,x_2,y_2, column_label)]
#current assignment is to a sample input for blood pressure
rectangle_list = [(264, 142, 393, 192, 'blood pressure'), (247, 198, 408, 252, 'pulse'), (239, 261, 405, 312, 'spo2'), (250, 319, 398, 380, 'weight'), (237, 381, 406, 435, 'temp'), (231, 432, 302, 466, 'pain'), (183, 465, 283, 510, 'pain')]

#change later when given specific image input
input_folder_path = r'C:\Users\justi\Code\GoogleCloudDemo\VisionAPIDemo\photos'
# end of inputs

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'GoogleCloudDemo-fe3700bf4625.json'
client = vision.ImageAnnotatorClient()

#FILE_NAME = 'vital_signs.png'

def image_to_text(rectangle_list, folder_path):
    columns = {}
    for image_path in os.listdir(folder_path):
        with io.open(os.path.join(folder_path, image_path), 'rb') as image_file:
            content = image_file.read()
        image = vision.types.Image(content=content)
        response = client.document_text_detection(image=image) 
        texts = response.text_annotations
        r = MessageToDict(response)
        stringTemp = ''
        charTemp = ''
        for tup in rectangle_list:
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
                                        ((tup[4] == "blood pressure" or tup[4] == "bp") or
                                        (tup[4] == "pain"))):
                                        charTemp = '/'
                                    stringTemp += charTemp
                                    charTemp = ''
            print(tup[4])
            columns[tup[4]] = stringTemp
            #confidence checker temp
            if (tup[4] == "temp" and (float(stringTemp) > 200)):
                print('poop')
                columns[tup[4]] = stringTemp[0:len(stringTemp) - 1] + '.' + stringTemp[len(stringTemp) - 1]
            stringTemp = ''

        return columns
        #.get('pages', [])[0].get('property').get('detectedLanguages', [])[0].get('confidence')
print(image_to_text(rectangle_list, input_folder_path))

#with open('data.json', 'w', encoding='utf-8') as f:
#    json.dump(image_to_text(rectangle_list, input_folder_path), f, ensure_ascii=False, indent=4)
#print(df['description'][1:])
#print(response)