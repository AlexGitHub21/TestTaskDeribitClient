from celery_app import celery_app
from core.db_dependency import DBDependency
from managers import Manager
from service import Service
import asyncio
from deribitclient import DeribitService


@celery_app.task
def fetch_prices():
    async def runner():
        db = DBDependency()
        manager = Manager(db=db)
        client = DeribitService()
        service = Service(manager=manager, client=client)

        await service.save_data("BTC")
        await service.save_data("ETH")

    asyncio.run(runner())