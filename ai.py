from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    results = []
    for g in soup.select(".BNeawe"):
        results.append(g.text)

    return results[:5]

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data["question"]

    hasil = search_google(question)

    return jsonify({
        "question": question,
        "answer": hasil
    })

app.run(debug=True)
