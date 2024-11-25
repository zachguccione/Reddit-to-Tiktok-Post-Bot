from moviepy.audio.AudioClip import concatenate_audioclips, AudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip

def generate_silence(duration=1, fps=44100):
    """
    Generate a silence clip of the specified duration in seconds.
    """
    return AudioClip(lambda t: 0, duration=duration, fps=fps)

def merge_mp3_files_with_gap(file_list, output_file, gap_duration=1):
    clips = []

    for file in file_list:
        clip = AudioFileClip(file)
        clips.append(clip)

        # Add silence after each clip except the last one
        if file != file_list[-1]:
            silence = generate_silence(duration=gap_duration)
            clips.append(silence)

    # Combine all clips
    final_clip = concatenate_audioclips(clips)

    # Export the combined audio
    final_clip.write_audiofile(output_file)
    print(f"Merged audio saved as {output_file}")

# Example usage
merge_mp3_files_with_gap(["mp3/comment_0.mp3", "mp3/comment_1.mp3", "mp3/comment_2.mp3"], "mp3/merged_audio.mp3")


def add_audio_to_video(video_path, audio_path, output_path):

    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # Ensure audio clip is the same length as video clip
    audio_clip = audio_clip.set_duration(video_clip.duration)

    # Combine the audio and video clips
    final_clip = video_clip.set_audio(audio_clip)

    # Write the final clip to the output file
    final_clip.write_videofile(output_path, codec='libx264')

if __name__ == '__main__':
    video_file = "your_video.mp4"
    audio_file = "your_audio.mp3"
    output_file = "output_video.mp4"

    add_audio_to_video(video_file, audio_file, output_file)