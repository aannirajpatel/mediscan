import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'GoogleCloudDemo-fe3700bf4625.json'

client = vision.ImageAnnotatorClient()

FILE_NAME = 'vital_signs.png'
FOLDER_PATH = r'C:\Users\justi\Code\GoogleCloudDemo\VisionAPIDemo\photos'

with io.open(os.path.join(FOLDER_PATH, FILE_NAME), 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.document_text_detection(image=image)
texts = response.text_annotations

df = pd.DataFrame(columns=['locale', 'description'])
for text in texts:
    df = df.append(
        dict(
            locale=text.locale,
            description=text.description
        ),
        ignore_index=True
    )

print(df['description'][1:])
#print(response)
print(texts)