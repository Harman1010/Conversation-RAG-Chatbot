import chromadb

from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="vectordb"
)

collection = client.get_or_create_collection(
    name="conversation_memory"
)


def store_topic_checkpoints(topic_checkpoints):

    for topic in topic_checkpoints:

        summary = topic["summary"]

        embedding = model.encode(
            summary
        ).tolist()

        collection.upsert(
            ids=[str(topic["topic_id"])],
            embeddings=[embedding],
            documents=[summary]
        )