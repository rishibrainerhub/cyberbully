import streamlit as st
from data_preprosesing import custom_input_prediction

st.header("Type of CyberBully")

# st.image("rename.png")

text = st.text_area("Enter tweet here", placeholder="Tweet")

b = st.button("Check")

if b:
    if text == "":
        st.info("enter some text")
    else:
        output = custom_input_prediction(text)
        if output == "Not Cyberbullying":
            st.success(output)
        else:
            st.warning(output)


st.markdown(
        '''### GitHub Repository: [cyberbully](https://github.com/rishibrainerhub/cyberbully)''')
