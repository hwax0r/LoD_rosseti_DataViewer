import os
from flask import Flask, render_template, request, redirect, url_for
import file_parsing

app = Flask(__name__)


@app.route('/')
def index():
    print('Kek')
    show_processed()
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def show_processed():
    photos = file_parsing.computerVision()
    return render_template('index.html', files=photos)


@app.route('/upload_file', methods=['POST'])
def upload_file():
    print('pop')
    uploaded_file = request.files['file']
    if uploaded_file.filename != '': uploaded_file.save(os.getcwd() + '/temp/' + uploaded_file.filename)
    show_processed()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
