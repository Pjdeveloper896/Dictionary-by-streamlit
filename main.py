import streamlit as st
import requests

st.title("Dictionary")
st.markdown("# Dictionary App")

col1, col2 = st.columns(2)

with col1:
    st.image(
        "https://media.istockphoto.com/id/849396234/photo/thesaurus-and-dictionary-isolated-on-white.jpg?s=1024x1024&w=is&k=20&c=9AGZgjaTNm4omZ73I-9JuHW128_jTdpuCMFMAyIgC44=",
        width=200)

with col2:
    word = st.text_input("Enter word to search")
    button = st.button("Search")

if button and word:
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        st.success(f"Results for: **{data[0]['word']}**")

        for meaning in data[0]["meanings"]:
            with st.expander(f"{meaning['partOfSpeech'].capitalize()}"):
                for idx, definition in enumerate(meaning["definitions"]):
                    st.markdown(f"**Definition {idx+1}:** {definition['definition']}")
                    if "example" in definition:
                        st.markdown(f"_Example:_ {definition['example']}")
                    st.markdown("---")
    else:
        st.error("Word not found. Try another one.") 
        
slidebar = st.sidebar.text_input("enter your name ")
st.sidebar.write(f" Welcome {slidebar}")