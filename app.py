from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/var/www/html/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/config')
def get_config():
    return jsonify({
        'app': app.name,
        'UPLOAD_FOLDER': UPLOAD_FOLDER
    })

@app.route('/files')
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify({'files': files})

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        file_path = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(file_path)
        return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
