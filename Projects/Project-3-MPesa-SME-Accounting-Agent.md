# Project 3: M-Pesa SME Accounting Agent

**Timeline**: Weeks 22-24 (Phase 4)  
**Complexity**: Medium  
**Target Users**: Kenyan small businesses, freelancers, sole traders

---

## Problem Statement

Kenyan SMEs using M-Pesa face:
- Manual reconciliation of hundreds of transactions
- No automated invoicing
- Payment tracking in WhatsApp/SMS/Excel chaos
- Tax compliance nightmares (no organized records)
- Cash flow blindness (don't know who owes what)
- Time waste: 5-10 hours/week on bookkeeping

**Market Size**: 1.5M+ registered MSMEs in Kenya, 80%+ use M-Pesa as primary payment method.

---

## Solution: AI-Powered M-Pesa Business Automation

An agent that:
1. Connects to M-Pesa via Safaricom Daraja API
2. Auto-categorizes transactions (sales, expenses, transfers)
3. Matches payments to invoices
4. Generates invoices automatically
5. Tracks outstanding payments
6. Produces tax-ready reports
7. Sends payment reminders

---

## Technical Architecture

### Core Components

**1. M-Pesa Integration**
- Daraja API (Safaricom's M-Pesa API)
- Pull transaction statements
- Handle callbacks for real-time payments
- B2C for refunds/payouts

**2. Transaction Classifier Agent**
```python
Tools:
- categorize_transaction(description, amount, counterparty)
  # Returns: "income", "expense", "transfer", "refund"
- identify_customer(phone_number, transaction_desc)
  # Matches to customer database
- extract_invoice_reference(sms_text)
  # Pulls invoice numbers from payment SMS
```

**3. Invoice Generator Agent**
```python
Tools:
- create_invoice(customer, items, amount)
- send_invoice(invoice_id, phone_number) # Via SMS/Email
- record_payment(invoice_id, mpesa_code)
```

**4. Reconciliation Agent**
```python
Tools:
- match_payment_to_invoice(mpesa_transaction)
- identify_unmatched_payments()
- suggest_matches(similar_amounts, dates)
```

**5. Reminder Agent**
```python
Tools:
- check_overdue_invoices()
- send_reminder(customer, invoice_id, days_overdue)
- escalate_reminder(days_overdue > 30)
```

**6. Reporting Agent**
```python
Tools:
- generate_cashflow_report(start_date, end_date)
- generate_tax_summary(period) # iTax-ready
- generate_profit_loss_statement()
```

---

## Key Features

### 1. Automatic Transaction Categorization

**Flow**:
```
M-Pesa SMS: "RKL3X9V2GH Confirmed. You have received 
             Ksh 5,000.00 from JOHN KAMAU 0712345678"
             
Agent: *Analyzes transaction*
- Amount: 5000
- From: John Kamau (0712345678)
- Type: Income
- Checks customer DB: John Kamau = existing customer
- Checks open invoices: Invoice #INV-089 = 5000
- Action: Mark invoice paid, update cashflow

User gets notification:
"✅ Payment received: KES 5,000 from John Kamau
   Invoice #INV-089 marked as PAID
   Outstanding balance: KES 0"
```

**Smart Categorization**:
- Income: Payments from customers (matches invoice amounts)
- Expense: Payments to suppliers, utilities, stock
- Transfer: Internal transfers between accounts
- Refund: Returns to customers
- Tax: KRA payments, VAT

### 2. Instant Invoice Generation

**Flow**:
```
User (via WhatsApp): "Create invoice for Jane Wanjiru 
                      - 10 bags cement @ 850 each"
                      
Agent: *Generates invoice*
Invoice #INV-090
To: Jane Wanjiru (0722334455)
Items:
- Cement (50kg bag) × 10 @ KES 850 = KES 8,500
Subtotal: KES 8,500
VAT (16%): KES 1,360
Total: KES 9,860

Pay to Till: 123456
M-Pesa: 0712345678 (JOHN'S HARDWARE)

User: "Send it"
Agent: *Sends via SMS*
"Hi Jane, your invoice #INV-090 for KES 9,860 is ready.
 Items: Cement × 10. Pay to Till 123456 or 0712345678.
 Due: 7 days. Reply PAID when done. - John's Hardware"
```

### 3. Smart Payment Matching

**Scenario**: Customer sends KES 9,860 with reference "INV-090"

```
Agent: 
1. Receives M-Pesa confirmation
2. Extracts amount (9,860) and reference (INV-090)
3. Finds matching invoice
4. Verifies amount matches
5. Marks invoice as PAID
6. Notifies user + customer

Notification to User:
"✅ Invoice #INV-090 paid by Jane Wanjiru
   Amount: KES 9,860
   Outstanding invoices: 3 (KES 34,500 total)"
   
Notification to Customer:
"Thank you Jane! Payment received for Invoice #INV-090.
 Your account is up to date. - John's Hardware"
```

**Partial Payments**:
```
Customer pays KES 5,000 of KES 9,860 invoice

Agent:
"Partial payment received: KES 5,000 / 9,860
 Remaining balance: KES 4,860
 Want to send reminder for balance? (yes/no)"
```

### 4. Automated Payment Reminders

**3-Tier Reminder System**:

**Day 7 (Due Date)**:
```
"Hi Jane, gentle reminder: Invoice #INV-090 (KES 9,860) 
 is due today. Pay to Till 123456 or 0712345678.
 Thanks! - John's Hardware"
```

**Day 14 (1 week overdue)**:
```
"Hi Jane, Invoice #INV-090 (KES 9,860) is now 7 days 
 overdue. Please settle by end of week to avoid 
 late fees. Need payment plan? Reply YES. 
 - John's Hardware"
```

**Day 30 (1 month overdue)**:
```
"FINAL NOTICE: Invoice #INV-090 (KES 9,860) is 30 days 
 overdue. Late fee of KES 1,000 now applies. 
 Total due: KES 10,860. Settle within 3 days.
 - John's Hardware"
```

### 5. Cash Flow Dashboard

**Daily WhatsApp Report** (Morning 8am):
```
Good morning! Here's your business summary:

💰 CASH FLOW (Yesterday)
Income: KES 45,000 (8 transactions)
Expenses: KES 12,500 (3 transactions)
Net: +KES 32,500

📊 OUTSTANDING
Invoices due: 5 (KES 67,000)
Overdue: 2 (KES 15,000)

🔔 ACTION NEEDED
- Send reminder to John Doe (14 days overdue)
- Stock low: Cement (5 bags left)

Reply '1' for detailed report
Reply '2' for today's invoices
```

### 6. Tax Compliance (iTax Integration)

**Monthly Tax Report**:
```
TAX SUMMARY - March 2026

Sales: KES 450,000
VAT Collected: KES 72,000
Expenses: KES 180,000
VAT Paid: KES 28,800

VAT Payable: KES 43,200 (due April 20)
Withholding Tax: KES 5,000

📄 iTax CSV ready for upload
📧 Email report? (yes/no)
```

---

## User Personas

### 1. Hardware Shop Owner (John)
- 50 transactions/day
- 10 regular suppliers, 100+ customers
- Accepts M-Pesa + Cash
- Pain: Manual reconciliation takes 2 hours/day

**Agent Value**:
- Auto-match 90% of payments
- Flag discrepancies
- Generate supplier payment schedule

### 2. Freelance Graphic Designer (Mary)
- 15 clients/month
- KES 5,000 - 50,000 per project
- Pain: Chasing payments, forgetting who paid

**Agent Value**:
- Auto-invoice on project completion
- Payment reminders
- Income tracking for taxes

### 3. Salon Owner (Grace)
- 30-40 customers/day
- Mix of services (haircut, styling, nails)
- Pain: Difficult to track daily income

**Agent Value**:
- Categorize by service type
- Daily revenue reports
- Identify best-selling services

---

## Data Schema

### Customer Database
```json
{
  "customer_id": "CUST-001",
  "name": "Jane Wanjiru",
  "phone": "+254722334455",
  "email": "jane@example.com",
  "total_invoiced": 45000,
  "total_paid": 40000,
  "outstanding": 5000,
  "credit_limit": 10000,
  "payment_terms": 7, // days
  "last_payment": "2026-03-15",
  "status": "good" // good/warning/blocked
}
```

### Invoice
```json
{
  "invoice_id": "INV-090",
  "customer_id": "CUST-001",
  "date_issued": "2026-03-10",
  "due_date": "2026-03-17",
  "items": [
    {
      "description": "Cement 50kg",
      "quantity": 10,
      "unit_price": 850,
      "total": 8500
    }
  ],
  "subtotal": 8500,
  "vat": 1360,
  "total": 9860,
  "amount_paid": 5000,
  "balance": 4860,
  "status": "partial", // unpaid/partial/paid/overdue
  "payment_history": [
    {
      "date": "2026-03-12",
      "amount": 5000,
      "mpesa_code": "RKL3X9V2GH",
      "method": "mpesa"
    }
  ]
}
```

### Transaction
```json
{
  "transaction_id": "TXN-12345",
  "mpesa_code": "RKL3X9V2GH",
  "date": "2026-03-12T14:30:00",
  "type": "income", // income/expense/transfer
  "category": "sales", // sales/supplies/utilities/etc
  "amount": 5000,
  "counterparty_name": "Jane Wanjiru",
  "counterparty_phone": "+254722334455",
  "linked_invoice": "INV-090",
  "description": "Payment for cement",
  "reconciled": true
}
```

---

## Implementation Roadmap

### Week 22: M-Pesa Integration + Core Agent
- [ ] Set up Daraja API (sandbox then production)
- [ ] Build transaction fetching service
- [ ] Create transaction classifier agent
- [ ] Build customer database
- [ ] Test with 100 real M-Pesa transactions

### Week 23: Invoicing + Matching
- [ ] Build invoice generator
- [ ] Create payment matching logic
- [ ] Implement SMS sending (Africa's Talking)
- [ ] Build reconciliation dashboard
- [ ] Test with real business (hardware shop)

### Week 24: Reminders + Reporting
- [ ] Build reminder agent
- [ ] Create cash flow reporting
- [ ] Generate tax reports (iTax format)
- [ ] WhatsApp bot interface
- [ ] User testing with 5 businesses
- [ ] Documentation + demo

---

## Tech Stack

- **M-Pesa API**: Safaricom Daraja API
- **SMS**: Africa's Talking
- **Agent**: Anthropic Claude (Haiku for classification)
- **Database**: PostgreSQL (Supabase)
- **Backend**: Python + FastAPI
- **Frontend**: WhatsApp bot + web dashboard (Next.js)
- **PDF Generation**: ReportLab (invoices)
- **Deployment**: Railway / Fly.io
- **Monitoring**: Helicone + Sentry

---

## Business Model

### Subscription Pricing
**Free Tier**:
- 50 transactions/month
- 5 invoices/month
- Basic categorization

**Starter (KES 500/month = ~$4)**:
- 200 transactions/month
- Unlimited invoices
- Auto-matching
- Payment reminders

**Pro (KES 1,500/month = ~$12)**:
- Unlimited transactions
- Multiple business accounts
- Tax reports
- API access
- Priority support

**Enterprise (KES 5,000/month = ~$40)**:
- Multi-location
- Custom integrations
- Dedicated account manager
- Advanced analytics

### Target Market
- 1.5M MSMEs in Kenya
- Focus: Nairobi, Mombasa, Kisumu, Nakuru
- Verticals: Retail, services, wholesale

### Revenue Goal
- 100 free users by Month 2
- 50 paying users (Starter) by Month 4
- 10 Pro users by Month 6
- Monthly Revenue: KES 50,000 (~$400)

---

## Success Metrics

**Technical**:
- Transaction processing <2 seconds
- Matching accuracy >95%
- Uptime >99.5%
- Cost <KES 50 per user/month

**Product**:
- Time saved: 8 hours → 30 minutes/week
- Payment collection improved 20%+
- User NPS >50

---

## Challenges & Solutions

**Challenge 1: API Rate Limits**
- Solution: Queue system, batch requests, cache frequently accessed data

**Challenge 2: Data Security**
- Solution: End-to-end encryption, PCI-DSS compliance, regular audits

**Challenge 3: Internet Downtime**
- Solution: Offline-first mobile app, sync when online

**Challenge 4: User Onboarding**
- Solution: 5-minute guided setup, pre-fill common business types

---

## Before AGI Content Angle

**Article Title**: "How I Built M-Pesa Automation with AI"

**Story Arc**:
1. Meet John, hardware shop owner drowning in M-Pesa receipts
2. Show his pain: 2 hours/day reconciling, missed payments
3. Introduce the agent solution
4. Demo the automation (screenshots/video)
5. Results: 8 hours saved/week, 15% more revenue collected
6. Bigger picture: Automating Africa's informal economy

**YouTube Video**: "This AI Handles My M-Pesa Business"
- Screen recording of agent in action
- Interview with John (before/after)
- Live demo of invoice → payment → reconciliation

---

**Related Projects**:
- [[Project-1-Kenyan-Hiring-Agent]]
- [[Project-2-Crop-Doctor]]

**Prerequisites**:
- Complete [[Phase-3-Production]] (reliability is critical for money)
- M-Pesa developer account from Week 3
- Test with real transactions in sandbox
