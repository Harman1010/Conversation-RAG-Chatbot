from sklearn.metrics.pairwise import cosine_similarity
import re


SIMILARITY_THRESHOLD = 0.55


def clean_text(text):

    text = text.lower()

    words = re.findall(r"\\b\\w+\\b", text)

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

    similarity = cosine_similarity(
        [embedding1],
        [embedding2]
    )[0][0]

    return similarity


def calculate_topic_score(semantic_score, keyword_score):

    final_score = (
        0.7 * semantic_score
        + 0.3 * keyword_score
    )

    return final_score