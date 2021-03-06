#Library imports
import numpy as np
import streamlit as st
import cv2
from keras.models import load_model
import os

script_dir = os.path.dirname(__file__)
rel_path = "plant_disease.h5"
abs_file_path = os.path.join(script_dir, rel_path)

model = load_model(abs_file_path)

#if the loading above doesn't work just try
#model = load_model('copy the path manually to the plant_disease.h5 file')



CLASS_NAMES = ['Corn-Common_rust', 'Potato-Early_blight', 'Tomato-Bacterial_spot']

st.title("Plant Disease Detection")
st.markdown("Upload an image of the plant leaf")

plant_image = st.file_uploader("Choose an image...", type="jpg")
submit = st.button('Predict')
if submit:


    if plant_image is not None:

        file_bytes = np.asarray(bytearray(plant_image.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        st.image(opencv_image, channels="BGR")
        st.write(opencv_image.shape)
        opencv_image = cv2.resize(opencv_image, (256,256))
        opencv_image.shape = (1,256,256,3)
        Y_pred = model.predict(opencv_image)
        result = CLASS_NAMES[np.argmax(Y_pred)]
        st.title(str("This is "+result.split('-')[0]+ " leaf with " + result.split('-')[1]))
