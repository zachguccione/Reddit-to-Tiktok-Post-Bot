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

print(post_title)
print("")
print(comment_1)
print("")
print("")
print(question_brainrot)
print("")
print(comment_1_brainrot)