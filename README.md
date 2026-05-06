---
title: Conversation-RAG-Chatbot
sdk: streamlit
sdk_version: 1.35.0
app_file: app.py
---

# Conversation Persona Chatbot

This project is a Retrieval-Augmented Generation (RAG) based conversation analysis system built using conversation datasets.

The system processes conversations chronologically, detects topic changes, creates topic checkpoints with summaries, extracts persona information, and provides a chatbot interface for querying user behavior and conversation patterns.

---

# Features

- Chronological conversation processing
- Topic change detection
- Topic checkpoint summaries
- 100-message checkpoint summaries
- Persona extraction
- Streamlit chatbot interface
- JSON-based retrieval system
- Hugging Face deployment

---

# Project Workflow

Conversation CSV  
↓  
Message Parsing  
↓  
Topic Detection  
↓  
Topic Checkpoints  
↓  
Topic Summaries  
↓  
100 Message Checkpoints  
↓  
Persona Extraction  
↓  
JSON Storage  
↓  
Streamlit Chatbot  

---

# How Topic Changes Are Detected

The system processes conversations message-by-message in chronological order.

For every incoming message:
- A running topic context is created from recent messages
- Sentence embeddings are generated using all-MiniLM-L6-v2
- Cosine similarity is calculated between the current message and topic context
- Keyword overlap is also calculated

Final Topic Score:

0.7 × Semantic Similarity + 0.3 × Keyword Overlap

If the final score falls below a threshold, the system creates a new topic checkpoint.

This allows dynamic topic segmentation instead of treating the entire conversation as one topic.

---

# Topic Checkpoints

Each topic checkpoint stores:
- Topic ID
- Start message
- End message
- Topic summary
- Related messages

This helps preserve conversation memory in structured form.

---

# 100 Message Checkpoints

Apart from topic checkpoints, the system also creates summaries every 100 chronological messages.

These checkpoints help compress large conversations into manageable summaries for long-range memory retrieval.

---

# Summarization

The project uses transformer-based summarization using the BART model.

To avoid transformer token limitations:
- Large text blocks are truncated before summarization
- Smaller message groups are summarized independently

---

# How Persona Is Built

The system extracts persona information directly from conversation text.

The following attributes are extracted:
- Interests
- Communication style
- Emoji usage
- Average message length

Persona extraction is based on:
- Keyword detection
- Message statistics
- Conversation behavior patterns

The persona is stored in structured JSON format.

Example:

```json
{
    "interests": [
        "music",
        "fitness",
        "cooking"
    ],
    "communication_style": "medium messages",
    "emoji_style": "low emoji usage",
    "average_message_length": 11.16
}
```

---

# How Retrieval Works

The chatbot retrieves relevant information using stored topic summaries.

When a user enters a query:
- The query is converted into keywords
- Topic summaries are searched for matching keywords
- Relevant topic summaries are returned to the chatbot

The chatbot then combines:
- Retrieved topic summaries
- Extracted persona information

to answer user-related questions.

---

# Chatbot

The chatbot is built using Streamlit.

Users can ask questions such as:
- What are the user's interests?
- What kind of person is this user?
- What topics were discussed?
- How does the user communicate?

The chatbot displays:
- Relevant topic summaries
- Extracted persona information

---

# Technologies Used

- Python
- Streamlit
- Pandas
- Sentence Transformers
- Transformers
- Scikit-learn

---

# Project Files

- `main.py` → Main pipeline execution
- `app.py` → Streamlit chatbot
- `parser.py` → CSV parsing
- `checkpoint_manager.py` → Topic checkpoint logic
- `topic_detector.py` → Similarity calculations
- `summarizer.py` → Topic summarization
- `persona_extractor.py` → Persona extraction
- `save_outputs.py` → JSON output storage

---

# Output Files

- `topic_checkpoints.json`
- `hundred_message_checkpoints.json`
- `persona.json`

These files store processed conversation memory and extracted persona information.

---

# How To Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Main Pipeline

```bash
python -m main
```

## Run Streamlit Chatbot

```bash
streamlit run app.py
```

---

# Example Questions

- What are the user's interests?
- What kind of person is this user?
- Does the user like cooking?
- What topics were discussed?
- How does the user communicate?

---

# Deployment

The project is deployed using Hugging Face Spaces with Streamlit.

---

# Video Demo

Loom Link:

PASTE_YOUR_LOOM_LINK_HERE
