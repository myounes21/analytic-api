#!/bin/bash
set -e

RUN_PORT=${PORT:-8002}
RUN_HOST=${HOST:-0.0.0.0}

exec uvicorn main:app --host $RUN_HOST --port $RUN_PORT
