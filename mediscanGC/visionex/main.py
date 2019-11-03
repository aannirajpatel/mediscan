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
	data = request.get_json(silent=True)
	coords = data["Coords"]
	names = data["Names"]
	#base64img = data["Image"]

	def image_to_dict(rect_coords, rect_labels, img_base64):
    	#json_input = input()#'JSON::{"img":"iVB...U5ErkJggg\u003d\u003d\n","fields":["kk"],"coords":[[206,368,728,685]]}'
		data = base64.b64decode(img_base64)
		client = vision.ImageAnnotatorClient()

		final_dict = {}
		image = vision.types.Image(content=data)
		response = client.document_text_detection(image=image) 
		texts = response.text_annotations
		stringTemp = ''

		charTemp = ''
		for num in range(len(rect_labels)):
			print(rect_labels[num])
			final_dict[rect_labels[num]] = []
			for page in response.full_text_annotation.pages:
				for block in page.blocks:
					for paragraph in block.paragraphs:
						for word in paragraph.words:
							for symbol in word.symbols:
								if (symbol.bounding_box.vertices[0].x > rect_coords[num][0] and
                                	symbol.bounding_box.vertices[0].y > rect_coords[num][1] and
                                	symbol.bounding_box.vertices[2].x < rect_coords[num][2] and
                                	symbol.bounding_box.vertices[2].y < rect_coords[num][3]):
									charTemp = symbol.text
                                	#confidence checker for '/', edit for clarity later
									if ((symbol.confidence < .65) and (symbol.text == '1' or symbol.text == '7') and
                                    	((rect_labels[num].lower() == "blood pressure" or rect_labels[num].lower() == "bp") or
                                    	(rect_labels[num].lower() == "pain") or
                                    	(rect_labels[num].lower() == "date/time" or rect_labels[num].lower() == "date" or 			rect_labels[num].lower() == "dob"))):
										charTemp = '/'
									print(stringTemp + " BEFORE")
									stringTemp += charTemp
									print(stringTemp + " AFTER")
									charTemp = ''

							if stringTemp:
                            #temp confidence checker
                            #if ((rect_labels[num].lower() == "temp") and (float(stringTemp) > 200)):
                                #final_dict[rect_labels[num]].append(stringTemp[0:len(stringTemp) - 1] + '.' + stringTemp[len(stringTemp) - 1])
                            #else:
								print("ADDING TO DICT")
								print(final_dict[rect_labels[num]])
								print(stringTemp)
								final_dict[rect_labels[num]] = stringTemp
								print(final_dict[rect_labels[num]])
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

	print(coords)
	print(coords[0])
	print(names)
	print(names[0])



	print(image_to_dict(coords, names, base64img))
	json_data = image_to_dict(coords, names, base64img)
	#json_data = json.dumps(image_to_dict(coords, names, base64img))
	print(json_data)

	#img = data["Image"]

	#print(img)
	
	return json.dumps({"result": json_data})#request.get_json(silent=True)})

if __name__ == '__main__':
    app.run(debug=True)
