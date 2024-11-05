from flask import Flask, render_template_string
import threading

# Initialize Flask app
app = Flask(__name__)

# HTML template (moved here to keep it separate from bot logic)
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
    <style>
        body {
            background-color: #f0f8ff;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            background-color: #fff;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
        }
        a {
            text-decoration: none;
            color: #1e90ff;
            font-weight: bold;
        }
        a:hover {
            color: #ff4500;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome</h1>
        <p>By <a href="https://t.me/gkbotz" target="_blank">GKBotz</a></p>
    </div>
</body>
</html>
'''

# Define the route for the main page
@app.route('/')
def welcome():
    return render_template_string(html_template)

# Function to run the Flask app in a separate thread
def run_web():
    app.run(host='0.0.0.0', port=8080)

# Start the Flask web server in a new thread
def start_worker():
    web_thread = threading.Thread(target=run_web)
    web_thread.start()
