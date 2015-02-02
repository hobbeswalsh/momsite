from flask import Flask, jsonify, render_template

import constants

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/api/v1/main')
def get_main():
    return jsonify(constants.about_me)


@app.route('/api/v1/resume')
def get_resume():
    return jsonify(constants.resume)


@app.route('/api/v1/testimonials')
def get_testimonials():
    return jsonify(constants.testimonials)


@app.route('/api/v1/contact')
def get_contact_info():
    return jsonify(constants.contact_info)


if __name__ == '__main__':
    app.run(debug=True)
