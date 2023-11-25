from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # Extract data from the form
        username = request.form['username']
        # Perform search with Maigret here
        results = perform_maigret_search(username)
        return render_template('results.html', results=results)
    else:
        # For a GET request, just display the search form
        return render_template('search_form.html')

def perform_maigret_search(username):
    # Your Maigret search logic goes here
    return search_results

if __name__ == '__main__':
    app.run(debug=True)
