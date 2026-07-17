import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


df = pd.read_csv(
    r"D:\ML JOURNEY\Spam Mail\spam.csv",
    encoding="latin-1"
)


df = df[['Category', 'Message']]


df['Category'] = df['Category'].map({'ham': 0, 'spam': 1})


df.columns = ['spam', 'message']


X = df['message']
y = df['spam']


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

vectorizer = TfidfVectorizer()

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

print("Accuracy :", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


test_email = [
    "Congratulations! You have won $5000. Click here to claim your prize."
]

test_vector = vectorizer.transform(test_email)

prediction = model.predict(test_vector)

if prediction[0] == 1:
    print("\nPrediction: Spam Mail")
else:
    print("\nPrediction: Not Spam")


email = [ "meeting tommorrow with the boss urgent free ham spam" ]
nvectorizer=vectorizer.transform(email)
prediction=model.predict(nvectorizer)
if(prediction[0]==1):
    print("spam email::")
else:
    print("ham email")
    

import pickle

pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model Saved Successfully!")