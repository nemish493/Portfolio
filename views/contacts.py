import streamlit as st
#import pymongo
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection function
def get_mongo_client():
    # Replace with your MongoDB connection string
    client = MongoClient("")  # For local MongoDB instance
    # If you're using MongoDB Atlas, you would use the connection string provided by Atlas
    return client

# Function for the contact form
def contact_form():
    # Title
    st.title("Contact Me")

    # Contact form
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message", height=150)

        # Submit button
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if name and email and message:
                # Save the data to MongoDB
                #client = get_mongo_client()
                #db = client["contact_form_db"]  
                #collection = db["submissions"]  

                # Create a dictionary to store the form data
                #contact_data = {
                 #   "name": name,
                  #  "email": email,
                   # "message": message,
                    #"timestamp": datetime.now()
                #}

                # Insert the data into the collection
                #collection.insert_one(contact_data)

                st.success(f"Thank you, {name}! Your message has been sent.")
            else:
                st.error("Please fill in all fields.")

    # Optional: Add a return button to go back to the home page
    if st.button("Back to Home"):
        
        st.write("Redirecting to home...")

contact_form()