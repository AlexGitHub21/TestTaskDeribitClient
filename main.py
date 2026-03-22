from fastapi import FastAPI, Depends
import uvicorn
import asyncio
from service import Service
from dependencies import get_service


app = FastAPI()


@app.get("/")
async def root():
    return {"status": "price tracking started"}

@app.get("/prices/")
async def get_prices_ticker(ticker: str, service: Service = Depends(get_service)):
    return await service.get_prices_ticker(ticker=ticker)

@app.get("/prices_latest/")
async def get_latest_prices(ticker: str, service: Service = Depends(get_service)):
    return await service.get_latest_price_ticker(ticker=ticker)

@app.get("/prices/by_date")
async def get_prices_by_period(ticker: str, from_ts: int, to_ts: int, service: Service = Depends(get_service)):
    return await service.get_price_ticker_by_period(ticker=ticker, from_ts=from_ts, to_ts=to_ts)




def start():
    uvicorn.run(app="main:app", reload=True)