# Accounts Setup Checklist

Set up these accounts in order. Most are free, some have free tiers.

---

## Essential Accounts (Week 1)

### 1. GitHub
- **URL**: https://github.com/signup
- **Purpose**: Code hosting, portfolio, version control
- **Username suggestion**: `ianochieng-ai` or similar
- **Cost**: Free
- **What to do**: 
  - Create account
  - Set up profile with bio mentioning AI agents + Africa
  - Create repository: `african-ai-agents`
  - Star relevant repos: LangChain, Anthropic SDK

### 2. Anthropic Console
- **URL**: https://console.anthropic.com
- **Purpose**: Claude API access (primary LLM)
- **Cost**: $5 free credit, then pay-as-you-go (~$0.003 per 1K tokens for Haiku)
- **What to do**:
  - Sign up
  - Generate API key
  - Store in password manager (NOT in code)
  - Set budget alerts at $5, $10, $20

### 3. OpenAI Platform
- **URL**: https://platform.openai.com/signup
- **Purpose**: GPT API access (comparison/fallback)
- **Cost**: $5 free credit on new accounts
- **What to do**:
  - Create account
  - Generate API key
  - Keep as backup option

---

## Development Tools (Week 1-2)

### 4. Replit
- **URL**: https://replit.com/signup
- **Purpose**: Cloud-based Python environment, prototyping
- **Cost**: Free tier sufficient for learning
- **What to do**:
  - Create account
  - Set up Python template
  - Practice running code in browser

### 5. Google Colab
- **URL**: https://colab.research.google.com
- **Purpose**: Jupyter notebooks, experiments
- **Cost**: Free (uses Google account)
- **What to do**:
  - Sign in with Google
  - Create first notebook: "AI Agent Experiments"

### 6. Vercel
- **URL**: https://vercel.com/signup
- **Purpose**: Deploy web-based agents, free hosting
- **Cost**: Free tier (good for portfolio projects)
- **What to do**:
  - Sign up
  - Connect GitHub account
  - Deploy a test project

---

## Monitoring & Analytics (Week 4-6)

### 7. LangSmith (LangChain)
- **URL**: https://smith.langchain.com
- **Purpose**: Debug and monitor agent runs
- **Cost**: Free tier: 5K traces/month
- **What to do**:
  - Sign up
  - Get API key
  - Will use in Phase 2

### 8. Helicone
- **URL**: https://www.helicone.ai
- **Purpose**: LLM usage tracking and costs
- **Cost**: Free tier: 100K requests/month
- **What to do**:
  - Create account
  - Set up proxy for API calls
  - Monitor spend

---

## Learning Platforms (Week 1)

### 9. DeepLearning.AI
- **URL**: https://www.deeplearning.ai
- **Purpose**: Free AI courses
- **Cost**: Free courses available
- **What to do**:
  - Create account
  - Enroll in "LangChain for LLM Application Development"
  - Enroll in "Building Systems with the ChatGPT API"

### 10. YouTube Channels (Subscribe)
- **LangChain**: https://www.youtube.com/@LangChain
- **AI Jason**: https://www.youtube.com/@AIJason
- **Sam Witteveen**: https://www.youtube.com/@samwitteveenai
- **Purpose**: Free tutorials, updates

---

## Community & Support (Week 2-3)

### 11. Discord - LangChain
- **URL**: https://discord.gg/langchain
- **Purpose**: Ask questions, get help
- **Cost**: Free

### 12. Discord - Anthropic Developers
- **URL**: Via Anthropic Console
- **Purpose**: Claude API support
- **Cost**: Free

### 13. Twitter/X Developer Account
- **URL**: https://twitter.com/signup
- **Purpose**: Follow AI agent developers, share work
- **Accounts to follow**: 
  - @LangChainAI
  - @AnthropicAI
  - @hwchase17 (LangChain founder)
  - @swyx (AI engineer)

---

## African Context Tools (Week 3-4)

### 14. M-Pesa Developer Portal (Safaricom)
- **URL**: https://developer.safaricom.co.ke
- **Purpose**: M-Pesa API for Project 3
- **Cost**: Free sandbox
- **What to do**:
  - Create account
  - Generate sandbox credentials
  - Test Daraja API

### 15. Africa's Talking
- **URL**: https://account.africastalking.com/auth/register
- **Purpose**: SMS/WhatsApp APIs for agricultural agent
- **Cost**: Free sandbox + small credit
- **What to do**:
  - Sign up
  - Get API credentials
  - Test SMS sending

---

## Documentation & Writing (Week 1)

### 16. Notion or Obsidian Publish
- **Obsidian Publish**: https://obsidian.md/publish (paid)
- **Alternative**: Use GitHub Pages (free)
- **Purpose**: Publish Before AGI articles alongside Substack
- **Cost**: Free via GitHub Pages

---

## Account Security Setup

**Critical**: Set up password manager first
- **Bitwarden** (free): https://bitwarden.com
- Store all API keys here
- Never commit keys to GitHub
- Use environment variables in code

---

## Setup Checklist

Week 1:
- [ ] GitHub account created
- [ ] Anthropic Console account + API key
- [ ] OpenAI account + API key
- [ ] Replit account
- [ ] Password manager set up
- [ ] DeepLearning.AI account

Week 2:
- [ ] Google Colab tested
- [ ] Vercel account created
- [ ] Discord communities joined
- [ ] Twitter following AI accounts

Week 3:
- [ ] M-Pesa Developer account
- [ ] Africa's Talking account
- [ ] LangSmith account

Week 4:
- [ ] Helicone monitoring set up
- [ ] All API keys organized in password manager
- [ ] Test API calls working

---

## API Key Storage Template

Create `.env` file (never commit):
```
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
LANGCHAIN_API_KEY=ls-...
MPESA_CONSUMER_KEY=...
MPESA_CONSUMER_SECRET=...
AFRICAS_TALKING_API_KEY=...
```

---

**Next**: Once accounts are set up → [[Phase-1-Foundation]]
