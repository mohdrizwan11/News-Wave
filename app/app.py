from flask import Flask, render_template, request
from newsapi import NewsApiClient

# init flask app
app = Flask(__name__)

# Init news api
newsapi = NewsApiClient(api_key='05aff1de3e9a41c490e6c1e247ab6eab')

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

if __name__ == "__main__":
    app.run(debug=True)