from fastapi import FastAPI
from routers.analysis.analysis_router import router as analysis_router

app = FastAPI(title="Pachinko Data Analycs")
app.include_router(analysis_router)


@app.get("/")
async def health_check():
    return {"message": "helth check ok"}
