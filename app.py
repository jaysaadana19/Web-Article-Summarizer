from flask import Flask, request, render_template
from summarizer import summarize_article

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    if request.method == 'POST':
        url = request.form['url']
        summary = summarize_article(url)
        return render_template('summary.html', summary=summary)
    else:
        return render_template('index.html')  # Render the index page for GET requests

if __name__ == '__main__':
    app.run(debug=True)
