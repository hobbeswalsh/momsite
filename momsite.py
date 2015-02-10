from flask import Flask, render_template, redirect, request, url_for

import constants

app = Flask(__name__)


@app.route('/')
def index():
    if request.args.get("blue"):
        template = "index-blue.html"
    else:
        template = "index.html"
    return render_template(template, caption=constants.get_caption())


@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))


@app.route('/about')
def get_main():
    return render_template("about.html")


@app.route('/resume')
def get_resume():
    return render_template("resume.html")


@app.route('/testimonials')
def get_testimonials():
    return render_template('testimonials.html')


@app.route('/contact')
def get_contact_info():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
