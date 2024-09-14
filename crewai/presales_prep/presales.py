import streamlit as st

st.title('Customer meeting preparation')
st.write('''This is a tool to help you prepare for a customer meeting.
    It will help you research the company and the topic of the meeting,
    and prepare a report to share with your team.''')
company = st.text_input('Company name')
topic = st.text_input('Topic')
st.button('Start')

if company and topic:
    st.write(f'Preparing for meeting with {company} on {topic}')
