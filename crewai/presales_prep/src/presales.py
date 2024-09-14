import streamlit as st
import presales_prep.main as pp

st.title('Customer meeting preparation')
st.write('''This is a tool to help you prepare for a customer meeting.
    It will help you research the company and the topic of the meeting,
    and prepare a report to share with your team.''')
company = st.text_input('Company name')
topic = st.text_input('Topic')
st.button('Start')

result = pp.PresalesPrepCrew().crew().kickoff(inputs={'company': company, 'topic': topic})

if result:
    st.write(result)
