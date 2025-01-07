from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

def add_audio_to_video(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # Ensure audio clip is the same length as video clip
    audio_clip = audio_clip.with_duration(audio_clip.duration)

    # Combine the audio and video clips
    final_clip = video_clip.with_audio(audio_clip)

    # Write the final clip to the output file
    final_clip.write_videofile(output_path, codec='libx264')

if __name__ == '__main__':
    video_file = "videos/Subway Surfers.mp4"
    audio_file = "mp3/merged_audio.mp3"
    output_file = "videos/output.mp4"

    add_audio_to_video(video_file, audio_file, output_file)