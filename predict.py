import joblib


model = joblib.load(
    "intent_classifier/intent_model.pkl"
)


def predict_intent(text):

    prediction = model.predict(
        [text]
    )[0]

    return prediction


message = (
    "Remind me to call mom tomorrow"
)

prediction = predict_intent(
    message
)

print(prediction)