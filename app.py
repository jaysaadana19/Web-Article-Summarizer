from flask import Flask, request, render_template
from summarizer import summarize_article

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.form['url']
    summary = summarize_article(url)
    return render_template('summary.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
