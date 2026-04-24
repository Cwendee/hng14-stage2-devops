1.
File: api/requirements.txt  
Line: N/A  
Issue: Missing FastAPI and Uvicorn dependencies caused ModuleNotFoundError when starting the API  
Impact: Application failed to start because required packages were not installed  
Fix: Added `fastapi` and `uvicorn` to requirements.txt and reinstalled dependencies  

2.
File: api/main.py execution context  
Line: N/A  
Issue: Uvicorn was executed from system Python instead of the project virtual environment  
Impact: Installed dependencies were not recognized, leading to import errors  
Fix: Used `python -m uvicorn main:app --reload` to ensure execution within the active virtual environment  

3.
File: api/main.py  
Line: 1 (entry point reference)  
Issue: Uvicorn could not import module "main" due to incorrect working directory when starting the server  
Impact: Application failed to start with import error  
Fix: Changed working directory to `api/` before running uvicorn, or used module path `api.main:app` from project root  

4.
File: worker/worker.py  
Line: ~15–20 (main loop)  
Issue: Worker retrieved jobs from Redis queue using brpop but did not process them due to missing handling logic  
Impact: Jobs were removed from queue but never executed, leading to incorrect system behavior  
Fix: Added condition to decode job_id and pass it to process_job() function 

5.
File: worker/worker.py  
Line: Redis connection initialization  
Issue: Lack of visibility into Redis connection status made debugging difficult  
Impact: Could not easily determine if worker was connected to correct Redis instance  
Fix: Added `r.ping()` check and logging to confirm Redis connectivity during startup  

6.
File: system behavior (API + Worker interaction)  
Line: N/A  
Issue: Initial confusion due to asynchronous processing — job status remained "queued" when checked immediately after creation  
Impact: Misinterpreted system behavior as failure  
Fix: Introduced delay before polling job status and validated worker updates status to "completed" after processing  

7.
File: api/main.py  
Issue: Hardcoded Redis host "localhost" would fail in containerized environment  
Fix: Replaced with environment variables REDIS_HOST and REDIS_PORT

8.
File: worker/worker.py  
Issue: Hardcoded Redis host "localhost" would fail in container environment  
Fix: Replaced with environment variables REDIS_HOST and REDIS_PORT

9.
File: worker/Dockerfile / worker runtime  
Issue: Worker container failed to connect to Redis using hostname "redis" when run standalone  
Impact: Container could not resolve Redis host without a shared network  
Fix: Use docker-compose to define Redis service and shared network for inter-container communication

10.
File: api/Dockerfile  
Issue: Healthcheck failed because curl was not installed in container  
Impact: API container marked as unhealthy despite running successfully  
Fix: Installed curl using apt-get in runtime stage

11.
File: worker/worker.py  
Issue: Logs were not visible due to Python output buffering in container  
Impact: Worker appeared inactive despite processing jobs  
Fix: Added flush=True to print statements and enabled unbuffered execution

12.
File: docker-compose.yml  
Issue: Services started before dependencies were ready due to basic depends_on usage  
Impact: Worker and API experienced inconsistent behavior due to Redis not being ready  
Fix: Implemented health checks and used depends_on with condition: service_healthy

13.
File: docker-compose.yml  
Issue: Use of deploy.resources caused instability and Redis container exit in non-swarm mode  
Impact: Redis container stopped unexpectedly  
Fix: Removed deploy section and relied on standard docker-compose configuration

14.
File: Dockerfiles  
Issue: Dockerfiles did not follow best practices (apt usage, caching, non-root execution)  
Impact: Failed Hadolint checks in CI pipeline  
Fix: Refactored Dockerfiles to use minimal layers, non-root user, and proper package installation

15.
File: CI Pipeline (ci.yml)  
Issue: Hadolint failed due to non-existent frontend/Dockerfile  
Impact: CI pipeline failed during Dockerfile lint stage  
Fix: Removed frontend/Dockerfile from hadolint check

16.
File: CI Pipeline  
Issue: No deployment stage  
Impact: Pipeline incomplete for delivery  
Fix: Added rolling update deployment using Docker Compose with service-level updates