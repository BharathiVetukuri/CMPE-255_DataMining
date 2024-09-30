#### random_joke_app/app.py
```python
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    joke = fetch_joke()
    return render_template('index.html', joke=joke)

def fetch_joke():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    if response.status_code == 200:
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "Failed to fetch joke."

if __name__ == '__main__':
    app.run(debug=True)
