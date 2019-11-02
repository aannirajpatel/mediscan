import io
from google.cloud import vision

vision_client = vision.ImageAnnotatorClient()
file_name = 'roadsign.jpg'

with io.open(file_name, 'rb') as image_file:
	content = image_file.read()
	image = vision.types.Image(content=content)

response = vision_client.label_detection(image=image)
labels = response.label_annotations

for label in labels:
	print(label.description)

