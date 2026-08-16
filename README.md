# AI Voicebot – Customer Payment Assistant

An AI-powered voicebot built to automate customer payment and collections conversations using voice AI, LLMs, and backend business tools.

## Tech Stack

* **Voice Platform:** Vapi
* **LLM:** GPT-4o-mini
* **Speech-to-Text:** Deepgram Nova-2
* **Text-to-Speech:** ElevenLabs
* **Backend:** Python, FastAPI
* **Testing:** Pytest
* **Version Control:** Git, GitHub

## Key Features

* Customer identity verification
* Outstanding payment assistance
* Payment-link generation
* Promise-to-pay capture
* Call disposition tracking
* Human-agent escalation
* Tool/function calling
* Verification-first privacy flow

## Architecture

```text
Customer
   ↓
Vapi Voice Agent
   ↓
Deepgram → GPT-4o-mini → ElevenLabs
   ↓
FastAPI Backend
   ↓
Business Tools
 ├── verify_customer
 ├── log_promise_to_pay
 ├── send_payment_link
 ├── mark_disposition
 └── escalate_to_agent
```

## Project Structure

```text
voicebot/
├── app/
│   ├── main.py
│   └── tools.py
├── tests/
│   └── test_tools.py
├── vapi/
│   ├── system_prompt.txt
│   └── tool_definitions.json
├── docs/
│   └── HLD.md
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Core Tools

### `verify_customer`

Verifies the customer's identity before account information is disclosed.

### `log_promise_to_pay`

Records the customer's committed payment date and amount.

### `send_payment_link`

Generates/sends a payment link for the outstanding amount.

### `mark_disposition`

Records the final outcome of the conversation.

### `escalate_to_agent`

Escalates the conversation to a human when required.

## Conversation Flow

```text
Call Starts
    ↓
Customer Verification
    ↓
Verified?
 ┌──┴──┐
No    Yes
↓      ↓
Retry  Discuss Payment
       ↓
 ┌─────┼──────────┐
Pay   Promise    Human Help
Now   to Pay       ↓
 ↓      ↓       Escalate
Payment PTP
Link   Logged
 └──────┼─────────┘
        ↓
Disposition
        ↓
   End Call
```

## Running Locally

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd voicebot

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## Environment Variables

Create a `.env` file:

```env
VAPI_API_KEY=your_vapi_api_key
OPENAI_API_KEY=your_openai_api_key
DEEPGRAM_API_KEY=your_deepgram_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

**Never commit API keys or `.env` to GitHub.**

## Testing

Run:

```bash
pytest
```

## Sample Test Customer

```text
Name: Rahul Sharma
Account ID: ACC-88392
Outstanding Amount: ₹8,499
Verification Code: 1234
```

## Security & Compliance

* Verify the customer before revealing account information.
* Store API keys in environment variables.
* Validate tool inputs.
* Escalate complex or sensitive cases to a human agent.
* Do not expose internal errors or sensitive information to customers.

## Future Improvements

* Real payment gateway integration
* Production database
* CRM integration
* Persistent conversation history
* Call monitoring and analytics
* Authentication and webhook security
* Production deployment and CI/CD

## Assignment Outcome

The project demonstrates an end-to-end **AI voice automation system** combining voice interaction, LLM reasoning, speech processing, FastAPI backend services, tool calling, payment workflows, verification, escalation, and automated testing.
