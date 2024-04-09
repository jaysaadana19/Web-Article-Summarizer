# Web Article Summarizer

## Overview
The Web Article Summarizer is a tool that allows users to quickly generate summaries of articles found on the web. It utilizes Browserless to retrieve web content and natural language processing techniques to condense the content into a concise summary.

## How to Use
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Flask application: `python app.py`
4. Access the tool in your browser at `http://localhost:5000`

## Features
- Web scraping to fetch article content.
- Text processing to remove unnecessary elements and stop words.
- Summarization using frequency-based algorithm.
- Simple web interface for user interaction.

## Dependencies
- Flask==2.0.2
- browserless==0.0.7
- nltk==3.6.5
