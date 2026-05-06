---
title: Conversation Persona Chatbot
sdk: streamlit
sdk_version: 1.35.0
app_file: app.py
---

# Conversation Persona Chatbot

This project is a Retrieval-Augmented Generation (RAG) based chatbot system built using conversation data.

The system processes conversations chronologically, detects topic changes, creates topic checkpoints with summaries, extracts user persona information, and allows users to ask questions through a Streamlit chatbot interface.

## Features

- Chronological conversation processing
- Topic change detection
- Topic checkpoint summaries
- 100-message checkpoint summaries
- Persona extraction
- Streamlit chatbot interface
- JSON-based retrieval system

---

# Project Workflow

Conversation CSV  
↓  
Message Parsing  
↓  
Topic Detection  
↓  
Topic Checkpoint Summaries  
↓  
100 Message Checkpoints  
↓  
Persona Extraction  
↓  
JSON Storage  
↓  
Streamlit Chatbot  

---

# Topic Change Detection

The project processes messages one-by-one in chronological order.

For each new message:
- Semantic similarity is calculated using sentence embeddings
- Keyword overlap is calculated
- Final topic score is generated

If the score falls below a threshold, a new topic checkpoint is created.

## Formula Used

Final Topic Score:

0.7 × Semantic Similarity + 0.3 × Keyword Overlap

---

# Persona Extraction

The system extracts:
- Interests
- Communication style
- Emoji usage
- Average message length

Persona extraction is based on actual conversation text.

---

# Retrieval System

The chatbot retrieves relevant topic summaries by matching query keywords with stored topic summaries.

The retrieved topics and extracted persona are displayed in the chatbot interface.

---

# Technologies Used

- Python
- Streamlit
- Sentence Transformers
- Transformers
- Pandas
- Scikit-learn

---

# How to Run

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run preprocessing pipeline

```bash
python -m main
```

## Run chatbot

```bash
streamlit run app.py
```

---

# Example Questions

- What are the user's interests?
- What kind of person is this user?
- What topics were discussed?
- Does the user like cooking?
- How does the user communicate?

---

# Files

- `main.py` → Main pipeline
- `app.py` → Streamlit chatbot
- `checkpoint_manager.py` → Topic checkpoint logic
- `persona_extractor.py` → Persona extraction
- `summarizer.py` → Topic summarization
- `parser.py` → CSV parsing
- `topic_detector.py` → Topic similarity calculations

---

# Output Files

- `topic_checkpoints.json`
- `hundred_message_checkpoints.json`
- `persona.json`

These files store processed conversation memory and persona information.
