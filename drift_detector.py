from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()


TOPIC_KEYWORDS = {
    "music": ["music", "band", "song"],
    "fitness": ["gym", "run", "yoga", "fitness"],
    "food": ["food", "cooking", "chef"],
    "books": ["book", "reading"]
}


def detect_mood(text):

    sentiment = analyzer.polarity_scores(text)

    compound_score = sentiment["compound"]

    question_count = text.count("?")

    exclamation_count = text.count("!")

    if compound_score < -0.4:
        return "frustrated"

    if question_count >= 3:
        return "curious"

    if exclamation_count >= 3:
        return "playful"

    return "formal"


def detect_trigger(text):

    text = text.lower()

    for topic, keywords in TOPIC_KEYWORDS.items():

        for keyword in keywords:

            if keyword in text:

                return f"discussion about {topic}"

    return "general conversation"


def build_drift_timeline(messages):

    grouped_days = {}

    for message in messages:

        day = message["day_id"]

        if day not in grouped_days:

            grouped_days[day] = []

        grouped_days[day].append(
            message["text"]
        )

    timeline = []

    for day, texts in grouped_days.items():

        combined_text = " ".join(texts)

        mood = detect_mood(
            combined_text
        )

        trigger = detect_trigger(
            combined_text
        )

        timeline.append({
            "day": int(day),
            "mood": mood,
            "trigger": trigger
        })

    return timeline