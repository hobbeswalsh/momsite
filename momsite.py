from flask import Flask, jsonify, render_template

import constants

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/about')
def get_main():
    return render_template("about.html")


@app.route('/api/v1/resume')
def get_resume():
    return jsonify(constants.resume)


@app.route('/testimonials')
def get_testimonials():
    return render_template('testimonials.html')


@app.route('/contact')
def get_contact_info():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
