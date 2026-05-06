import re


interest_keywords = {
    "gym": "fitness",
    "workout": "fitness",
    "football": "sports",
    "cricket": "sports",
    "music": "music",
    "movie": "movies",
    "travel": "travel",
    "book": "reading",
    "coding": "technology",
    "python": "technology",
    "food": "food",
    "cook": "cooking"
}


def extract_persona(messages):

    full_text = " ".join(
        [
            msg["text"].lower()
            for msg in messages
        ]
    )

    # Detect interests
    detected_interests = []

    for keyword, category in interest_keywords.items():

        if keyword in full_text:

            detected_interests.append(category)

    detected_interests = list(set(detected_interests))

    # Average message length
    avg_message_length = sum(
        len(msg["text"].split())
        for msg in messages
    ) / len(messages)

    # Communication style
    if avg_message_length < 6:

        communication_style = "short messages"

    elif avg_message_length < 18:

        communication_style = "medium messages"

    else:

        communication_style = "long detailed messages"

    # Emoji usage
    emoji_pattern = r"[:;=8][\-]?[)\(DPp]"

    emoji_count = len(
        re.findall(emoji_pattern, full_text)
    )

    if emoji_count > 50:

        emoji_style = "high emoji usage"

    elif emoji_count > 10:

        emoji_style = "moderate emoji usage"

    else:

        emoji_style = "low emoji usage"

    persona = {
        "interests": detected_interests,
        "communication_style": communication_style,
        "emoji_style": emoji_style,
        "average_message_length": round(
            avg_message_length,
            2
        )
    }

    return persona