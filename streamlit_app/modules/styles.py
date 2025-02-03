import streamlit as st

def apply_styles():
    """Apply compact and visually appealing styles for the Homer Donut App."""
    st.markdown(
        """
        <style>
        /* Simpsons-Themed Streamlit App */
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #FCEFA1 !important;  /* Compact Yellow */
            color: #4A2F10 !important;  /* Darker Text for Readability */
            font-family: "Arial", sans-serif !important;
        }

        /* Navbar (Horizontal Bar) */
        header[data-testid="stHeader"] {
            background-color: #FFCC00 !important; /* Darker Yellow */
            color: black !important;
            border-bottom: 2px solid #E67E22;
        }

        /* Readable Headers */
        h1 {
            text-align: center;
            color: #FFAC33 !important; /* Brighter Orange */
            text-shadow: none !important;
            font-weight: bold;
            text-align: center;
            margin-bottom: 10px;
        }

        /* Improve GIF & Content Positioning */
        .simpsons-container {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            padding: 10px;
        }

        /* Buttons Styling */
        div.stButton > button {
            background-color: #FF9800 !important; /* Orange */
            border-radius: 5px !important;
            color: white !important;
            font-weight: bold !important;
            padding: 8px 15px;
            border: none;
            margin-bottom: 5px;
            width: 220px;
        }
        div.stButton > button:hover {
            background-color: #E67E22 !important; /* Darker Orange */
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #FFD90F !important; /* Sidebar Simpsons Yellow */
            color: black !important;
        }
        .main {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        
        /* Center buttons */
        .stButton {
            display: flex;
            justify-content: center;
        }

        /* Center GIFs */
        img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            text-align: center;
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )
