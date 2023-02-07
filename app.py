import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image
from torchvision import models
from src import helpers

model = # download the pretrained model, e.g. resnet50
model.eval()


# set the title of the application using st.title()

# use the st.camera_input("") feature of the streamlit to get the input picture of the user

# load the vectors of the dataset pictures and use the helper function to compare them to the input

# print the result for the user! what dog breed is the selfie most similar to? :)
