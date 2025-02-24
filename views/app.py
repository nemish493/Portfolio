import streamlit as st

#pages
landing = st.Page(

    page ='views/landing.py',
    title= 'Home',
    icon = '🏠',
    default=   True
)

projects = st.Page(
    page = 'views/projects.py',
    title = 'Projects',
    icon = '👨‍💻',
    default = False
)

contact = st.Page(
    page = 'views/contacts.py',
    title = 'Contact',
    icon = '📧',
    default = False
)

page = st.navigation([landing,projects,contact])

page.run()