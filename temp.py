import pandas as pd

# Sample data
data = {
    'tweet': [
        "I love the new iPhone, it's amazing!",
        "Just watched the latest Avengers movie, it was awesome!",
        "The weather today is terrible, I hate rainy days.",
        "Learning new things is always exciting!",
        "Politics can be quite boring sometimes.",
        "Having a great time with friends at the beach!",
        "I'm so tired of studying for exams.",
        "Food is life, especially pizza!",
        "Feeling inspired after reading a good book.",
        "Traveling to new places is my passion."
    ],
    'topic': [
        'Technology',
        'Entertainment',
        'Weather',
        'Education',
        'Politics',
        'Social',
        'Education',
        'Food',
        'Education',
        'Travel'
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save DataFrame to a CSV file
df.to_csv('twitter_topic_classification_sample.csv', index=False)
