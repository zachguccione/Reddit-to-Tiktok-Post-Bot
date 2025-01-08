from moviepy import VideoFileClip, AudioFileClip

def get_audio_length(file_path):
    audio_clip = AudioFileClip(file_path)
    return audio_clip.duration

audio_file = "mp3/merged_audio.mp3"
duration = get_audio_length(audio_file)
print(f"Audio duration: {duration} seconds")

def trim_video_to_audio(video_path, audio_path, output_path):
    # Get the duration of the audio file
    audio_duration = get_audio_length(audio_path)

    # Load the video file
    video_clip = VideoFileClip(video_path)

    # Trim the video to the length of the audio
    trimmed_video = video_clip.subclipped(0, audio_duration)

    # Set the audio of the trimmed video
    audio_clip = AudioFileClip(audio_path)
    trimmed_video = trimmed_video.with_audio(audio_clip)
    # Write the output video file
    trimmed_video.write_videofile(output_path, codec='libx264')

if __name__ == "__main__":
    # Paths to your files
    video_file = "videos/Subway Surfers.mp4"
    audio_file = "mp3/merged_audio.mp3"
    output_file = "videos/output.mp4"

    # Trim the video
    trim_video_to_audio(video_file, audio_file, output_file)