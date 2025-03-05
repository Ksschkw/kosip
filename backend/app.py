from flask import Flask, render_template, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template(app.static_folder,'index.html')
@app.route('/projects')
def serve_projects():
    return send_from_directory(app.static_folder, 'projects.html')
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)
if __name__ == '__main__':
    app.run(debug=True)
