import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load saved model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🔍 Fake Profile Detection App")
st.write("Enter profile details to check if account is Fake or Real")

# Inputs
followers = st.number_input("Followers", 0, 100000)
following = st.number_input("Following", 0, 100000)
posts = st.number_input("Posts", 0, 10000)
likes = st.number_input("Likes", 0, 10000)
comments = st.number_input("Comments", 0, 10000)
profile_pic = st.selectbox("Profile Picture", [1, 0])
bio_length = st.number_input("Bio Length", 0, 500)
account_age = st.number_input("Account Age (days)", 1, 5000)

# Prediction
if st.button("Predict"):

    input_data = pd.DataFrame([[followers, following, posts, likes, comments,
                                profile_pic, bio_length, account_age]],
                              columns=['followers','following','posts','likes',
                                       'comments','profile_pic','bio_length','account_age'])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🚨 Fake Account")
    else:
        st.success("✅ Real Account")