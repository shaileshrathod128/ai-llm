## 📦 Examples Included

This repository contains two complete, production-ready LangChain demos to showcase different real-world use cases:

---

### 🔁 1. `rag-pipeline/` – Retrieval-Augmented Generation (RAG) Demo

Build an LLM-powered assistant that answers domain-specific questions by retrieving relevant content from your own knowledge base using:

- 🧠 LangChain
- 📚 FAISS vector search
- 🤖 OpenAI (or any LLM)

**Use Case:**

> “Ask questions over your company policies, PDF docs, or knowledge base with factual, grounded answers.”

📂 [View `rag-pipeline`](./rag-pipeline)

---

### 🤖 2. `langchain-agents/` – Multi-Model LangChain Agent

Create an AI assistant that dynamically chooses between models based on the type of user query:

- 🔍 General Q&A → OpenAI
- 📝 Summarization → Mistral (via Replicate)

**Use Case:**

> “Automatically route summarization tasks to Mistral and general questions to OpenAI.”

📂 [View `langchain-agents`](./langchain-agents)

---

Both demos follow best practices, support `.env` secrets, and are great starting points for real-world GenAI applications.
