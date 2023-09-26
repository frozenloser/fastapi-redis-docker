import functools
import json
import logging
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from typing import Dict
from typing import Iterable
from typing import List
from typing import Tuple
from typing import Union

import redis
import httpx
from redis import ResponseError
from redis import asyncio as aioredis
from fastapi import BackgroundTasks
from fastapi import Depends
from fastapi import FastAPI

from app.config import Config



log = logging.getLogger(__name__)
config = Config()
app = FastAPI(title=config.title)
redis = redis.from_url(config.redis_url, decode_responses=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/health")
async def health():
    return {"status": "ok"}

@app.get("/api/v1/redis")
async def redis_health():
    try:
        redis.ping()
        return {"status": "ok"}
    except ResponseError:
        return {"status": "error"}
    
@app.get("/api/v1/redis/keys")
async def redis_keys():
    try:
        keys = redis.keys()
        return {"keys": keys}
    except ResponseError:
        return {"status": "error"}
    
@app.get("/api/v1/redis/{key}")
async def redis_get(key: str):
    try:
        value = redis.get(key)
        return {"value": value}
    except ResponseError:
        return {"status": "error"}

@app.post("/api/v1/redis/{key}")
async def redis_set(key: str, value: str):
    try:
        redis.set(key, value)
        return {"status": "ok"}
    except ResponseError:
        return {"status": "error"}
    
@app.delete("/api/v1/redis/{key}")
async def redis_delete(key: str):
    try:
        redis.delete(key)
        return {"status": "ok"}
    except ResponseError:
        return {"status": "error"}
    
