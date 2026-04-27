from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.models.database import Base, engine
from app.routers import customers, invoices

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Business CRM</title>
        <style>
            body { font-family: Arial; margin: 40px; }
            h1 { color: #2c3e50; }
            a { color: #3498db; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>📊 Business CRM System</h1>
        <p>Το σύστημα λειτουργεί κανονικά!</p>
        
        <h3>🔗 Endpoints:</h3>
        <ul>
            <li><a href="/docs">📘 /docs</a> - API documentation (Swagger UI)</li>
            <li><a href="/customers">👥 /customers</a> - Λίστα πελατών</li>
            <li><a href="/invoices">🧾 /invoices</a> - Λίστα τιμολογίων</li>
        </ul>
        
        <hr>
        <small>Built with FastAPI + SQLite</small>
    </body>
    </html>
    """

app.include_router(customers.router)
app.include_router(invoices.router)
