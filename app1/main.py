 '''
how to run
- open terminal/console and type
- cd aap1
- streamlit run main.py  

'''

import streamlit as st

st.title("This is a title ")
st.header("this is heading")
st.subheader("this is subheading")
st.text("a very normal text on a normal text ")
st.write("this is the magic funtion to write stuff")
st.success("this is the magic funtion to success message")
st.error("this is a error message")
st.info("this is information message text")
st.warning("this is warnig text ")
st.markdown('''
            this ia a markdown text, here u are free to use 
<h5> html </h5>
<p> this is a para graph</p>
<ul type='circle'>
<li>one two</li>
<li>one two</li>
<li>one two</li> 
</ul>
or 
#markdorn heading
''', unsafe_allow_html=True)

st.code('area where we put code')
