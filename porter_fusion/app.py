"""
MIT License

Copyright (c) 2024 JUAN CALVOPINA M

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

@author jcalvopinam
@version 1.0.0
"""

from flask import Flask, request, send_from_directory, render_template, redirect, url_for, flash
import os

app = Flask(__name__)
# app = Flask(__name__, template_folder='templates')
# app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')

home_user_folder = os.path.expanduser("~")

UPLOAD_FOLDER = os.getenv('UPLOAD_PATH', os.path.join(home_user_folder, "Downloads/porter"))
DOWNLOAD_FOLDER = os.getenv('DOWNLOAD_PATH', os.path.join(home_user_folder, "Downloads"))

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# Make sure the paths exiDOWNLOAD_FOLDERst, if not, it creates
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# List files and folders
def list_files_and_folders(path):
    items = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            items.append({'name': item, 'path': os.path.relpath(item_path, DOWNLOAD_FOLDER), 'is_folder': True})
        else:
            items.append({'name': item, 'path': os.path.relpath(item_path, DOWNLOAD_FOLDER), 'is_folder': False})
    # Sort folders first, then files
    return sorted(items, key=lambda x: (not x['is_folder'], x['name'].lower()))

# displays index.html page
@app.route('/')
@app.route('/<path:subpath>')
def index(subpath=''):
    current_path = os.path.join(app.config['DOWNLOAD_FOLDER'], subpath)
    if not os.path.exists(current_path):
        return 'Path not found', 404

    items = list_files_and_folders(current_path)

    return render_template('index.html', items=items, current_path=subpath)

# Uploads files to UPLOAD_FOLDER
@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part', 'danger')
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        flash('No selected file', 'danger')
        return redirect(url_for('index'))

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        flash('File uploaded successfully', 'success')
        return redirect(url_for('index'))

# Shows the list of the files to download from DOWNLOAD_FOLDER
@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)

# Exposes the application on the entire network interface on port 8081
def main():
    app.run(host='0.0.0.0', port=8081, debug=True)

if __name__ == '__main__':
    main()
