import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image
from torchvision import models
from src import helpers

model = models.resnet50(weights="ResNet50_Weights.DEFAULT")
model.eval()

# set the title of the application using st.title()

# use the st.camera_input("") feature of the streamlit to get the input picture of the user

# use a helper function to convert input picture to vector

# load the vectors of the dataset images

# use the helper function to compare vectors to the vector you created from the input picture

# use the path to the most similar image from the dataset to show image of the dog breed to the user

# parse the path to display the name of the dog breed as well :)
