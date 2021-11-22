import streamlit as st
import urllib

def main():
    #st.title('1 M and 2 Cs')
    #st.header('Notes on machine learning, cryptocurrency, and cybersecurity')
    intro_text = get_file_content_as_string('README.md')
    st.markdown(intro_text)

@st.cache(show_spinner=False)
def get_file_content_as_string(path):
    url = 'https://raw.githubusercontent.com/amanovv/notesontech/main/' + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")

if __name__ == "__main__":
  main()