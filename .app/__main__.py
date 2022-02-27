import uvicorn
from app import app
from config import settings


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        app, host=settings.host, port=settings.port, log_level=settings.log_level
    )


if __name__ == "__main__":
    run()
