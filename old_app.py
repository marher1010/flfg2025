from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)


############
# SECURITY #
############


csrf = CSRFProtect(app)


@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response


##########
# GLOBAL #
##########


@app.route("/")
def main_global():
    return render_template("/global/main_global.html")


###########
# DESKTOP #
###########


@app.route("/advisors0")
def advisors_desktop():
    return render_template("/desktop/advisors_desktop.html")


@app.route("/services0")
def services_desktop():
    return render_template("/desktop/services_desktop.html")


##########
# MOBILE #
##########


@app.route("/advisors00")
def advisors_mobile():
    return render_template("/mobile/advisors_mobile.html")


@app.route("/services00")
def services_mobile():
    return render_template("/mobile/services_mobile.html")


@app.route("/login00")
def login_mobile():
    return render_template("/mobile/login_mobile.html")


@app.route("/disclosures00")
def disclosures_mobile():
    return render_template("/mobile/disclosures_mobile.html")


#######
# RUN #
#######


if __name__ == "__main__":
    app.run(debug=True)
