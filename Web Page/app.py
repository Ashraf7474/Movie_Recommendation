
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd


app = Flask(__name__)

# Load your movie data from the CSV file into a Pandas DataFrame
movie_data = pd.read_csv('F:\\the khan\projects\IMDB Movie Recommdation\pythonProject\\Movie_Cleaned_Data.csv')  # Update with your data file

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_year = int(request.form['year'])
        input_genre = request.form['genre']
        input_certificate = request.form['certificate']

        # Filter movies based on user input
        filtered_movies = movie_data[
            (movie_data['Year of release'] == input_year) &
            (movie_data['Genre'].str.contains(input_genre, case=False)) &
            (movie_data['Certificate'] == input_certificate)
        ]

        # Sort the filtered movies by Rating
        sorted_movies = filtered_movies.sort_values(by='Rating', ascending=False)

        # Select the top 15 movies
        recommended_movies = sorted_movies.head(50)

        if not recommended_movies.empty:
            # Convert DataFrame to a list of dictionaries
            recommended_movies_list = recommended_movies.to_dict(orient='records')
            return render_template('recommended.html', recommended_movies=recommended_movies_list)
        else:
            return render_template('index.html', recommended_movies=None)

    return render_template('index.html', recommended_movies=None)

if __name__ == '__main__':
    app.run(debug=True)

