from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    # Ensure the required email is displayed
    return {"email": "23f3004443@ds.study.iitm.ac.in", "message": "Hello from Codespaces!"}
