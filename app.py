import streamlit as st
import os

# Folder with your videos
VIDEO_DIR = "Videos"

# Get all .mp4 or .avi files in the folder
video_files = []
if os.path.exists(VIDEO_DIR):
    video_files = [f for f in os.listdir(VIDEO_DIR) if f.endswith(('.mp4', '.avi'))]

# Streamlit UI
st.set_page_config(page_title="🎥 Video Interface", layout="centered")
st.title("🎬 Video Viewer")

# Check if videos exist
if video_files:
    selected_video = st.selectbox("Select a video", video_files)
    video_path = os.path.join(VIDEO_DIR, selected_video)

    st.video(video_path)
else:
    st.warning("⚠️ No video files found in the 'videos/' folder. Please add some .mp4 or .avi files.")
