import logging

from fastapi import FastAPI

# Setup logging
logging.basicConfig(format="[%(levelname)s] - %(message)s", level=logging.DEBUG)

logging.info("Starting payment service...")

# Start API Server
app = FastAPI()

logging.info("Ready to process transactions.")

# Endpoints
@app.get("/")
def get() -> str:
    return "Hello world!"

@app.get("/transactions")
def get_transactions() -> list:
    return ["transaction 1", "transaction 2"]
