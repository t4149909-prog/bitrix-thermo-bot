from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok", "message": "Bitrix thermo bot is running"}


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("INCOMING WEBHOOK:", data)
    return {"ok": True}


@app.api_route("/install", methods=["GET", "POST"])
async def install(request: Request):
    if request.method == "GET":
        return PlainTextResponse("Bitrix app install endpoint is working")

    form = await request.form()
    data = dict(form)
    print("INSTALL DATA:", data)
    return PlainTextResponse("installed")


@app.api_route("/app", methods=["GET", "POST"])
async def app_handler(request: Request):
    if request.method == "GET":
        html = """
        <!doctype html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Термо ИИ</title>
        </head>
        <body>
            <h1>Термо ИИ подключен</h1>
            <p>Приложение установлено и отвечает.</p>
        </body>
        </html>
        """
        return HTMLResponse(content=html)

    form = await request.form()
    data = dict(form)
    print("APP HANDLER DATA:", data)
    return JSONResponse({"ok": True})
