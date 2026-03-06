import json
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline



#Load intents data
with open("data/intents.json") as file:
    data = json.load(file)

patterns = []  #two string value
tags = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])

print("Total samples:", len(patterns)) #total patterns 

# train test Split coxrrectly
X_train, X_test, y_train, y_test = train_test_split(
    patterns,
    tags,
    test_size=0.2,
    random_state=42
)

print("Sample X_train:", X_train[:3])
print("Sample y_train:", y_train[:3])

# TF-IDF
vector = TfidfVectorizer(ngram_range=(1, 2),min_df=1,
    analyzer='word')

X_train_tfd = vector.fit_transform(X_train)
X_test_tfd = vector.transform(X_test)

# Train model
model = LogisticRegression(max_iter=1000, C=10,solver='lbfgs',
    )
model.fit(X_train_tfd, y_train)

#  Accuracy
# y_pred = model.predict(X_test_tfd)
# print("Accuracy:", accuracy_score(y_test, y_pred))
pipeline= Pipeline([("tfidf", TfidfVectorizer(ngram_range=(1,2), min_df=1)),
                    ("clf", LogisticRegression(max_iter=1000, C=100, solver="lbfgs" ))
                    ])
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))



#  Save model
os.makedirs("models", exist_ok=True)

with open("models/chatbot_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vector, f)

print(" Training completed successfully!") 