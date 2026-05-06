from transformers import pipeline


summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)


def generate_summary(text):

    # Skip tiny text
    if len(text.split()) < 30:

        return text

    # Limit text length for model stability
    words = text.split()

    limited_text = " ".join(words[:400])

    result = summarizer(
        limited_text,
        max_length=80,
        min_length=20,
        do_sample=False
    )

    return result[0]["summary_text"]