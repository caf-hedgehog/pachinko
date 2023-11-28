from pydantic import BaseModel


class AnalysisDataFetchResponse(BaseModel):
    status: int
    result: int
