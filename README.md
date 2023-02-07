# dog-breed-streamlit-app

## Steps:

## 1. Go to vectorize_dataset.ipynb

- download a pretrained neural network with resnet50 architecture
- use this model to create a vector representation of each image in our dataset
- store the vectors and their corresponding image filepaths as dataframe with two columns: vector, img_path
- save the dataframe to parquet format

## 2. Go to src.helpers.py

Fill the missing lines in predefined functions based on comments:

- image_to_vector():
  - define suitable preprocess transformations for our model (resnet50)
  - load image from image_path using PIL
  - transform image to vector using the model
  - return vectorized image
- most_similar_vectors():
  - load parquet file with vectorized dataset pictures
  - compare input image from user's camera with every vector from the dataset (use distance metric)
  - return the path to the most similar image in the dataset

## 3. Go to app.py

- with the help of documentation https://docs.streamlit.io/library/get-started/create-an-app and comments create your streamlit application!

#### **Hint**

_In case you get stuck or you need an inspiration, take a sneak peek into the answers/ folder_

---

## Too easy? Try adding more complexity

    # enrich the page layout, add texts, input fields, result metrics - be creative :)

    # add cats dataset from https://www.kaggle.com/datasets/ma7555/cat-breeds-dataset - ask the user if he/she/it is a cat or dog person and display the result image based on the answer

    # push your project into GitHub repository and deploy your app to streamlit cloud https://streamlit.io/cloud

    # or simply publish your Deepnote project and share it around!
