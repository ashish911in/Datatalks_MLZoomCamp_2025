import numpy as np
import onnxruntime as ort
from io import BytesIO
from urllib import request
from PIL import Image

# Use the specific filename from the base image
MODEL_FILE = 'hair_classifier_empty.onnx'

interpreter = ort.InferenceSession(MODEL_FILE)
input_name = interpreter.get_inputs()[0].name

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    return img.resize(target_size, Image.NEAREST)

def preprocess_input(img):
    x = np.array(img, dtype='float32')
    x /= 255.0
    mean, std = np.array([0.485, 0.456, 0.406]), np.array([0.229, 0.224, 0.225])
    x = (x - mean) / std
    return np.expand_dims(x.transpose(2, 0, 1), axis=0)

def lambda_handler(event, context):
    url = event['url']
    with request.urlopen(url) as resp:
        img = Image.open(BytesIO(resp.read()))
    
    img = prepare_image(img, (200, 200))
    x = preprocess_input(img)
    
    preds = interpreter.run(None, {input_name: x})
    return float(preds[0][0][0])