import io
import base64
from flask import Flask, request, json
from google.cloud import vision#, storage

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
	fields = request.form['Fields']
	rectCoords = request.form['Coords']
	img = base64.b64decode(request.form['Image'])
	vision_client = vision.ImageAnnotatorClient()

	with io.open(img, 'rb') as image_file:
		content = image_file.read()
		image = vision.types.Image(content=content)

	response = vision_client.label_detection(image=image)
	labels = response.label_annotations

	for label in labels:
		print(label.description)
	
	return json.dumps({"result": "here"})

if __name__ == '__main__':
    app.run(debug=True)

