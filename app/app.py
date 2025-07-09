from flask import Flask, render_template, request, jsonify
from newsapi import NewsApiClient
import sys
import os
import logging
from logging.handlers import RotatingFileHandler

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import config

# init flask app
app = Flask(__name__)
config_name = os.environ.get('FLASK_CONFIG') or 'default'
app.config.from_object(config[config_name])

# Init news api
newsapi = NewsApiClient(api_key=app.config['NEWS_API_KEY'])

# Configure logging for production
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/newswave.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('News Wave startup')

# List of categories
categories = [
    {"code": "", "name": "All Categories"},
    {"code": "business", "name": "Business"},
    {"code": "entertainment", "name": "Entertainment"},
    {"code": "general", "name": "General"},
    {"code": "health", "name": "Health"},
    {"code": "science", "name": "Science"},
    {"code": "sports", "name": "Sports"},
    {"code": "technology", "name": "Technology"},
]

@app.route("/", methods=['GET', 'POST'])
def home():
    try:
        if request.method == "POST":
            keyword = request.form.get("keyword")
            category = request.form.get("category")
            
            if keyword:
                related_news = newsapi.get_everything(q=keyword, language='en', sort_by='relevancy')
                articles = related_news['articles']
            else:
                top_headlines = newsapi.get_top_headlines(category=category, language="en")
                articles = top_headlines['articles']
            
            return render_template("news.html", articles=articles, keyword=keyword, category=category, categories=categories)
        else:
            top_headlines = newsapi.get_top_headlines(language="en")
            articles = top_headlines['articles']
            return render_template("news.html", articles=articles, category="", categories=categories)
    except Exception as e:
        print(f"Error: {e}")
        top_headlines = newsapi.get_top_headlines(language="en")
        articles = top_headlines['articles']
        return render_template("news.html", articles=articles, category="", categories=categories)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f'Unhandled exception: {str(e)}')
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))