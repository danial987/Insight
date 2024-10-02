import streamlit as st
from pathlib import Path
import importlib.util
import os
from pages.dataset_summary import dataset_summary_page

# Load custom CSS
def load_css():
    css_file = Path('static/style.css')
    if css_file.exists():
        with open(css_file) as f:
            css_code = f.read()
        st.markdown(f'<style>{css_code}</style>', unsafe_allow_html=True)
    else:
        st.warning("CSS file not found!")

# st.set_page_config(page_title="InsightPilot", page_icon="🧠")

# Adding a logo to the sidebar with specified width
logo_file = Path("static/logo.png")
if logo_file.exists():
    st.sidebar.image(str(logo_file), width=200)  # Set the desired width in pixels
else:
    st.warning("Logo file not found!")

# Page routing using session state
PAGES = {
    "Dataset Upload": "pages/dataset_upload.py",
    "Search Dataset": "pages/search_dataset.py",
    "Dataset Summary": "dataset_summary_page",
    "Data Preprocessing": "pages/data_preprocessing.py",
    "Data Visualization": "pages/data_visualization.py",
    "Chatbot": "pages/chatbot.py"
}

# Sidebar navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()), index=0)

# Dynamic page loading
page_path = Path(PAGES[selection])

# Function to dynamically import a Python module
def load_page(page_path):
    module_name = page_path.stem  # Get the module name from the file path
    if page_path.exists():
        spec = importlib.util.spec_from_file_location(module_name, page_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)  # Execute the module's code
    else:
        st.error(f"Could not find page: {page_path}. Make sure the file exists in the 'pages' directory.")

# Try to load the selected page
try:
    load_page(page_path)
except Exception as e:
    st.error(f"An error occurred while loading the page: {str(e)}")




# import streamlit as st
# from st_pages import Page, Section, add_page_title
# from pathlib import Path

# def load_css():
#     with open('static/style.css') as f:
#         css_code = f.read()
#     st.markdown(f'<style>{css_code}</style>', unsafe_allow_html=True)

# st.set_page_config(page_title="InsightPilot", page_icon="🧠")

# # Adding a logo to the sidebar with specified width
# st.sidebar.image("static/logo.png", width=200)  # Set the desired width in pixels

# # Define pages
# pages = [
#     st.Page("pages/dataset_upload.py", title="Dataset Upload", icon="⬆️"),
#     st.Page("pages/search_dataset.py", title="Search Dataset", icon="🔍"),
#     st.Page("pages/dataset_summary.py", title="Dataset Summary", icon="📊"),
#     st.Page("pages/data_preprocessing.py", title="Data Preprocessing", icon="🔧"),
#     st.Page("pages/data_visualization.py", title="Data Visualization", icon="📈"),
#     st.Page("pages/chatbot.py", title="Chatbot", icon="🤖")

# ]

# pg = st.navigation(pages)
# pg.run()
