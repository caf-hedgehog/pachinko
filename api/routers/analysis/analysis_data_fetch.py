from fastapi import APIRouter, Request
from http import HTTPStatus
from schemas.analysis.analysis_data_fetch_schema import AnalysisDataFetchResponse

router = APIRouter(prefix="/data")


@router.get("/fetch", response_model=AnalysisDataFetchResponse)
async def get_shinfo_data(request: Request):
    return AnalysisDataFetchResponse(status=HTTPStatus.OK, result=1111)
