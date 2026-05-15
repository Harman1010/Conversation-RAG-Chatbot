Adaptive Conversational Memory System

Features


Chronological conversation processing
Topic segmentation
Checkpoint-based memory compression
Persona extraction
Persona drift detection
Offline intent classification
Contradiction-aware retrieval
Streamlit interface


Tech Stack
Python
Streamlit
Scikit-learn
Pandas
VADER Sentiment
Sentence Transformers


How Topic Detection Works

The system processes messages chronologically and compares semantic similarity between conversation windows.

When similarity falls below a threshold, a new topic checkpoint is created.

How Persona Is Built

Persona is extracted using:

keyword analysis
communication patterns
message statistics
sentiment behavior

The system stores:

interests
communication style
emoji usage
message length
How Persona Drift Works

Instead of using one static persona, the system tracks mood and tone changes across multiple days.

The drift detector uses:

sentiment analysis
punctuation patterns
question frequency
topic triggers
How Retrieval Works

The retrieval system uses checkpoint summaries instead of raw conversation history.

The conflict resolver ranks retrieved chunks using:

semantic similarity
recency
emotional weight

It also flags contradictory memories.

Offline Intent Classifier

The intent classifier uses:

TF-IDF vectorization
Logistic Regression

This keeps the model:

lightweight
CPU friendly
fully offline
low latency
