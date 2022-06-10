import streamlit as st

from PIL import Image
img = Image.open("perfume.jpg")
st.image(img, width=600)

st.title("Welcome to presh perfume collection ")

st.header("Use our scents to evoke positive memories")
st.subheader("Book for your preffered collection")

st.text("Enter the collection of your choice")

if st.checkbox("zara collection"):
    st.text("zara collection selected")

    
if st.checkbox("marque collection"):
    st.text("marque collection selected")
    
    
if st.checkbox("sauvage_dior collection"):
    st.text("sauvage_dior collection selected")
    
    
    
if st.checkbox("revolution collection"):
    st.text("revolution collection selected")
    
    
if st.checkbox("mousuf_perfume collection"):
    st.text("mousuf_perfume collection selected")
    
    
status = st.radio("select size: ", ('100ml', '300ml', '500ml', '700ml'))
    
    
if (status == '100ml'):
    st.success("100ml selected")
elif (status =='300ml'):
    st.success ('300ml selected')
elif (status =='500ml'):
    st.success ('500ml selected')
else:
    st.success('700ml selected')
    
name = st.text_input("Enter your name", "Type Here.....")

if(st.button("submit")):
    result = name.title()
    st.success("thank you for submitting")
    
level = st.slider("How satisfied are you on a scale of 5?", 1, 5)

st.text('selected:{}' .format(level))

    


  
