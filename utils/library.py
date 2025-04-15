from PIL import Image
import streamlit as st
import io
import os
import subprocess
import shutil

try:
    subprocess.run(["pip", "install", "./assets/ultralytics"], check= True)
except:
    pass