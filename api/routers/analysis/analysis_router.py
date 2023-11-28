from fastapi import APIRouter
from routers.analysis import analysis_data_fetch

router = APIRouter(prefix="/api/analysis")

router.include_router(analysis_data_fetch.router)
