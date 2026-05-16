import logging

import chromadb

logger = logging.getLogger(__name__)

client = chromadb.Client()
collection = client.create_collection(name="marketing_memory")


def save_memory(text: str) -> None:
    try:
        collection.add(documents=[text], ids=[str(hash(text))])
        logger.info("Memory saved successfully")
    except Exception as e:
        logger.error(f"Save memory error: {e}")
        raise e


def query_memory(query: str) -> list:
    try:
        results = collection.query(query_texts=[query], n_results=5)
        return results["documents"]
    except Exception as e:
        logger.error(f"Query memory error: {e}")
        raise e
