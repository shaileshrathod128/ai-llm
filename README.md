# 🔍 RAG Pipeline Demo using LangChain, FAISS & OpenAI

This is a hands-on Retrieval-Augmented Generation (RAG) pipeline built using:

- LangChain
- FAISS for vector search
- OpenAI for LLM

## 💡 What It Does

Loads text files, splits them into chunks, creates vector embeddings, and allows you to query them using an LLM. Great for building AI assistants on top of your own knowledge base.

## 🚀 Quick Start

1. **Install dependencies**

```bash
pip install -r app/requirements.txt
```

2. **Add your .txt files to app/docs/**

3. **Run Python script**

```bash
python app/rag_pipeline.py
```
