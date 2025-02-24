import streamlit as st
import webbrowser

st.title('These are some of my projects')

st.divider()

# List of projects
projects = [
    {
        "name": "Diabetes Prediction with machine Learning",
        "image": "statics/project1.png",  # Replace with actual image URL
        "short_desc": "A machine learning model that predicts diabetes in patients using a logistic regression model trained on a given dataset. The project features an interactive GUI developed with PyQt5.",
        "link": "https://github.com/nemish493/DiabeticPrediction",
        "col": 1
    },
    {
        "name": "Crop Prediction Model Deployment",
        "image": "statics/project2.png",
        "short_desc": "This project aims to learn about CI/CD pipelines and the deployment of a machine learning model for crop prediction using Docker",
        "link": "https://github.com/nemish493/ML_EndtoEnd",
        "col": 2
    },
    {
        "name": "Titanic Survival Prediction",
        "image": "statics/project3.jpg",
        "short_desc": "Full-fledged ML project to predict survival on Titanic dataset - With deployed website",
        "link": "https://github.com/nemish493/SWE_Titanic_survial_model",
        "col": 1
    },
    {
        "name": "Gesured Controlled Mouse",
        "image": "statics/project4.jpg",
        "short_desc": "This project implements a gesture-controlled mouse interface using computer vision and machine learning techniques. The system detects hand gestures via a webcam and translates them into mouse actions such as moving the cursor, left click, right click, double click, and taking screenshots.",
        "link": "https://github.com/nemish493/GestureControlledMouse",
        "col": 2
    }
]

# Display projects as cards
col1, col2 = st.columns(2, gap='large')  # Create columns dynamically

for project in projects:
    cols = col1 if project["col"] == 1 else col2
    with cols:
        st.image(project["image"], width=300)
        st.write(f"**{project['name']}**")
        st.write(project["short_desc"])
        if st.button(f"Learn More", key=project["name"]):
            webbrowser.open_new_tab(project["link"])
        st.divider()
