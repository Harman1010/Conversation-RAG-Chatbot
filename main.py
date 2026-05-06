from processing.parser import load_csv
from processing.parser import parse_conversations
from processing.checkpoint_manager import (create_topic_checkpoints)
from processing.persona_extractor import (
    extract_persona
)
from processing.save_outputs import save_json
df = load_csv("data/conversations.csv")

messages = parse_conversations(df)

print(f"\nTotal messages: {len(messages)}")

# Small sample first
sample_messages = messages[:300]

topic_checkpoints = create_topic_checkpoints(sample_messages)

print(f"\nTotal topics found: {len(topic_checkpoints)}\n")


for topic in topic_checkpoints[:5]:

    print("\n")

    print(f"Topic ID: {topic['topic_id']}")

    print(
        f"Messages "
        f"{topic['start_message']} "
        f"to "
        f"{topic['end_message']}"
    )

    print()

    for msg in topic["messages"][:3]:

        print(f"{msg['speaker']}: {msg['text']}")

    print()
from processing.checkpoint_manager import (
    create_topic_checkpoints,
    create_hundred_message_checkpoints
)
# Create 100-message checkpoints
hundred_msg_checkpoints = (
    create_hundred_message_checkpoints(
        sample_messages
    )
)

print(
    f"\n100-message checkpoints: ",
    f"{len(hundred_msg_checkpoints)}"
)
# Extract persona
persona = extract_persona(
    sample_messages
)

print("\n")

print("\nExtracted Persona:\n")

print(persona)

save_json(
    topic_checkpoints,
    "checkpoints/topic_checkpoints.json"
)

save_json(
    hundred_msg_checkpoints,
    "checkpoints/hundred_message_checkpoints.json"
)

save_json(
    persona,
    "checkpoints/persona.json"
)

print("\nAll checkpoint files saved.")