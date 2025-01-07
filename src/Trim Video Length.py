from moviepy import VideoFileClip, AudioFileClip
from mutagen import MP3

def trim_video_to_audio(video_path, audio_path, output_path):
    # Load video and audio files
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    # Get the duration of the MP3 file
    audio_duration = MP3(audio_path).info.length

    # Trim the video to the length of the audio
    trimmed_video = video.subclip(0, audio_duration)

    # Set the audio of the trimmed video
    trimmed_video.audio = audio

    # Write the output video file
    trimmed_video.write_videofile(output_path)

if __name__ == "__main__":
    # Paths to your files
    video_file = "videos/output.mp4"
    audio_file = "mp3/merged_audio.mp3"
    output_file = "videos/trimmed_output.mp4"

    trim_video_to_audio(video_file, audio_file, output_file)

# Trim the video
trim_video_to_audio(video_file, audio_file, output_file)