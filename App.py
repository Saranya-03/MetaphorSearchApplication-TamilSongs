from flask import Flask, render_template, request
from elasticsearch_dsl import Index
from Query import search_query

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/search-meaning', methods=['GET', 'POST'])
def search_meaning():
    if request.method == 'POST':
        query = request.form['queryName']           # Get search phrase by using the name in the request
        res = search_query(query)                         # Get the response by processing the query by calling search method in Query class.
        hits = res['hits']['hits']
        num_results = res['hits']['total']['value']

        return render_template('MetaphorMeaningResults.html', query=query, hits=hits, num_results=num_results)

    if request.method == 'GET':
        return render_template('index.html', init='True')\


@app.route('/search-metaphors', methods=['GET', 'POST'])
def search_metaphors():
    if request.method == 'POST':
        query = request.form                        # Here, query is a dictionary which contains, inputTarget,sourceDom,inputType
        res = search_query(query)                         # Get the response by processing the query by calling search method in Query class.
        hits = res['hits']['hits']
        num_results = res['hits']['total']['value']
        return render_template('SearchMetaphorsResults.html', query=query, hits=hits, num_results=num_results)

    if request.method == 'GET':
        return render_template('index.html', init='True')


if __name__ == '__main__':
    app.run()
