from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse
from datetime import datetime

app = FastAPI()

@app.post("/voice", response_class=PlainTextResponse)
async def voice_reply(SpeechResult: str = Form(None)):
    print(f"[DEBUG] Received SpeechResult: {SpeechResult}")
    log_entry = f"[{datetime.utcnow()}] Incoming text: {SpeechResult}"
    with open("call_logs.txt", "a") as log_file:
        log_file.write(log_entry + "\n")
    return "Processed"

if __name__ == "__main__":
    import uvicorn
    print("[DEBUG] Starting local server and connecting SIP.")
    uvicorn.run(app, host="0.0.0.0", port=8000)
