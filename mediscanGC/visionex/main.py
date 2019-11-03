import os, io
import base64
from flask import Flask, request, json
from google.cloud import vision
from google.cloud.vision import types
import json
import sys

app = Flask(__name__)

fileID = 0
fileString = "medForm"

#def create_file(fileName):
		#response.write("Creating file %s \n" % fileName)
		#storage_client = storage.Client()
		#write_retry_params = gcs.RetryParams(backoff_factor=1.1)
		#gcs_file = gcs.open(fileName, 'w', content_type='text/plain', options={'x-goog-meta-foo': 'foo', 'x-goog-meta-bar': 'bar'}, retry_params=write_retry_params)
  		
		#gcs_file.write('abcde\n')
		#gcs_file.write('f'*1024*4 + '\n')
		#gcs_file.close()
		#tmp_filenames_to_clean_up.append(fileName)

@app.route('/', methods=['POST'])
def main():
	print(request.get_json(silent=True))
	js = request.get_json(silent=True)
	coordinates = js["Coords"]
	category_names = js["Names"]
	base64img = js["Image"]
	print(coordinates)
	print(coordinates[0])
	print(len(category_names))

	client = vision.ImageAnnotatorClient()

	rectangle_list= []
	x = []
	for i in range(len(category_names)):
		for j in range(len(coordinates[0])):
			print(coordinates[i][j])
			x.append(coordinates[i][j])
		x.append(category_names[i])
		rectangle_list.append(x)
		x = []
	print(rectangle_list)

	def image_to_dict(rectangle_list):
		columns = {}
		image = vision.types.Image(content=data)
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
				if temp != 0:
					newList.append(columns[tup[4]][int(temp*-1)])
			if newList:
				columns[tup[4]] = newList
		return columns
	
	data = base64.b64decode(base64img)

	print(image_to_dict(rectangle_list))
	json_data = image_to_dict(rectangle_list)
	#json_data = json.dumps(image_to_dict(coords, names, base64img))
	print(json_data)


	#print(img)
	
	return json.dumps({"result": json_data})#request.get_json(silent=True)})

if __name__ == '__main__':
    app.run(debug=True)

