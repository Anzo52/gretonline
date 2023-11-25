from flask import Flask, request, render_template
from maigret import MaigretSite, MaigretDatabase, search as maigret_search

app = Flask(__name__)

@app.route('/search', methods=['GET', 'POST'])
def search_route():
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
    # Initialize Maigret database
    db = MaigretDatabase().load_from_file()

    # Perform the search
    try:
        result = maigret_search(username, db)
        # Format and return the results
        return format_maigret_results(result)
    except Exception as e:
        print(f"Error during search: {e}")
        return None

def format_maigret_results(results):
    # Format the results into a more readable form
    formatted_results = {}
    for site_name, data in results.items():
        if data['exists']:
            formatted_results[site_name] = data['url_user']
    return formatted_results

if __name__ == '__main__':
    app.run(debug=True)
