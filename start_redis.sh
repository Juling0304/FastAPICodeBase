#!/bin/bash
set -e

# echo "Starting Redis on port 9993 for initialization..."
# redis-server --port 9993 --daemonize yes

# echo "Checking Redis health on port 9993..."
# for i in {1..1000}; do
#     if redis-cli -p 9993 ping | grep -q "PONG"; then
#         echo "Redis on port 9993 is ready."
#         break
#     else
#         echo "Redis not ready yet... retrying... ($i/1000)"
#         sleep 3
#     fi

#     if [ $i -eq 1000 ]; then
#         echo "Redis on port 9993 did not become ready in time."
#         exit 1
#     fi
# done

# echo "Running initialization script..."
# python3 ./initialize_redis.py

# echo "Shutting down initialization Redis..."
# redis-cli -p 9993 shutdown && exec redis-server --port 9994

exec redis-server --port 9994
