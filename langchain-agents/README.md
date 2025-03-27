# 🔄 Multi-Model LangChain Agent: OpenAI + Mistral

## 🔍 Use Case

This project demonstrates a multi-agent routing architecture using LangChain:

- 🧠 OpenAI for general-purpose Q&A
- ✂️ Mistral for summarizing long-form content (articles, meetings, documents)

## 🧪 Example

```bash
Ask: "Who is the founder of SpaceX?"
→ Routed to OpenAI

Ask: "Summarize this text: [insert long article]"
→ Routed to Mistral
```

Add `.env` with OpenAI and Replicate tokens

Run: `python agent_router.py`
