import pandas as pd
import re


def load_csv(path):
    df = pd.read_csv(path, header=None)
    df.columns = ["conversation"]
    return df


pattern = r"(User \d+): (.*?)(?=\nUser \d+:|$)"


def parse_conversations(df):

    messages = []

    global_id = 0

    for day_id, row in df.iterrows():

        conversation = str(row["conversation"])

        matches = re.findall(pattern, conversation, re.DOTALL)

        for speaker, message in matches:

            global_id += 1

            messages.append(
                {
                    "message_id": global_id,
                    "day_id": day_id,
                    "speaker": speaker,
                    "text": message.strip(),
                }
            )

    return messages