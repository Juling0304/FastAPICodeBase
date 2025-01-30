#!/bin/bash
set -e


# Check if 'redis-server-9994' process is already running
if pm2 describe redis > /dev/null; then
  echo "'redis' process is already running. Skipping Redis server startup."
else
  # Run Redis server with PM2
  echo "Starting Redis on port 9993 for initialization..."

  pm2 start start_redis.sh --name redis

  echo "Checking Redis health on port 9994..."
  for i in {1..1000}; do
      if redis-cli -p 9994 ping | grep -q "PONG"; then
          echo "Redis on port 9994 is ready."
          break
      else
          echo "Redis not ready yet... retrying... ($i/1000)"
          sleep 3
      fi

      if [ $i -eq 1000 ]; then
          echo "Redis on port 9994 did not become ready in time."
          exit 1
      fi
  done

  echo "Redis server started successfully."
fi

# Check if 'backend' process is already running
if pm2 describe backend > /dev/null; then
  echo "'backend' process is already running. Skipping FastAPI app startup."
else
  # Run FastAPI app with PM2
  pm2 start start_fastapi.py --name backend --max-memory-restart 8000M --interpreter python3 --log-date-format "YYYY-MM-DD HH:mm:ss"
  echo "FastAPI app started successfully."
fi

# Check if 'celery_worker' process is already running
if pm2 describe celery_worker > /dev/null; then
  echo "'celery_worker' process is already running. Skipping FastAPI app startup."
else
  # Run FastAPI app with PM2
  pm2 start start_celery.sh --name celery_worker --max-memory-restart 4000M --log-date-format "YYYY-MM-DD HH:mm:ss"
  echo "celery_worker started successfully."
fi