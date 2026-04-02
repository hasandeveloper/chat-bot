from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    breakpoint()
    return {"message": "Chatbot Running"}

