from flask import Flask, request, render_template
from summarizer import summarize_article

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['GET', 'POST'])  # Allow both GET and POST requests
def summarize():
    if request.method == 'POST':
        url = request.form['url']
        summary = summarize_article(url)
        return render_template('summary.html', summary=summary)
    else:
        # Handle GET request (if needed)
        pass

if __name__ == '__main__':
    app.run(debug=True)
