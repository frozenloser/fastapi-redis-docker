from pydantic import BaseSettings


class Config(BaseSettings):
    redis_url: str = 'redis://redis:6379'
    title : str = 'Tribe Mobile Controller'
