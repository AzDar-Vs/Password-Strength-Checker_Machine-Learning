from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

app = Flask(__name__)
CORS(app)

data = pd.read_excel("/Users/a1111/Downloads/ML FINAL/Book3_converted (1).xlsx")
data = data.dropna(subset=['password'])

def length_based_label(pw):
    pw = str(pw)
    if len(pw) < 8:
        return 0
    elif len(pw) <= 15:
        return 1
    else:
        return 2

data['strength'] = data['password'].apply(length_based_label)

X = np.array(data["password"])
y = np.array(data["strength"])

def word(password):
    return list(password)

vectorizer = TfidfVectorizer(tokenizer=word)
X_vec = vectorizer.fit_transform(X)

xtrain, xtest, ytrain, ytest = train_test_split(X_vec, y, test_size=0.05, random_state=42)

models = {
    "Random Forest": RandomForestClassifier(),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(),
    "Naive Bayes": BernoulliNB()
}

results = {}
for name, model in models.items():
    model.fit(xtrain, ytrain)
    y_pred = model.predict(xtest)
    acc = accuracy_score(ytest, y_pred)
    prec = precision_score(ytest, y_pred, average='weighted')
    rec = recall_score(ytest, y_pred, average='weighted')
    f1 = f1_score(ytest, y_pred, average='weighted')

    results[name] = {
        'Accuracy': round(acc, 4),
        'Precision': round(prec, 4),
        'Recall': round(rec, 4),
        'F1_Score': round(f1, 4)
    }

@app.route('/predict', methods=['POST'])
def predict():
    password = request.json.get('password', '')
    pw_vec = vectorizer.transform([password]).toarray()
    label_map = {0: "Weak", 1: "Medium", 2: "Strong"}

    predictions = {}
    for name, model in models.items():
        pred = model.predict(pw_vec)[0]
        predictions[name] = label_map[pred]

    return jsonify({
        'predictions': predictions,
        'metrics': results
    })

if __name__ == '__main__':
    app.run(debug=True)
