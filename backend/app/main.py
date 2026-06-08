
from fastapi import FastAPI
from app.core.config import settings 
from app.api.auth import router as auth_router



app = FastAPI(
    title = 'saas-monitoring-platform',
    version='1.0.0'
    
)
app.include_router(auth_router)

@app.get('/')
def root():
    return {
        'message' : 'Saas monitoring platform API'
    }







