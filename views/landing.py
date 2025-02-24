import streamlit as st
from views.contacts import contact_form
#st.title("Nemish's Portfolio")

@st.dialog("contact")
def contact():
    contact_form()

col1,col2 = st.columns(2,gap='small',vertical_alignment='center')
with col1:
    st.image('statics/image1.png',width=270)
    st.write('***Build, learn, iterate—growth follows action.***')

with col2:
    st.title("Nemish Kyada ")
    st.write(''' AI Enthusiast | Exploring Generative AI, LLMs, and MLOps to build real-world solutions.

Always open to new projects, collaborations, and opportunities! 🚀 ''')
        
    st.divider()
    resume ='statics/Nemish_cv.pdf'

    bt1,bt2 = st.columns(2,gap='small',vertical_alignment='center')
    with bt1:
        st.download_button(
                label='Resume',
                data=open(resume,'rb').read(),
                file_name='Nemish_cv.pdf',
                mime='application/pdf',
                )
    with bt2:
        st.button('Contact',on_click=contact)

st.divider()

st.subheader('Experience')
st.write(''' ***Machine Learning Intern | Kogenie***
- Worked on LLM model tuning and Generative AI applications.
- Developed RAG-based systems for efficient retrieval and response generation.
- Built a website frontend using Next.js and implemented user management with Clerk.''')

st.divider()
st.subheader('Skills')

skills_css = """
<style>
.skills-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    margin-top: 15px;
}

.skill {
    background-color: #1E1E1E;
    color: #fff;
    font-size: 14px;
    padding: 6px 14px;
    border-radius: 18px;
    box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1);
    transition: 0.3s ease-in-out;
    cursor: pointer;
}

.skill:hover {
    box-shadow: 0px 0px 15px rgba(0, 255, 255, 0.8);
    transform: scale(1.1);
}
</style>
"""
# Inject CSS
st.markdown(skills_css, unsafe_allow_html=True)

# List of skills
skills = ["Python", "Machine Learning", "Deep Learning", "Torch", "Generative AI", 
          "SQL", "Streamlit", "RAG", "Computer Vision", "MLOps" , "DevOps","NLP", "LLM","Data Analytics", "DBMS", "React" , "NEXT" , "Sci-Kit learn" ,"Spacy" , "Keras" , "Pytorch"]

# Create HTML for skill bubbles
skills_html = '<div class="skills-container">'
for skill in skills:
    skills_html += f'<div class="skill">{skill}</div>'
skills_html += '</div>'

# Display the skills section
st.markdown(skills_html, unsafe_allow_html=True)