# ################# FFMPEG function  #########################
import os
import subprocess

def extract_frames_and_audio(video_path, fps, quality):
    # Create output folder if it doesn't exist
    output_folder = "part0"
    os.makedirs(output_folder, exist_ok=True)
    
    # Frame extraction command
    frame_output_path = os.path.join(output_folder, "%04d.jpg")
    frame_command = [
        "ffmpeg",
        "-i", video_path,
        "-vf", f"fps={fps}",
        "-qscale:v", str(quality),
        frame_output_path
    ]
    
    # Execute frame extraction
    print("Extracting frames...")
    subprocess.run(frame_command, check=True)
    print(f"Frames saved in {output_folder}")
    
    # Audio extraction command
    audio_output_path = os.path.join(output_folder, "audio.mp3")
    audio_command = [
        "ffmpeg",
        "-i", video_path,
        "-q:a", "0",
        "-map", "a",
        audio_output_path
    ]
    
    print("Extracting audio...")
    try:
        subprocess.run(audio_command, check=True)
        print(f"Audio saved as {audio_output_path}")
    except subprocess.CalledProcessError:
        print("No audio stream found in the video, skipping audio extraction.")

if __name__ == "__main__":
    # Get user inputs
    video_path = input("Enter the path of the video file: ")
    fps = input("Enter desired FPS for frame extraction: ")
    quality = input("Enter quality level (1-31, lower is better): ")
    
    try:
        # Run extraction
        extract_frames_and_audio(video_path, fps, quality)
    except Exception as e:
        print(f"An error occurred: {e}")
