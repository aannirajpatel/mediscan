import io
import requests
from flask import Flask
from google.cloud import vision, storage

app = Flask(__name__)

@app.route('/')
def main():
	storage_client = storage.Client()
	vision_client = vision.ImageAnnotatorClient()
	
	files = storage_client.list_blobs("medical_forms")
	key = "AIzaSyD_jpxC4BEv1v7uUG3_0EwG8qzlM6TxDXw"

	for file_name in files:
		print("FILEPATH")
		print(file_name.public_url)
		js = {
  				"requests":[
    							{
      								"image":{
        								"source":{
          										"imageUri": file_name.public_url
        										}
      										},
     								 "features":[
        									{ "type":"TEXT_DETECTION",
          										"maxResults":10
        									}
      											]
    							}
  							]
				}
		r = requests.post(url = "https://vision.googleapis.com/v1/images:annotate?key=AIzaSyD_jpxC4BEv1v7uUG3_0EwG8qzlM6TxDXw", json = js)
		json = r.json()
		#print(json['responses'][0]['textAnnotations'])
		for x in json['responses'][0]['textAnnotations']:
			print(x['description'])
	
	return "hi"

if __name__ == '__main__':
    app.run(debug=True)

