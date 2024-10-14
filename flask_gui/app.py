from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle Python script execution
@app.route('/run_script', methods=['POST'])
def run_script():
    try:
        # Define the path to the script located outside the current directory
        script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts', 'search_polar.py')
        
        # Execute the external Python script using python3
        result = subprocess.run(['python3', script_path], capture_output=True, text=True)
        
        # Get the output and errors from the script execution
        output = result.stdout
        error = result.stderr
        
        # Display output or error on the web page
        if result.returncode == 0:
            return f"<h2>Output:</h2><pre>{output}</pre>"
        else:
            return f"<h2>Error:</h2><pre>{error}</pre>"
    except Exception as e:
        return f"<h2>Execution Error:</h2><pre>{str(e)}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
