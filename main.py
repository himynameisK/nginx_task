from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Монтируем статические файлы (CSS, JS, изображения)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Настраиваем шаблонизатор
templates = Jinja2Templates(directory="templates")

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.get("/items/{item_id}", response_class=HTMLResponse)
async def read_item(request: Request, item_id: str):
    return templates.TemplateResponse(
        "item.html",
        {
            "request": request,
            "item_id": item_id,
            "example_data": ["Статистика", "Графики", "Отчёты"]
        }
    )