# Project 2: Crop Doctor (Swahili-First Agronomy Agent)

**Timeline**: Weeks 19-21 (Phase 4)  
**Complexity**: High  
**Target Users**: Kenyan smallholder farmers (2M+ households)

---

## Problem Statement

Kenyan smallholder farmers face:
- Limited access to agricultural extension officers (1 officer per 1000+ farmers)
- Language barriers (advice in English, farmers speak local languages)
- Delayed pest/disease diagnosis
- No personalized crop advice
- Weather information not actionable
- High input costs due to poor planning

**Impact**: 70% of Kenya's population relies on agriculture, but productivity is 30% below potential due to knowledge gaps.

---

## Solution: WhatsApp-Based AI Extension Officer

An agent accessible via WhatsApp that:
1. Provides farming advice in Swahili/English
2. Diagnoses crop diseases from photos
3. Gives weather-based planting recommendations
4. Answers farming questions 24/7
5. Connects to local input suppliers
6. Tracks farm activities and reminds farmers

---

## Technical Architecture

### Core Components

**1. WhatsApp Interface**
- Platform: Africa's Talking WhatsApp API
- Input: Text messages, photos, voice notes
- Output: Text, images, voice replies (TTS)
- Sessions: Track conversation context

**2. Agricultural Knowledge Base**
- Crop database (maize, beans, kale, tomatoes, potatoes, tea, coffee)
- Pest/disease database with images
- Fertilizer recommendations by crop/soil
- Planting calendars by region
- Market prices by county

**3. Multi-Agent System**

```python
Agents:
1. Router Agent: Determines user intent
2. Crop Advisor Agent: Planting, fertilizer, irrigation advice
3. Disease Diagnosis Agent: Analyzes crop photos
4. Weather Agent: Integrates with Kenya Met Dept API
5. Market Agent: Provides current prices
6. Reminder Agent: Schedules farming activities
```

**4. Language Handler**
- Input: Swahili or English (detect automatically)
- Output: Same language as input
- Handle Sheng (Swahili-English mix)

**5. Image Analysis**
- Vision API: Claude Vision or GPT-4V
- Compare against disease database
- Confidence scoring
- Treatment recommendations

---

## Key Features

### 1. Crop Disease Diagnosis

**Flow**:
```
Farmer: *sends photo of maize leaves*
Agent: "I can see brown spots on your maize leaves. This looks like 
        Maize Lethal Necrosis (MLN). How long have you noticed this?"
Farmer: "2 weeks"
Agent: "MLN spreads quickly. Here's what to do immediately:
        1. Uproot and burn infected plants
        2. Don't plant maize in that area for 2 seasons
        3. Use certified seeds next time
        
        Would you like suppliers for certified seeds near you?"
```

**Supported Diseases**:
- Maize: MLN, Fall Armyworm, Striga weed
- Beans: Bean rust, anthracnose
- Tomatoes: Late blight, early blight
- Potatoes: Late blight
- +20 more common diseases

### 2. Planting Calendar & Reminders

**Flow**:
```
Farmer: "When should I plant maize in Nakuru?"
Agent: "In Nakuru, plant maize during long rains (March-May) or 
        short rains (Oct-Nov). Next ideal window: March 15-30.
        
        Shall I remind you 1 week before and send prep checklist?"
Farmer: "Yes"
Agent: *Sets reminder for March 8*

[On March 8]
Agent: "Good morning! Maize planting starts in 1 week. 
        Checklist:
        ✓ Test soil pH
        ✓ Buy certified H614 seeds (2kg per acre)
        ✓ Get DAP fertilizer (50kg per acre)
        ✓ Prepare land (plow and harrow)
        
        Reply 'done' after each task."
```

### 3. Weather-Based Advice

**Integration**: Kenya Met Department API + local weather stations

**Flow**:
```
Agent: *Morning broadcast*
"Good morning farmers in Kiambu! 
🌧️ Heavy rain expected today-tomorrow.
📋 Recommended actions:
- Don't spray pesticides (rain will wash off)
- Delay fertilizer application
- Harvest ready vegetables before rains
- Check drainage in fields

Stay safe!"
```

### 4. Market Information

**Data Sources**:
- Ministry of Agriculture market prices
- RATIN (Regional Agricultural Trade Intelligence Network)
- Local market surveys

**Flow**:
```
Farmer: "Tomato price today?"
Agent: "Tomato prices (per kg):
        🏪 Wakulima Market: KES 40-60
        🏪 Gikomba Market: KES 35-55
        🏪 Kangemi Market: KES 38-58
        
        Prices up 20% from last week due to low supply.
        
        💡 Tip: If you have tomatoes ready, sell this week!"
```

### 5. Personalized Farm Management

**Farm Profile**:
- Farm size
- Crops grown
- Location/county
- Soil type
- Water source

**Activity Tracking**:
```
Farmer: "I planted tomatoes today"
Agent: "Great! Recorded tomato planting. 
        
        Upcoming tasks:
        ➜ Week 2: First weeding
        ➜ Week 3: Apply fertilizer (CAN 50kg/acre)
        ➜ Week 4: Start staking
        ➜ Week 10: First harvest expected
        
        I'll remind you for each task."
```

---

## Swahili Language Support

### Example Conversations

**Pest Diagnosis**:
```
Mkulima: *Anatuma picha ya mahindi yenye madoa*
Wakala: "Naona madoa ya kahawia kwenye majani ya mahindi yako. 
         Hii inaonekana ni Maize Lethal Necrosis (MLN). 
         Umeiangalia kwa muda gani?"
Mkulima: "Wiki mbili"
Wakala: "MLN inasambaa haraka. Fanya hivi mara moja:
         1. Ng'oa na choma mimea iliyoathirika
         2. Usipande mahindi pale kwa miaka 2
         3. Tumia mbegu za kuhakikishwa mara ijayo
         
         Ungependa wauzaji wa mbegu bora karibu nawe?"
```

**Weather Alert**:
```
Wakala: "Habari za asubuhi wakulima wa Kiambu!
🌧️ Mvua kubwa inatarajiwa leo na kesho.
📋 Fanya hivi:
- Usinyunyize dawa (mvua itaosha)
- Subiri kuongeza mbolea
- Vuna mboga zilizo tayari kabla ya mvua
- Angalia mifereji shambani

Kuweni salama!"
```

---

## Data Schema

### User Profile
```json
{
  "phone": "+254712345678",
  "name": "John Mwangi",
  "language": "swahili",
  "location": {
    "county": "Kiambu",
    "subcounty": "Kikuyu"
  },
  "farm": {
    "size_acres": 2,
    "soil_type": "clay loam",
    "water_source": "rain-fed",
    "crops": ["maize", "beans", "kale"]
  },
  "created": "2026-03-20"
}
```

### Activity Log
```json
{
  "user_phone": "+254712345678",
  "activity_type": "planting",
  "crop": "maize",
  "date": "2026-03-15",
  "area_acres": 1.5,
  "variety": "H614",
  "reminders": [
    {"task": "first_weeding", "date": "2026-03-29"},
    {"task": "fertilizer_top_dressing", "date": "2026-04-05"},
    {"task": "harvest", "date": "2026-07-15"}
  ]
}
```

---

## Implementation Roadmap

### Week 19: Core Agent + Knowledge Base
- [ ] Set up WhatsApp API (Africa's Talking)
- [ ] Build agricultural knowledge base
- [ ] Create router agent
- [ ] Implement crop advisor agent
- [ ] Test Swahili language support
- [ ] Build session management

### Week 20: Vision & Weather Integration
- [ ] Integrate Claude Vision for disease diagnosis
- [ ] Build disease database with images
- [ ] Connect Kenya Met Dept API
- [ ] Build weather advice generator
- [ ] Test with 20 crop disease photos

### Week 21: Market Data & Reminders
- [ ] Integrate market price APIs
- [ ] Build reminder system
- [ ] Create broadcast messaging
- [ ] Build farm profile system
- [ ] User testing with 10 farmers
- [ ] Documentation + demo

---

## Testing Strategy

### Beta Testing
- Recruit 20 smallholder farmers:
  - 10 in Central Kenya (Kiambu, Murang'a)
  - 5 in Rift Valley (Nakuru, Uasin Gishu)
  - 5 in Western (Kakamega, Bungoma)
- Mix of crops: maize, beans, vegetables, tea
- Run for 2 weeks
- Collect feedback via WhatsApp surveys

### Success Metrics
- Response time <5 seconds for text, <15 seconds for images
- Disease diagnosis accuracy >80%
- User satisfaction >4/5 stars
- Advice actionability: >70% of farmers implement recommendations

---

## Business Model

### Freemium Model
**Free Tier**:
- 10 questions/month
- Basic crop advice
- Weather alerts
- Disease diagnosis (2/month)

**Premium (KES 200/month = ~$1.50)**:
- Unlimited questions
- Priority responses
- Personalized reminders
- Market price alerts
- Voice support
- Direct expert escalation

### Partnerships
1. **Input Suppliers**: Commission on fertilizer/seed sales
2. **Insurance Companies**: Data for weather-based crop insurance
3. **Government**: Funded access for specific regions
4. **NGOs**: Subsidized access for beneficiaries

### Revenue Goal
- 1000 free users by Month 3
- 100 premium users by Month 6
- Revenue: KES 20,000/month (~$150)

---

## Tech Stack

- **Messaging**: Africa's Talking WhatsApp API
- **Agent**: Anthropic Claude (Haiku for cost, Sonnet for vision)
- **Knowledge Base**: Vector DB (Pinecone free tier / FAISS)
- **Weather**: Kenya Met Dept API
- **Market Data**: Ministry of Agriculture API
- **Database**: PostgreSQL (Supabase free tier)
- **Backend**: Python + FastAPI
- **Deployment**: Railway / Fly.io
- **Monitoring**: Helicone + CloudWatch

---

## Challenges & Solutions

**Challenge 1: WhatsApp API Cost**
- Solution: Use Africa's Talking ($0.01 per message), cheaper than Twilio

**Challenge 2: Vision API Cost**
- Solution: Use Claude Haiku for simple diagnoses, Sonnet only when needed

**Challenge 3: Offline Farmers**
- Solution: USSD fallback option (works on feature phones)

**Challenge 4: Low Phone Literacy**
- Solution: Voice notes + text-to-speech responses

**Challenge 5: Unreliable Internet**
- Solution: Async messaging, works well on 2G

---

## Impact Potential

**Quantifiable Impact**:
- 1000 farmers using = 2000+ acres better managed
- 20% yield improvement = 400 extra tons of produce/year
- 15% input cost savings = KES 6M saved/year
- Earlier disease detection = 30% loss prevention

**Social Impact**:
- Information in local languages
- 24/7 access (vs occasional extension officer visits)
- Women farmers empowered (access from home)
- Youth engagement (modern interface)

---

## Before AGI Content Angle

**Article Title**: "How AI Can Solve Kenya's Agricultural Extension Gap"

**Story Arc**:
1. Meet Mary, smallholder farmer in Kiambu
2. Her maize is dying, extension officer is 50km away
3. She WhatsApps the AI agent, sends photo
4. Gets instant diagnosis + treatment in Swahili
5. Saves crop, increases yield 30%
6. Broader implications for 2M+ Kenyan farmers

**YouTube Video**: "I Built an AI Farming Assistant for Kenya"
- Show WhatsApp demo
- Interview with beta testers
- Impact data visualization

---

**Related Projects**:
- [[Project-1-Kenyan-Hiring-Agent]]
- [[Project-3-MPesa-SME-Accounting-Agent]]

**Prerequisites**:
- Complete [[Phase-3-Production]] (reliability is critical)
- Test vision capabilities in Phase 2
- Practice Swahili prompts throughout
