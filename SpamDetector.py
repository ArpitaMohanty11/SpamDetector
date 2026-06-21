import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


data = pd.read_csv(
    "sms+spam+collection/SMSSpamCollection",
    sep="\t",
    names=["label", "message"]
)


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["message"])


y = data["label"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy * 100, "%")

msg = input("Enter a message: ")

msg_vector = vectorizer.transform([msg])

prediction = model.predict(msg_vector)

print("Prediction:", prediction[0])
import pickle

pickle.dump(model, open("spam_model.pkl", "wb"))
print("Model saved successfully!")

