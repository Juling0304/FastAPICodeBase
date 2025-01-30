#!/bin/bash
for i in {1..1000}; do
    if curl -s -o /dev/null -w "%{http_code}" http://localhost:9995/api/v1/ | grep -q "200"; then
        echo "API is ready at http://localhost:9995/api/v1/"
        echo "Starting Celery worker..."
        celery -A app_celery.worker.celery_worker.celery_worker_app worker --pool=prefork --prefetch-multiplier=1
        break
    else
        echo "API not ready yet... retrying... ($i/1000)"
        sleep 3
    fi

    if [ $i -eq 1000 ]; then
        echo "API did not become ready in time."
        exit 1
    fi
done