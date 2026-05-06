from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re
from processing.summarizer import generate_summary


model = SentenceTransformer("all-MiniLM-L6-v2")

SIMILARITY_THRESHOLD = 0.30


def create_embedding(text):

    return model.encode(text)


def clean_text(text):

    text = text.lower()

    words = re.findall(r"\b\w+\b", text)

    return set(words)


def get_keyword_overlap(text1, text2):

    words1 = clean_text(text1)
    words2 = clean_text(text2)

    union = words1.union(words2)

    if len(union) == 0:
        return 0

    overlap = words1.intersection(words2)

    return len(overlap) / len(union)


def get_semantic_similarity(embedding1, embedding2):

    similarity = cosine_similarity([embedding1],[embedding2])[0][0]

    return similarity


def calculate_topic_score(semantic_score, keyword_score):

    final_score = (0.7 * semantic_score+ 0.3 * keyword_score)

    return final_score


def create_topic_checkpoints(messages):

    checkpoints = []

    current_topic = []

    topic_id = 1

    for current_message in messages:

        # First message starts topic
        if len(current_topic) == 0:

            current_topic.append(current_message)

            continue

        # Build topic context
        topic_context = " ".join(
            [
                msg["text"]
                for msg in current_topic[-15:]
            ]
        )

        current_text = current_message["text"]

        # Create embeddings
        topic_embedding = create_embedding(topic_context)

        current_embedding = create_embedding(current_text)

        # Similarity scores
        semantic_score = get_semantic_similarity(topic_embedding,current_embedding)

        keyword_score = get_keyword_overlap(topic_context,current_text)

        final_score = calculate_topic_score(semantic_score,keyword_score)

        # Topic shift
        short_message = len(current_text.split()) < 6
        if final_score < SIMILARITY_THRESHOLD and not short_message:
            topic_text = " ".join(
                [
                    msg["text"]
                    for msg in current_topic
                ]
            )
            topic_summary = generate_summary(topic_text)
            checkpoints.append({
                "topic_id": topic_id,
                "start_message": current_topic[0]["message_id"],
                "end_message": current_topic[-1]["message_id"],
                "summary": topic_summary,
                "messages": current_topic
            })

            topic_id += 1
            current_topic = [current_message]

        else:
            current_topic.append(current_message)

    # Save last topic
    if current_topic:
        topic_text = " ".join(
            [
                msg["text"]
                for msg in current_topic
            ]
        )
        topic_summary = generate_summary(topic_text)
        checkpoints.append({
            "topic_id": topic_id,
            "start_message": current_topic[0]["message_id"],
            "end_message": current_topic[-1]["message_id"],
            "summary" : topic_summary,
            "messages": current_topic
        })

    return checkpoints
def create_hundred_message_checkpoints(messages):

    checkpoints = []

    chunk_size = 100

    checkpoint_id = 1

    for i in range(0, len(messages), chunk_size):

        chunk = messages[i:i + chunk_size]

        chunk_text = " ".join(
            [
                msg["text"]
                for msg in chunk
            ]
        )

        chunk_summary = generate_summary(
            chunk_text
        )

        checkpoint_data = {
            "checkpoint_id": checkpoint_id,
            "start_message": chunk[0]["message_id"],
            "end_message": chunk[-1]["message_id"],
            "summary": chunk_summary,
            "messages": chunk
        }

        checkpoints.append(checkpoint_data)

        checkpoint_id += 1

    return checkpoints