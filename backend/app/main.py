
# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from app.core.config import settings 
from app.api.auth import router as auth_router
from app.api.monitor import router as monitor_router
from app.api.monitor_log import router as monitor_log_router
from app.services.scheduler_service import (
    start_scheduler,
    stop_scheduler
)
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    
    print('starting scheduler....')

    start_scheduler()

    yield
    
    print('stoping scheduler....')

    stop_scheduler()


app = FastAPI(
    title = 'saas-monitoring-platform',
    version='1.0.0',
    lifespan=lifespan
    
)
app.include_router(auth_router)
app.include_router(monitor_router)
app.include_router(monitor_log_router)

@app.get('/')
def root():
    return {
        'message' : 'Saas monitoring platform API'
    }







