from pydantic import BaseModel

import bs4


class AnalysisDataFetchResponse(BaseModel):
    status: int
    result: int
