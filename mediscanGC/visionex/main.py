import io
from flask import Flask
from google.cloud import vision, storage

app = Flask(__name__)

@app.route('/')
def main():
	storage_client = storage.Client()
	vision_client = vision.ImageAnnotatorClient()
	
	#files = storage_client.list_blobs("medical_forms")

	#for file_name in files:
		#print(file_name.name)
		#with io.open(file_name.name, 'rb') as image_file:
			#content = image_file.read()
			#image = vision.types.Image(content=content)

		#response = vision_client.label_detection(image=image)
		#labels = response.label_annotations

		#for label in labels:
			#print(label.description)
	
	return "hi"

if __name__ == '__main__':
    app.run(debug=True)

