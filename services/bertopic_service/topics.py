import logging
from bertopic import BERTopic

logger = logging.getLogger(__name__)

model = BERTopic(verbose=False)


def detect_topics(documents: list) -> dict:
    try:
        if len(documents) < 10:
            return {"error": "Need at least 10 documents for topic modeling"}

        topics, probs = model.fit_transform(documents)
        topic_info = model.get_topic_info()

        return {
            "status": "success",
            "num_topics": len(set(topics)),
            "topics": topics,
            "probabilities": probs.tolist(),
            "topic_info": topic_info.to_dict(),
        }
    except Exception as e:
        logger.error(f"BERTopic error: {e}")
        raise e
