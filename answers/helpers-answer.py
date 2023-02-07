import numpy as np
import pandas as pd
from torchvision import transforms
from PIL import Image


def image_to_vector(img_path, model):
    preprocess = transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
    input_image = Image.open(img_path)
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)
    vector = model(input_batch)[0].detach().numpy()

    return vector


def most_similar_vectors(image_vector, df_vectors):
    min_dist = float("inf")
    closest_breed = None

    for i, row in df_vectors.iterrows():
        dist = np.linalg.norm(image_vector - row["vector"])
        if dist < min_dist:
            min_dist = dist
            closest_breed = row["img_path"]

    return closest_breed
