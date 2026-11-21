import redis
import json

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True,
)

CACHE_KEY = "blog_posts_cache"
CACHE_TTL = 60


def get_cached_posts():
    cached_data = redis_client.get(CACHE_KEY)
    if cached_data:
        return json.loads(cached_data)
    return None


def set_cached_posts(posts_data):
    redis_client.setex(CACHE_KEY, CACHE_TTL, json.dumps(posts_data))


def clear_cache():
    redis_client.delete(CACHE_KEY)
    print("Redis cache cleared successfully.")
