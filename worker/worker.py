import redis
import time
import sys

r = redis.Redis(host="redis", port=6379)

try:
    print("Connected to Redis:", r.ping(), flush=True)
except Exception as e:
    print("Redis connection failed:", e, flush=True)
    sys.exit(1)


def process_job(job_id):
    print(f"Processing job {job_id}", flush=True)
    time.sleep(2)
    r.hset(f"job:{job_id}", "status", "completed")
    print(f"Done: {job_id}", flush=True)


print("Worker started. Waiting for jobs...", flush=True)

while True:
    print("Checking for job...", flush=True)
    job = r.brpop("job", timeout=5)

    if job:
        _, job_id = job
        process_job(job_id.decode())
        