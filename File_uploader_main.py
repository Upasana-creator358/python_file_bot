import streamlit as st

def file_uploader():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:

        # To read file as bytes
        bytes_data = uploaded_file.getvalue()
        # st.write(bytes_data)

        # Comverting byte data to a sting data
        raw_data = bytes_data.decode('utf-8')

        return(str(raw_data))
