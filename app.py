from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Dummy articles data (replace with your data source)
articles_data = [
    {'id': 1, 'title': 'Article 1', 'summary': 'Summary of Article 1', 'content': 'Content of Article 1'},
    {'id': 2, 'title': 'Article 2', 'summary': 'Summary of Article 2', 'content': 'Content of Article 2'},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/article/<int:article_id>')
def article(article_id):
    article = next((a for a in articles_data if a['id'] == article_id), None)
    return render_template('article.html', article=article)

@app.route('/get_articles')
def get_articles():
    return jsonify({'articles': articles_data})

if __name__ == '__main__':
    app.run(debug=True)