import numpy as np
import pandas as pd
from torchvision import transforms
from PIL import Image


def image_to_vector(img_path: str, model) ->  np.array:
    # define suitable preprocess transformations for our model (resnet50)
    # load image from image_path using PIL
    # transform image to vector using the model 
    # return vectorized image


def most_similar_vectors(image_vector: np.array, path_to_vectors: str) -> str:
    # load parquet file with vectorized dataset pictures
    # compare input image from user's camera with every vector from the dataset (use distance metric)
    # return the path to the most similar image in the dataset
