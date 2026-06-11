import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

from rag1.retriever import retrieve

# -------------------------------
# Load Environment Variables
# -------------------------------

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if api_key is None:
    st.error("❌ GROQ_API_KEY not found in .env file")
    st.stop()

# Initialize Groq Client
client = Groq(api_key=api_key)

# -------------------------------
# Streamlit Page Config
# -------------------------------

st.set_page_config(
    page_title="Project Intelligence Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Project Intelligence Assistant")
st.write("Ask questions about the PowerPoint Project Repository.")

# -------------------------------
# User Query
# -------------------------------

query = st.text_input("Enter your question")

if st.button("Search") and query:

    # Retrieve relevant slides
    results = retrieve(query, top_k=20)

    context = ""

    for r in results:
        context += f"""
Slide {r['slide_number']}:

{r['content']}

"""

    prompt = f"""
You are a Project Intelligence Assistant.

Answer ONLY using the retrieved context below.

Rules:
- Do NOT use outside knowledge.
- Do NOT hallucinate.
- If multiple projects match, list all.
- Include Project ID whenever available.
- Include Domain whenever available.
- Include Technology Stack whenever available.
- If the answer is not in the context, reply:
"I could not find this information in the project repository."

Context:
{context}

Question:
{query}

Answer:
"""

    with st.spinner("Generating Answer..."):

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

    answer = response.choices[0].message.content

    st.subheader("📌 Answer")
    st.write(answer)

    st.subheader("📄 Retrieved Slides")

    for r in results:
        st.markdown(f"### Slide {r['slide_number']}")
        st.write(r["content"])
        st.divider()