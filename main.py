from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok", "message": "Bitrix thermo bot is running"}


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("INCOMING:", data)
    return {"ok": True}
