import streamlit as st
import pickle
import base64

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Netflix Text Classification",
    page_icon="🎬",
    layout="centered"
)

# ------------------ Background Image Function ------------------
def set_background(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background
set_background("netflix_img.jpg")

# ------------------ Load Model ------------------
@st.cache_resource
def load_model():
    with open("netflix_text_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# ------------------ UI ------------------
st.markdown(
    "<h1 style='color:white;'>🎬 Netflix Text Classification</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='color:white;'>Predict the category using Netflix description text</p>",
    unsafe_allow_html=True
)

user_input = st.text_area(
    "Enter Netflix Description:",
    placeholder="A thrilling crime drama set in a dystopian future..."
)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        prediction = model.predict([user_input])[0]
        st.success(f"🎯 Predicted Category: **{prediction}**")

