from moviepy.audio.AudioClip import concatenate_audioclips, AudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

def generate_silence(duration=1, fps=44100):
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