import os
import base64
import streamlit as st

# Define paths
BASE_PATH = os.path.dirname(os.path.dirname(__file__))  # Adjust for modules folder
ASSETS_PATH = os.path.join(BASE_PATH, "assets")
GIFS_PATH = os.path.join(ASSETS_PATH, "gifs")
IMG_PATH = os.path.join(ASSETS_PATH, "img")

# Paths for assets
HOMER_HUNGRY = os.path.join(GIFS_PATH, "homerHungry.gif")
HOMER_CRYING = os.path.join(GIFS_PATH, "homerCrying.gif")
DONUT_PATH = os.path.join(IMG_PATH, "donut.png")
HOMER_PATH = os.path.join(IMG_PATH, "homer.png")

def get_base64_image(image_path):
    """Convert an image file to a base64-encoded string for HTML embedding."""
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    else:
        st.error(f"File not found: {image_path}")
        return ""

def load_gif(gif_path, placeholder):
    """Display a GIF in Streamlit properly using HTML for continuous looping."""
    base64_gif = get_base64_image(gif_path)
    if base64_gif:
        gif_html = f"""
        <div class="simpsons-container">
            <img src="data:image/gif;base64,{base64_gif}" class="homer-gif" />
        </div>
        """
        placeholder.markdown(gif_html, unsafe_allow_html=True)

def generate_animation_html():
    """Generate HTML for the moving donut towards Homer."""
    donut_base64 = get_base64_image(DONUT_PATH)
    homer_base64 = get_base64_image(HOMER_PATH)

    return f"""
    <html>
    <head>
    <style>
    @keyframes move-donut {{
      0% {{ transform: translateX(-100%) translateY(-10px); }}
      90% {{ transform: translateX(200%) translateY(0); }}
      100% {{ transform: translateX(240%) translateY(0); }}
    }}
    .container {{
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
    }}
    .donut {{
      width: 100px;
      height: 100px;
      position: absolute;   /* Allows precise positioning */
      left: 50px;           /* Adjust starting position */
      top: 105px;           /* Move it downward */
      animation: move-donut 2s linear infinite;
      z-index: 5;  /* Ensure the donut is behind */
    }}
    .homer {{
      width: 150px;
      height: auto;
      margin-top: 20px;
      right: 20px;          /* Move Homer to the right */
      bottom: 50px;         /* Adjust vertical position */
      z-index: 10;  /* Ensure Homer appears in front */
    }}
    </style>
    </head>
    <body>
      <div class="container">
        <img src="data:image/png;base64,{homer_base64}" class="homer" />
        <img src="data:image/png;base64,{donut_base64}" class="donut" />
      </div>
    </body>
    </html>
    """
