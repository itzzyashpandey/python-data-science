from email import message
import streamlit as st 
st.title("simple Form")
with st.form('My Form'):
    name = st.text_input("enter your age")
    age = st.number_input("enter ur age", min_value=18,max_value=90)
    message = st.text_area("enter your thoughts ")
    time = st.time_input("enter what the time")
    date = st.date_input("enter the date")
    file = st.file_uploader("select a file")
    camera = st.camera_input("take a photo")
    sb = st.form_submit_button("submit")   
    
if sb: 
    st.write(name)
    st.write(age)
    st.write(message)
    st.write(time)
    st.write(date)
    st.write(file)
    st.write(camera)
    
    
with st.form('Another Form'):
    color= st.color_picker("select ur color")
    num1 = st.select_slider("select a value", [1,5,10,15,20,25])
    num2= st.slider("select another value", min_value=25,max_value=100,step=5)
    gender = st.radio("Gender",['Male','Female','other'],horizontal=True)
    education= st.selectbox("select ur height education",
                            ['Intermidiate','High schol','Graduate','Master','Pade likhe Gawar'])
    choices=st.multiselect("select what u like ",
                           ['maggi', 'pizaz','spanish','dry fruit','noodles','🥙'])
    is_checked = st.checkbox('agree to our secret term and condition ', value=True)
    sb2= st.form_submit_button("submit")