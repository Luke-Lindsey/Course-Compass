from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

print("hello")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Course Compass API running"}

@app.post("/predict")
def predict(data: dict):
    transcript = data.get("transcript", {})
    target_course = data.get("target_course", "")

    return {
        "predicted_grade": "B+",
        "confidence": 0.85,
        "target": target_course
    }