# Business CRM System

CRM application for managing customers and invoices.

## Technologies
- FastAPI
- SQLAlchemy (SQLite)
- SQLAlchemy ORM

## Features
- CRUD Customers
- CRUD Invoices
- REST API with Swagger docs

## Installation
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

