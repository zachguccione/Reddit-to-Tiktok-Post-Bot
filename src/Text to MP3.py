from gtts import gTTS
import os

def file_to_string(file_name):
    """
    Reads the content of a text file and returns it as a string.

    Args:
        file_name (str): The name of the text file to read.

    Returns:
        str: The content of the text file.
    """
    try:
        with open(file_name, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file '{file_name}' does not exist."
    
post = file_to_string("text files/post.txt")
comment_1 = file_to_string("text files/comment_1.txt")
comment_2 = file_to_string("text files/comment_2.txt")

# Text to convert
comments = [post, comment_1, comment_2]

# Specify the folder for MP3 files
folder = "mp3"

# Ensure the folder exists
os.makedirs(folder, exist_ok=True)

# Generate MP3 files in the specified folder
for i, text in enumerate(comments):
    file_path = os.path.join(folder, f"comment_{i}.mp3")  
    tts = gTTS(text=text, lang='en')                     
    tts.save(file_path)                                  
    print(f"Generated {file_path}")