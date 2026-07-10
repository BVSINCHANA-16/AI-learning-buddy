import streamlit as st
from google import genai

# Read API key from Streamlit Secrets
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓"
)

st.title("🎓 Sinchana - The Binary Tutor")

topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 MCQs on {topic} with answers."

        else:
            prompt = topic

        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )

        st.write(response.text)
