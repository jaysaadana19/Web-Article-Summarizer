from browserless import BrowserlessClient
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def get_article_text(url):
    # Fetch web content
    with BrowserlessClient() as browserless:
        page = browserless.get(url)
        html_content = page.content

    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract text
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    return text

def summarize_article(url):
    article_text = get_article_text(url)

    # Tokenize sentences
    sentences = sent_tokenize(article_text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_sentences = [sentence for sentence in sentences if sentence.lower() not in stop_words]

    # Calculate word frequency
    word_freq = FreqDist(filtered_sentences)

    # Select top sentences for summary
    summary_sentences = sorted(filtered_sentences, key=lambda x: word_freq[x], reverse=True)[:5]

    summary = ' '.join(summary_sentences)
    return summary
