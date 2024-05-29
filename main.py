from fastapi import FastAPI
from core import auth
from database import engine

app = FastAPI()

# Include routers
app.include_router(auth.router)

# Other configurations and middleware may be added here

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
