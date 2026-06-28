from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.logging import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Repository-Aware PR Review Agent")
    yield
    logger.info("Stopping Repository-Aware PR Review Agent")