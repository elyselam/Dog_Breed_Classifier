import tensorflow as tf
import os
import keras
import numpy as np
from keras.preprocessing import image
from keras.applications.vgg19 import (VGG19, preprocess_input, decode_predictions)
import pickle

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def predict(image_path):
    model = VGG19(include_top=True, weights='imagenet')
    tf.get_default_graph()
    
    image_size = (224, 224)
    """Use VGG19 to label image"""

    print(dir(image))
    img = image.load_img(image_path, target_size=image_size)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    #model = pklfile
    
    predictions = model.predict(x)
    result = decode_predictions(predictions, top = 5)[0]
    
    output = []
    for i in result:
        dog_name = i[1].split("_")
        dn = ""
        for j in dog_name:
            dn += f'{j} '.capitalize()
        percent = str(round(i[2] * 100, 1)) + "%"
        dn = dn.rstrip()
        output.append(f"{dn}: {percent}")

    return output
