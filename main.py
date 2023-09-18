<!DOCTYPE html>
<html>
<head>
    <title>Movie Recommendation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            color: #333;
        }
        label {
            font-weight: bold;
        }
        input[type="text"] {
            width: 100%;
            padding: 5px;
            margin-bottom: 10px;
        }
        button {
            background-color: #007BFF;
            color: #fff;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid #ccc;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>Movie Recommendation</h1>
    <form id="movieForm">
        <label for="year">Year:</label>
        <input type="number" id="year" name="year"><br>

        <label for="genre">Genre:</label>
        <input type="text" id="genre" name="genre"><br>

        <label for="certificate">Certificate:</label>
        <input type="text" id="certificate" name="certificate"><br>

        <label for="stars">Stars:</label>
        <input type="text" id="stars" name="stars"><br>

        <button type="button" onclick="getRecommendedMovies()">Get Recommendations</button>
    </form>

    <h2>Recommended Movies</h2>
    <table id="movieTable">
        <!-- Recommended movies will be displayed here -->
    </table>

    <script>
        function getRecommendedMovies() {
            // JavaScript code to send user inputs to the server (backend) and retrieve movie recommendations
            // You can use AJAX or fetch() to make a request to your backend service
            // Once you have the recommendations, populate the table with the data
        }
    </script>
</body>
</html>
