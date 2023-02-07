import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image
from torchvision import models
from src import helpers

model = models.resnet50(weights="ResNet50_Weights.DEFAULT")
model.eval()

st.title("What dog breed are you?")

col1, col2 = st.columns(2)

with col1:
    picture = st.camera_input("Take a picture!")

    if picture:
        vector = helpers.image_to_vector(picture, model)

    if picture is not None:
        img = Image.open(picture)
        img_array = np.array(img)

with col2:
    if picture:
        df_vectors = pd.read_parquet("./data/vectors.parquet")
        closest_breed = helpers.most_similar_vectors(vector, df_vectors)

        if closest_breed:
            image = Image.open(closest_breed)
            st.image(image, width=img_array.shape[1])

        st.text(f"You look a lot like {closest_breed.split('/')[-2]}!")
