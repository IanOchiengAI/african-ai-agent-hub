# Phase 1: Foundation (Weeks 1-8)

**Goal**: Master Python basics, understand LLM APIs, and build your first simple agent  
**Time**: 8 weeks  
**Hours/week**: 18-22 hours  
**Milestone**: Working chatbot that can call functions

---

## Week 1: Python Fundamentals + Environment Setup

### Learning Goals
- Python syntax, variables, functions
- Lists, dictionaries, loops
- API requests basics
- Environment variables

### Free Resources
1. **CS50's Introduction to Programming with Python** (Harvard)
   - URL: https://cs50.harvard.edu/python/2022/
   - Watch: Weeks 0-4
   - Do: Problem sets 0-4
   - Time: ~12 hours

2. **Python Requests Library**
   - URL: https://requests.readthedocs.io/en/latest/
   - Read: Quickstart guide
   - Time: 2 hours

### Hands-On Projects
- [ ] Set up Python environment (local + Replit)
- [ ] Write a script that fetches weather data from an API
- [ ] Build a simple CLI calculator
- [ ] Make your first API request to Anthropic

### Code Challenge
```python
# Create a function that takes a question and sends it to Claude API
# Save the response to a file
# Run it 5 times with different questions
```

### Deliverable
- `week-1-python-basics` folder in GitHub repo
- Working API request script
- Screenshot of successful Claude API call

---

## Week 2: Prompt Engineering Basics

### Learning Goals
- How LLMs process prompts
- System vs user messages
- Temperature, tokens, stop sequences
- XML tags for structured prompts

### Free Resources
1. **Anthropic Prompt Engineering Guide**
   - URL: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
   - Read entire guide
   - Time: 4 hours

2. **OpenAI Prompt Engineering Guide**
   - URL: https://platform.openai.com/docs/guides/prompt-engineering
   - Compare approaches
   - Time: 2 hours

3. **Prompt Engineering Course (DeepLearning.AI)**
   - URL: https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/
   - Complete all lessons
   - Time: 6 hours

### Hands-On Projects
- [ ] Build a prompt that extracts structured data from unstructured text
- [ ] Create a system prompt for a Kenyan job CV screener
- [ ] Test temperature settings (0.0 vs 1.0) and document differences
- [ ] Build a multi-turn conversation handler

### Code Challenge
```python
# Build a script that:
# 1. Takes a Kenyan CV (text)
# 2. Uses Claude to extract: name, education system (8-4-4/CBC), 
#    experience years, skills
# 3. Returns JSON format
# 4. Handle errors gracefully
```

### Deliverable
- `week-2-prompt-engineering` folder
- CV extraction script with 5 test CVs
- Blog draft: "How I Taught Claude About Kenyan CVs"

---

## Week 3: Function Calling & Tool Use

### Learning Goals
- What is function/tool calling
- JSON schema definitions
- Parsing tool call responses
- Error handling

### Free Resources
1. **Anthropic Tool Use Guide**
   - URL: https://docs.anthropic.com/en/docs/build-with-claude/tool-use
   - Read entire section
   - Time: 3 hours

2. **Function Calling Tutorial (OpenAI)**
   - URL: https://platform.openai.com/docs/guides/function-calling
   - Compare with Anthropic
   - Time: 2 hours

3. **YouTube: "Function Calling Explained" by AI Jason**
   - Search and watch latest video
   - Time: 1 hour

### Hands-On Projects
- [ ] Create a calculator tool that Claude can use
- [ ] Build a weather lookup tool
- [ ] Create a database query tool (SQLite)
- [ ] Combine multiple tools in one conversation

### Code Challenge
```python
# Build an agent that can:
# 1. Check current M-Pesa rates (mock data)
# 2. Calculate currency conversion
# 3. Send SMS confirmation (Africa's Talking sandbox)
# All triggered by natural language: 
# "Convert 5000 KES to USD and SMS the result to +254..."
```

### Deliverable
- `week-3-function-calling` folder
- Multi-tool agent script
- Documentation of tool schemas

---

## Week 4: Agent Basics & ReAct Pattern

### Learning Goals
- What is an agent vs chatbot
- ReAct (Reasoning + Acting) pattern
- Agent loops and stopping conditions
- Logging and debugging

### Free Resources
1. **ReAct Paper (Simplified)**
   - URL: https://arxiv.org/abs/2210.03629
   - Read abstract + introduction
   - Time: 1 hour

2. **Building Your First Agent (Blog)**
   - Search: "build llm agent from scratch python"
   - Read 2-3 tutorials
   - Time: 3 hours

3. **YouTube: Agent Tutorials**
   - Sam Witteveen's agent series
   - Watch 3-4 videos
   - Time: 4 hours

### Hands-On Projects
- [ ] Build a simple ReAct agent from scratch (no frameworks)
- [ ] Add logging to track reasoning steps
- [ ] Create max iteration safety limit
- [ ] Build a research agent that can search and summarize

### Code Challenge
```python
# Build a Kenyan job market research agent:
# Tools: 
# - web_search(query) - mock with predefined results
# - extract_salary(job_posting) 
# - calculate_average(numbers)
# 
# Task: "What's the average salary for software engineers in Nairobi?"
# Agent should: search → extract → calculate → report
```

### Deliverable
- `week-4-react-agent` folder
- Job market research agent
- Log file showing reasoning steps
- Before AGI draft: "I Built My First AI Agent"

---

## Week 5: Working with Documents & Context

### Learning Goals
- Text splitting and chunking
- Embeddings basics
- Vector similarity search
- Building a simple RAG (Retrieval Augmented Generation)

### Free Resources
1. **Embeddings Guide (Anthropic)**
   - URL: https://docs.anthropic.com/en/docs/build-with-claude/embeddings
   - Read full guide
   - Time: 2 hours

2. **RAG Tutorial (DeepLearning.AI)**
   - Search for free RAG courses
   - Complete one full course
   - Time: 6 hours

3. **Chunking Strategies**
   - Read blog posts on text splitting
   - Time: 2 hours

### Hands-On Projects
- [ ] Split a long document into chunks
- [ ] Create embeddings using OpenAI/Cohere (free tier)
- [ ] Build a simple vector search with FAISS
- [ ] Create a Q&A system over documents

### Code Challenge
```python
# Build a Kenyan law Q&A system:
# 1. Load Kenya's Data Protection Act 2019 (PDF)
# 2. Split into chunks
# 3. Create embeddings
# 4. Build Q&A interface: ask questions, get relevant sections
# Example: "What are the penalties for data breach?"
```

### Deliverable
- `week-5-rag-system` folder
- Law Q&A system
- Comparison of different chunking strategies

---

## Week 6: Error Handling & Reliability

### Learning Goals
- Common LLM failure modes
- Retry logic and exponential backoff
- Rate limiting and quotas
- Fallback strategies
- Cost optimization

### Free Resources
1. **Production LLM Apps Guide**
   - Search: "production llm applications best practices"
   - Read 3-4 articles
   - Time: 4 hours

2. **Anthropic Rate Limits**
   - URL: https://docs.anthropic.com/en/api/rate-limits
   - Read and understand
   - Time: 1 hour

3. **Error Handling Patterns**
   - Python error handling tutorials
   - Time: 3 hours

### Hands-On Projects
- [ ] Implement retry logic with exponential backoff
- [ ] Build a rate limiter
- [ ] Create a cost tracking decorator
- [ ] Implement fallback from Claude to GPT

### Code Challenge
```python
# Enhance your CV screener from Week 2:
# 1. Add retry logic (3 attempts)
# 2. Implement rate limiting (10 requests/minute)
# 3. Track costs per CV processed
# 4. Fall back to cheaper model (Haiku) if Sonnet fails
# 5. Log all errors to file
```

### Deliverable
- `week-6-production-ready` folder
- Robust CV screener v2
- Cost analysis document

---

## Week 7: Async & Concurrency

### Learning Goals
- Python asyncio basics
- Parallel API calls
- Batch processing
- Managing concurrent agent runs

### Free Resources
1. **Python Asyncio Tutorial**
   - URL: https://realpython.com/async-io-python/
   - Read full guide
   - Time: 4 hours

2. **Anthropic Batch API**
   - URL: https://docs.anthropic.com/en/docs/build-with-claude/message-batches
   - Read documentation
   - Time: 2 hours

3. **YouTube: Async Python**
   - Search for recent tutorials
   - Watch 2-3 videos
   - Time: 3 hours

### Hands-On Projects
- [ ] Convert synchronous code to async
- [ ] Process 100 CVs concurrently
- [ ] Implement queue system
- [ ] Use Anthropic's Batch API

### Code Challenge
```python
# Build a batch CV processor:
# 1. Load 50 Kenyan CVs from folder
# 2. Process concurrently (max 10 at a time)
# 3. Extract skills, experience, education
# 4. Save results to database
# 5. Complete in under 2 minutes
```

### Deliverable
- `week-7-async-processing` folder
- Batch CV processor
- Performance benchmarks

---

## Week 8: Build Your First Complete Agent

### Learning Goals
- Integrate everything learned
- Build end-to-end system
- Documentation
- Deployment basics

### Project: Simple Kenyan Hiring Assistant

**Features**:
1. Accept CV upload (PDF/text)
2. Extract structured data
3. Match against job description
4. Score candidate fit (0-100)
5. Generate interview questions
6. Send SMS notification (sandbox)

**Tech Stack**:
- Python + Anthropic API
- Function calling for tools
- Error handling & retries
- Async processing
- Simple web interface (Gradio/Streamlit)

### Hands-On Projects
- [ ] Build complete hiring assistant
- [ ] Create web interface
- [ ] Deploy to Replit/Vercel
- [ ] Write documentation
- [ ] Record demo video

### Deliverable
- `week-8-hiring-assistant` folder
- Live demo link
- GitHub README with screenshots
- Before AGI article: "I Built My First AI Agent"
- YouTube video: Quick demo walkthrough

---

## Phase 1 Success Checklist

By end of Week 8, you should have:

**Technical Skills**:
- [ ] Comfortable with Python
- [ ] Can work with LLM APIs
- [ ] Understand prompt engineering
- [ ] Can build function calling systems
- [ ] Know error handling patterns
- [ ] Can deploy simple apps

**Portfolio**:
- [ ] 8 weekly projects on GitHub
- [ ] 1 complete agent deployed
- [ ] 1 Before AGI article published
- [ ] 1 demo video on YouTube

**Accounts & Setup**:
- [ ] All essential accounts created
- [ ] API keys working
- [ ] Development environment ready
- [ ] GitHub profile updated

---

## Estimated Costs (Phase 1)

- Anthropic API: ~$10-15 (including free credit)
- OpenAI API: $0 (using free credit)
- Hosting: $0 (free tiers)
- **Total: ~$10-15**

---

## Common Pitfalls to Avoid

1. **Tutorial hell**: Don't just watch videos - build projects
2. **Perfectionism**: Ship messy code, improve later
3. **Scope creep**: Stick to weekly goals
4. **No documentation**: Write as you build
5. **Ignoring costs**: Track API spend weekly

---

**Next Phase**: [[Phase-2-Frameworks]] (LangChain, production patterns)
