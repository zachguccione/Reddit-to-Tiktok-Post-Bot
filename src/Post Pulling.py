from groq import Groq
from dotenv import load_dotenv
import os
import praw
import random
load_dotenv("keys.env")

# reddit API keys
reddit_key = os.getenv("REDDIT")
reddit_secret = os.getenv("REDDIT_SECRET")
user_agent = "Reddit TikTok Poster by /u/CriticalApartment675"

# accessing reddit API
reddit = praw.Reddit(
    client_id=reddit_key,
    client_secret=reddit_secret,
    user_agent=user_agent,
)

# Access the 'askreddit' subreddit and fetch hot posts
sub = reddit.subreddit('askreddit')
posts = [post for post in sub.hot(limit=10)]

# Select a random post
random_post_number = random.randint(0, len(posts) - 1)
post = posts[random_post_number]

# setting title of the selected post
post_title = post.title

# Fetch comments from the selected post
post.comments.replace_more(limit=0)  # Remove "More Comments" objects
comments = post.comments.list()

# selecting 2 of the top 5 comments
top_comments = sorted(comments, key=lambda x: x.score, reverse=True)[:20]
random_comments = random.sample(top_comments, 2)
comment_1 = random_comments[0].body
comment_2 = random_comments[1].body

# removing removed comments
def remove_removed(comment):
    if comment == "[removed]":
        while comment == "[removed]":
            i = random.randint(0,20)
            comment = random_comments[i]

remove_removed(comment_1)
remove_removed(comment_2)

# creating our input for our AI: title, 2 comments.
input = [post_title, comment_1, comment_2]

# Creating the AI response
api_key = os.getenv('GROQ')
client = Groq(api_key=api_key)

# Question to brainrot
chat_completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": "I don't want you to answer the question, I want you to re-ask me the question in brainrot. I want you to sound like a 10 year old. Use all the lingo. I need it to be readable."
        },
        {
            "role": "user",
            "content": post_title,
        }
    ]
)
question_brainrot = chat_completion.choices[0].message.content

# Comment 1 to brainrot
chat_completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": "convert this text I am giving you. I want you to sound like a 10 year old. Use all the lingo. I want this to be in complete words though, it needs to be readable."
        },
        {
            "role": "user",
            "content": comment_1,
        }
    ]
)
comment_1_brainrot = chat_completion.choices[0].message.content


# Comment 2 to brainrot
chat_completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": "convert this text I am giving you. I want you to sound like a 10 year old. Use all the lingo. I want this to be in complete words though, it needs to be readable."
        },
        {
            "role": "user",
            "content": comment_2,
        }
    ]
)
comment_2_brainrot = chat_completion.choices[0].message.content

# to text file
import os

def variable_to_file(variable_name, variable_value, folder_path):
    """
    Creates a text file with the variable name as the file name,
    saves it in the specified folder, and writes the variable value as the content.

    Args:
        variable_name (str): The name of the variable (used as the file name).
        variable_value (str): The value of the variable (written as the file content).
        folder_path (str): The path to the folder where the file should be saved.
    """
    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)

    # Define the file name and its full path
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    sanitized_name = ''.join('_' if char in invalid_chars else char for char in variable_name)
    file_path = os.path.join(folder_path, f"{sanitized_name}.txt")

    # Write the variable value to the file
    with open(file_path, "w") as file:
        file.write(variable_value)

    print(f"File '{file_path}' created with content: {variable_value}")


# folder
folder_path = "text files"
# post and comments to text file
variable_to_file("post", question_brainrot, folder_path)
variable_to_file("comment_1", comment_1_brainrot, folder_path)
variable_to_file("comment_2", comment_2_brainrot, folder_path)