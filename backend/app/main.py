
from fastapi import FastAPI
from app.core.config import settings 

app = FastAPI(
    title = 'saas-monitoring-platform',
    version='1.0.0'
    
)

@app.get('/')
def root():
    return {
        'message' : 'Saas monitoring platform API'
    }







