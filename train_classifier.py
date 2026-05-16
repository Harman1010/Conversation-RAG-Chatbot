import pandas as pd

from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.linear_model import (
    LogisticRegression
)

from sklearn.pipeline import Pipeline

from sklearn.model_selection import (
    train_test_split
)

from sklearn.metrics import (
    classification_report
)

import joblib


df = pd.read_csv(
    "intent_classifier/training_data.csv"
)


X = df["text"]

y = df["intent"]


X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
)


model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer()
    ),
    (
        "classifier",
        LogisticRegression(max_iter=1000)
    )
])


model.fit(
    X_train,
    y_train
)


predictions = model.predict(
    X_test
)


print(
    classification_report(
        y_test,
        predictions
    )
)


joblib.dump(
    model,
    "intent_classifier/intent_model.pkl"
)


print("Intent classifier saved")