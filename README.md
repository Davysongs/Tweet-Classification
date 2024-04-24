# Multi-class Twitter Topic Classification Project

Welcome to the Multi-class Twitter Topic Classification project. This project focuses on building a Natural Language Processing (NLP) pipeline to classify tweets into multiple topics. The aim is to develop a robust system that can categorize short texts (tweets) into predefined classes for analysis, research, or other applications.

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Methodology](#methodology)
4. [Pipeline](#pipeline)
5. [Modeling](#modeling)
6. [Evaluation](#evaluation)
7. [Setup and Installation](#setup-and-installation)
8. [Usage](#usage)
9. [Future Work](#future-work)
10. [Contributors](#contributors)

## Introduction
Twitter has become a key platform for public discourse, where people share opinions, news, and other information in short messages. This project explores multi-class classification of tweets, allowing us to categorize tweets into distinct topics, facilitating further analysis and insights.

In this project, we use a synthetic dataset to classify tweets into 10 different topics: Technology, Entertainment, Weather, Education, Politics, Social, Sports, Food, Travel, and Health. The classification model relies on the TF-IDF (Term Frequency-Inverse Document Frequency) vectorization technique and a Multinomial Naive Bayes classifier.

## Dataset
A synthetic dataset is used in this project. It consists of 500 tweets, each associated with one of the 10 predefined topics. The tweets are generated to simulate typical Twitter messages, including a variety of contexts and themes.

The dataset is provided in CSV format with the following columns:
- `tweet`: The text of the tweet.
- `topic`: The topic/category to which the tweet belongs.

To use this dataset in the project, download or generate it and ensure it's accessible to the Python scripts.

## Methodology
The project follows the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology, consisting of six phases:

1. **Business Understanding**: Define the problem and set the project's objectives.
2. **Data Understanding**: Explore and understand the dataset.
3. **Data Preparation**: Prepare the data for modeling, including cleaning and feature engineering.
4. **Modeling**: Build the classification model.
5. **Evaluation**: Evaluate the model's performance and validate the results.
6. **Deployment**: Deploy the model for practical use (not covered in this project).

## Pipeline
The pipeline for this project consists of the following steps:

1. **Load the Dataset**: Load the CSV file into a pandas DataFrame for easy manipulation.
2. **Data Splitting**: Split the data into training and testing sets (80% for training and 20% for testing).
3. **Feature Extraction**: Use TF-IDF to convert text data into numerical features.
4. **Model Training**: Train the Multinomial Naive Bayes classifier using the training set.
5. **Model Prediction**: Predict the topics of the test set.
6. **Evaluation**: Use classification metrics to evaluate the model's performance.

## Modeling
For this project, we use the following approach for modeling:

- **Text Vectorization**: TF-IDF vectorizer with a maximum of 1000 features. TF-IDF helps identify the importance of words in a document relative to the entire corpus.
- **Classifier**: Multinomial Naive Bayes, a simple yet effective classifier for text data. It assumes that the presence or absence of a particular word is independent of the presence or absence of other words.
- **Parameter Settings**: Basic settings for TF-IDF and Naive Bayes. Future work could involve tuning parameters for better performance.

## Evaluation
To evaluate the model, we use the following metrics:

- **Precision**: Measures the proportion of correct predictions among the predicted classes.
- **Recall**: Measures the proportion of correct predictions among the actual classes.
- **F1-Score**: Harmonic mean of precision and recall.
- **Accuracy**: Overall accuracy of the classifier.

We also use the `zero_division` parameter in the classification report to avoid warnings when precision or recall is ill-defined due to classes with no predicted samples.

## Setup and Installation
To set up the project environment, you need Python and several packages. Here's a step-by-step guide:

1. **Clone the Repository**: Download or clone this project repository.
2. **Install Python**: Ensure Python 3.6 or later is installed.
3. **Install Dependencies**: Use `pip install -r requirements.txt` to install necessary packages. Common packages include `pandas`, `sklearn`, `numpy`, etc.
4. **Load the Dataset**: Place the CSV file in the appropriate location for the scripts to access.

## Usage
After setting up the project, follow these steps to run the pipeline:

1. **Run the Python Script**: Execute the script that contains the pipeline. This will load the dataset, train the model, and evaluate its performance.
2. **Analyze the Results**: Review the classification report to understand the model's effectiveness. Adjust the script or dataset as needed for further experimentation.
3. **Experiment with Changes**: Explore different classifiers, parameter settings, or data augmentation techniques to improve the results.

## Future Work
The project offers several opportunities for further development:

- **Data Augmentation**: Increase dataset size and diversity to improve the model's generalization.
- **Advanced Text Processing**: Apply additional NLP techniques such as tokenization, lemmatization, and stopword removal.
- **Model Tuning**: Adjust parameters and explore different classifiers for better performance.
- **Feature Engineering**: Experiment with additional features like sentiment analysis or word embeddings.
- **Deployment**: Consider deploying the model in a real-world application, such as a web service or social media monitoring tool.

## Contributors
If you have contributed to this project, list your name and role here.

- **[Godson David]** - Project Lead, NLP Pipeline Developmen

Thank you for exploring this project! If you have any questions or suggestions, feel free to reach out.
