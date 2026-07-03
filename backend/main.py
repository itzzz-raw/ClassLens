from fastapi import FastAPI

app = FastAPI(title="ClassLens API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the ClassLens API"}