import numpy as np
import pandas as pd
from torchvision import transforms
from PIL import Image


def image_to_vector(img_path, model):
    # define suitable preprocess transformations for model (resnet50)
    # load image from image_path
    # transform image to vector using the model 
    # return vectorized image


def most_similar_vectors(image_vector, df_vectors):
    # load parquet file with vectorized dataset pictures
    # compare input image from user's camera with every vector from the dataset
    # return the path to the most similar image in the dataset
