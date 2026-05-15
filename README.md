# Adaptive Conversational Memory System

## Project Overview

This project is a lightweight conversational memory system designed to process conversations chronologically, track persona evolution, classify intents offline, and resolve contradictory memories during retrieval.

The system combines:
- topic segmentation
- memory compression
- persona modeling
- persona drift tracking
- offline intent classification
- contradiction-aware retrieval

into a single scalable conversational architecture.

---

# Features

- Chronological conversation processing
- Topic segmentation
- Checkpoint-based memory compression
- Persona extraction
- Persona drift detection
- Offline intent classification
- Contradiction-aware retrieval
- Streamlit interface

---

# Architecture Flow

```text
Conversation Dataset
        ↓
Parser
        ↓
Chronological Processing
        ↓
Topic Segmentation
        ↓
Checkpoint Summaries
        ↓
Persona Extraction
        ↓
Persona Drift Detection
        ↓
Offline Intent Classification
        ↓
Conflict Resolution
        ↓
Streamlit Interface
