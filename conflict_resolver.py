from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()


def calculate_emotional_weight(text):

    sentiment = analyzer.polarity_scores(text)

    emotional_weight = abs(
        sentiment["compound"]
    )

    return emotional_weight


def calculate_final_score(
    similarity_score,
    recency_score,
    emotional_weight
):

    final_score = (
        0.5 * similarity_score +
        0.3 * recency_score +
        0.2 * emotional_weight
    )

    return final_score


def detect_contradiction(texts):

    positive_found = False

    negative_found = False

    for text in texts:

        sentiment = analyzer.polarity_scores(text)

        if sentiment["compound"] > 0.3:
            positive_found = True

        if sentiment["compound"] < -0.3:
            negative_found = True

    return positive_found and negative_found


def resolve_conflicts(retrieved_chunks):

    ranked_chunks = []

    for chunk in retrieved_chunks:

        emotional_weight = (
            calculate_emotional_weight(
                chunk["text"]
            )
        )

        final_score = calculate_final_score(
            chunk["similarity"],
            chunk["recency"],
            emotional_weight
        )

        chunk["final_score"] = final_score

        ranked_chunks.append(chunk)

    ranked_chunks.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    contradiction_detected = (
        detect_contradiction(
            [
                chunk["text"]
                for chunk in ranked_chunks
            ]
        )
    )

    return {
        "contradiction_detected":
        contradiction_detected,

        "ranked_chunks":
        ranked_chunks[:3]
    }