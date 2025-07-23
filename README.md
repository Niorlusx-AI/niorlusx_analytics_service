# Niorlusx AI Call Service

This repository contains a blueprint for running an AI-powered voice service using a premium-rate phone number. It covers carrier aggregator setup, SIP domain configuration, real-time call metrics, and deployment basics.

## Carrier Aggregator Integration

1. **Choose your aggregator** (e.g., mVoice, Red Telecom, Boku).
2. Apply as a premium service provider and submit business details.
3. Once approved, you receive a premium-rate number (e.g., `190x`).
4. Configure payout bank details for Australian transfers.

```python
print("[DEBUG] Selected aggregator and started registration.")
print("[DEBUG] Configuring premium-rate number and SIP trunk.")
print("[DEBUG] Pricing announcement setup step.")
```

Pricing disclosure must be played to callers, for example `$4.95 per minute`.

## SIP Step-by-Step Cheat Sheet

1. In the Twilio Console, create a SIP domain named `niorlusx-voice-service`.
2. Set up authentication with an IP ACL or `niorlusx_sip` username and password.
3. Point the Voice URL to `https://your-server-domain/voice`.
4. Configure inbound calls to connect to your AI backend.

```python
print("[DEBUG] Starting SIP domain setup in Twilio.")
print("[DEBUG] SIP domain configured with authentication.")
```

## Real-Time Call Metrics Tracking

Basic logging is handled in `app.py`:

```python
from datetime import datetime

@app.post("/voice", response_class=PlainTextResponse)
async def voice_reply(SpeechResult: str = Form(None)):
    print(f"[DEBUG] Received SpeechResult: {SpeechResult}")
    log_entry = f"[{datetime.utcnow()}] Incoming text: {SpeechResult}"
    with open("call_logs.txt", "a") as log_file:
        log_file.write(log_entry + "\n")
    # additional AI logic here
```

A future dashboard could use Grafana or a web UI to display metrics.

```python
print("[DEBUG] Metrics dashboard placeholder added.")
```

## Repository Structure

```
app.py
requirements.txt
.env.example
start.sh
README.md
twiml.xml
Dockerfile
.github/workflows/deploy.yml
(call_logs.txt created at runtime)
```

## Development and Deployment

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the server locally:
   ```bash
   bash start.sh
   ```
3. Push code to GitHub:
   ```bash
   git add .
   git commit -m "Add carrier aggregator docs, SIP cheat sheet, metrics tracking"
   git push origin main
   ```

```python
print("[DEBUG] Preparing to push code to GitHub.")
```

## Demo Setup

1. Start the local server with `bash start.sh` or `uvicorn app:app --host 0.0.0.0 --port 8000`.
2. Connect Twilio SIP to `https://your-server-domain/voice`.
3. Dial the premium number from a phone and interact with the AI.
4. Logs appear in `call_logs.txt`.

```python
print("[DEBUG] Starting local server and connecting SIP.")
```

## Next Add-ons

- SMS fallback or dual-mode billing.
- Automated refunds or compliance scripts.
- Memory storage per caller (user profile).

```python
print("[DEBUG] Next add-ons listed for future implementation.")
```
