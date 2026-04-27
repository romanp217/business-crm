from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Business CRM API is running"}
