#########################################################
#   TIMETRACKER using Face Detection and Streamlit      #
#   Author: Dalton Hardt           Date:  Feb/2024      #
#########################################################

import cv2
import numpy as np
import mediapipe as mp
import time
import os
import streamlit as st
import sys
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer


# Inicializando Stramlit
st.set_page_config(page_title="Time Tracker", page_icon="✅", layout="wide")
st.title("Time Tracker")
st.subheader("Snooze:")
col1, col2 = st.columns([0.2, 0.8])  # Adjust column ratios as needed

with col1:
    snooze10 = st.button(":one::zero:", use_container_width=True)
    snooze30 = st.button(":three::zero:", use_container_width=True)
    sair = st.button("PARAR", use_container_width=True)
    if snooze10:
        st.write("+10 min")
    elif snooze30:
        st.write("+30 min")
    elif sair:
        st.stop()

# Capturando Video
# with col2:
#    img_file_buffer = st.camera_input("Video")


