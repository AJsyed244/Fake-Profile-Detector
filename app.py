import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load saved model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🔍 Fake Profile Detection App")
st.write("Enter the details below")

# ---------- User Inputs ----------

followers = st.number_input("Followers", min_value=0, max_value=100000, step=10)

following = st.number_input("Following", min_value=0, max_value=100000, step=10)

posts = st.number_input("Posts", min_value=0, max_value=10000, step=1)

likes = st.number_input("Likes", min_value=0, max_value=10000, step=10)

comments = st.number_input("Comments", min_value=0, max_value=5000, step=5)

profile_pic = st.selectbox("Profile Picture", ["Yes", "No"])

bio_length = st.number_input("Bio Length", min_value=0, max_value=500, step=5)

account_age = st.number_input("Account Age (days)", min_value=1, max_value=5000, step=10)

# ---------- Prediction ----------

if st.button("Predict"):

    # Convert Yes/No to 1/0
    profile_pic_val = 1 if profile_pic == "Yes" else 0

    input_data = pd.DataFrame([{
    
        'followers': followers,
        'following': following,
        'posts': posts,
        'likes': likes,
        'comments': comments,
        'profile_pic': profile_pic_val,
        'bio_length': bio_length,
        'account_age': account_age
    }])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🚨 Fake Account")
    else:
        st.success("✅ Real Account")
