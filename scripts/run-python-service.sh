#!/bin/bash

SERVICE=$1

if [ -z "$SERVICE" ]; then
  echo "Usage: ./scripts/run-python-service.sh service-a"
  exit 1
fi

cd backends/python-fastapi/$SERVICE || exit 1

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate
pip install -r requirements.txt

uvicorn app.main:app --reload --port 8000
