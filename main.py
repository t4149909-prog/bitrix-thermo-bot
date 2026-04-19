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
    if request.method == "POST":
        form = await request.form()
        data = dict(form)
        print("INSTALL DATA:", data)

    html = """
    <!doctype html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Установка Термо ИИ</title>
        <script src="//api.bitrix24.com/api/v1/"></script>
    </head>
    <body>
        <h1>Установка Термо ИИ</h1>
        <p>Завершаем установку приложения...</p>

        <script>
            BX24.install(function() {
                BX24.installFinish();
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html)


@app.api_route("/app", methods=["GET", "POST"])
async def app_handler(request: Request):
    if request.method == "POST":
        form = await request.form()
        data = dict(form)
        print("APP HANDLER DATA:", data)

    html = """
    <!doctype html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Термо ИИ</title>
        <script src="//api.bitrix24.com/api/v1/"></script>
    </head>
    <body>
        <h1>Термо ИИ подключен</h1>
        <p>Приложение установлено и отвечает.</p>
        <div id="status">Инициализация...</div>

        <script>
            BX24.init(function() {
                document.getElementById("status").innerText = "BX24.init выполнен";
                BX24.fitWindow();
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html)
