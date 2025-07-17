import streamlit as st
from transliterate import translit

st.set_page_config(page_title="Name Entry App", layout="centered")

st.title("🔤 Russian Name Input App")

st.write("Please enter the components of your name:")

# Input fields
first_name = st.text_input("First Name", max_chars=30)
middle_name = st.text_input("Middle Name (optional)", max_chars=30)
last_name = st.text_input("Last Name", max_chars=30)

full_name = first_name + middle_name + last_name

# Display result
if st.button("Generate Full Name"):
    if not first_name or not last_name:
        # transliterated = translit(full_name, 'ru', reversed=True)
        st.warning("Please enter at least First and Last names.")
    else:
        full_name = " ".join([first_name, middle_name, last_name]).strip()
        transliterated = translit(full_name, 'ru')
        st.success(f"Russian Full Name: **{transliterated}**")
        st.success(f"English Full Name: **{full_name}**")