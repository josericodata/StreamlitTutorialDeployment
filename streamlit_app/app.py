import streamlit as st
import time
from modules.styles import apply_styles
from modules.utils import *

st.set_page_config(page_title="Homer Eating Donuts", page_icon="🍩")

# Apply styles
apply_styles()

st.title("Homer Simpson Eating Donuts")

# Initialize session state variables
if "eating" not in st.session_state:
    st.session_state.eating = False
if "donut_count" not in st.session_state:
    st.session_state.donut_count = 0
if "current_gif" not in st.session_state:
    st.session_state.current_gif = HOMER_HUNGRY  # Default to Hungry Homer
if "homer_message" not in st.session_state:
    st.session_state.homer_message = "Help Homer eat as many donuts as possible!"  # Initial message

# UI Components
gif_placeholder = st.empty()
text_placeholder = st.empty()  # Placeholder for dynamic text
placeholder = st.empty()
counter_placeholder = st.empty()

# Display the current text message
with text_placeholder:
    st.markdown(f"<div class='simpsons-container'><h3>{st.session_state.homer_message}</h3></div>", unsafe_allow_html=True)

# Ensure Homer starts hungry at the beginning
load_gif(HOMER_HUNGRY, gif_placeholder)

# Start & Stop Buttons
if st.button("Start Throwing Donuts"):
    st.session_state.eating = True
    st.session_state.donut_count = 0  # Reset counter
    st.session_state.homer_message = "Homer is delighted eating donuts! 🍩😋"
    
    with text_placeholder:
        st.markdown(f"<div class='simpsons-container'><h3>{st.session_state.homer_message}</h3></div>", unsafe_allow_html=True)

    gif_placeholder.empty()  # Clear hungry gif before animation starts

if st.button("Stop Throwing Donuts"):
    st.session_state.eating = False
    st.session_state.homer_message = "Oh no! Homer is heartbroken—he needs more donuts! 😢"
    
    with text_placeholder:
        st.markdown(f"<div class='simpsons-container'><h3>{st.session_state.homer_message}</h3></div>", unsafe_allow_html=True)

    load_gif(HOMER_CRYING, gif_placeholder)  # Show crying Homer when stopping

# Donut Animation when Eating Starts
if st.session_state.eating:
    gif_placeholder.empty()  # Remove hungry GIF
    animation_html = generate_animation_html()

    while st.session_state.eating:
        placeholder.markdown(animation_html, unsafe_allow_html=True)
        time.sleep(2)
        st.session_state.donut_count += 1
        counter_placeholder.markdown(f"<div class='simpsons-container'><h3>Donuts Eaten: {st.session_state.donut_count}</h3></div>", unsafe_allow_html=True)

# Show Crying Homer When Stopping
if not st.session_state.eating and st.session_state.donut_count > 0:
    placeholder.empty()  # Clear animation
    load_gif(HOMER_CRYING, gif_placeholder)
