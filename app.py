import streamlit as st
from classify import classify_article

st.set_page_config(page_title="German Article Classifier", page_icon="📚")

st.title("📘 German Article Classifier")
st.write("Enter a German noun to see its definite article (**der**, **die**, or **das**).")

user_input = st.text_input("Enter a noun:")

if user_input:
    cleaned_noun = user_input.strip().capitalize()
    result = classify_article(cleaned_noun)
    
    if result != "Unknown":
        st.success(f"**{result} {cleaned_noun}**")
    else:
        st.error(f"Sorry, the article for **{cleaned_noun}** is not in the dictionary.")
