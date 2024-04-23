import pandas as pd
import random

# Define topics
topics = [
    'Technology',
    'Entertainment',
    'Weather',
    'Education',
    'Politics',
    'Social',
    'Sports',
    'Food',
    'Travel',
    'Health'
]

# Generate sample tweets
def generate_tweet(topic):
    tweets = {
        'Technology': [
            "The new AI model is groundbreaking!",
            "I love coding in Python!",
            "Technology is evolving rapidly.",
            "Check out the latest smartphone!",
            "5G is changing the internet."
        ],
        'Entertainment': [
            "I can't wait for the new movie to release!",
            "Music festivals are the best.",
            "This show is binge-worthy!",
            "What's your favorite movie?",
            "The concert was amazing!"
        ],
        'Weather': [
            "It's so hot today, can't stand it!",
            "Rainy days are perfect for staying in.",
            "The snow is beautiful, but I hate shoveling.",
            "Windy days make me anxious.",
            "Weather forecasts can be unreliable."
        ],
        'Education': [
            "Learning is a lifelong journey.",
            "Exams are so stressful.",
            "I enjoy reading academic journals.",
            "Online courses are convenient.",
            "Education is the key to success."
        ],
        'Politics': [
            "The election results are in.",
            "Political debates can be intense.",
            "Voting is a civic duty.",
            "Government policies affect us all.",
            "Following politics can be exhausting."
        ],
        'Social': [
            "Hanging out with friends is the best!",
            "Social media is addictive.",
            "Community events are great for networking.",
            "I miss social gatherings.",
            "Volunteer work is rewarding."
        ],
        'Sports': [
            "Soccer is my favorite sport.",
            "The Olympics are always exciting.",
            "Team sports build camaraderie.",
            "I'm a huge football fan.",
            "Basketball games are so thrilling."
        ],
        'Food': [
            "I could eat sushi every day.",
            "Baking is my favorite hobby.",
            "I love trying new recipes.",
            "Pizza is life!",
            "Cooking shows are so inspiring."
        ],
        'Travel': [
            "Traveling is my passion.",
            "I can't wait to visit new places.",
            "The best part of traveling is the food.",
            "Backpacking is a great adventure.",
            "The airport security lines are so long."
        ],
        'Health': [
            "Exercise is essential for good health.",
            "I need to start eating healthier.",
            "Mental health is just as important.",
            "Yoga is a great stress reliever.",
            "Sleep is crucial for well-being."
        ]
    }
    return random.choice(tweets[topic])

# Create the dataset with 500 tweets
num_entries = 500
data = {
    'tweet': [generate_tweet(random.choice(topics)) for _ in range(num_entries)],
    'topic': [random.choice(topics) for _ in range(num_entries)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save DataFrame to a CSV file
df.to_csv('twiter2.csv', index=False)
print("Done")
