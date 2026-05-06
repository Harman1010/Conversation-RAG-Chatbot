import streamlit as st
import json


st.title("Conversation Persona Chatbot")


with open(
    "persona.json",
    "r",
    encoding="utf-8"
) as file:

    persona = json.load(file)


with open(
    "checkpoints/topic_checkpoints.json",
    "r",
    encoding="utf-8"
) as file:

    topic_checkpoints = json.load(file)


query = st.text_input(
    "Ask something about the user"
)


if query:

    st.subheader("Relevant Topics")

    query_words = query.lower().split()

    matched_topics = []

    for topic in topic_checkpoints:

        summary = topic["summary"].lower()

        if any(word in summary for word in query_words):

            matched_topics.append(topic)

    if matched_topics:

        for topic in matched_topics[:3]:

            st.write(
                f"Topic {topic['topic_id']}"
            )

            st.write(
                topic["summary"]
            )

            st.write("---")

    else:

        st.write(
            "No strongly relevant topics found."
        )

    st.subheader("Extracted Persona")

    st.json(persona)
