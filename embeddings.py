from sentence_transformers import SentenceTransformer


# Lightweight and fast embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text):

    return embedding_model.encode(text)