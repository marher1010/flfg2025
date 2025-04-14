from flask import Flask, render_template, send_from_directory
from flask_wtf.csrf import CSRFProtect
from werkzeug.exceptions import Gone

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

@app.route('/final_sitemap.xml', methods=['GET'])
def sitemap():
    return send_from_directory('static', 'sitemap.xml')


##########
# GLOBAL #
##########


@app.route("/")
def main_global():
    return render_template("/global/main_global.html")


@app.route('/robots.txt')
def robots_txt():
    return render_template('robots.txt')


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


#############################
# RETURN GONE FOR OLD PAGES #
#############################


@app.route("/<path:old_page_path>")
def old_pages(old_page_path):
    non_existent_pages = [
        "lime-spinner-rotate",
        "counter-03",
        "cropped-fs-lime-png",
        "hillary-updated-opt",
        "medicare-supplement-image-1",
        "our-services-image-5",
        "retirement-planning-image-1-3",
        "home-slider-bg-btm",
        "paul-image",
        "3-signs-hes-cheating-for-you",
        "medicare-supplement-image-1-3",
        "retirement-planning-image-1",
        "estate-planing-image-new",
        "our-famlilies",
        "counter-06",
        "2023-tax-guide/2023-tax-guide",
        "ray-image",
        "backline-sin-juicio-asistencia-para-el-la-mayoria-de-personal-decisiones",
        "financial-planning-image-1-1",
        "desire-to-start-online-dating-a-nursing-assistant-nurse-online-dating-and-elitesingles",
        "puzzle_shape",
    ]

    if old_page_path in non_existent_pages:
        message = f'The page at "{old_page_path}" no longer exists'
        raise Gone(message)
    else:
        raise Gone("This page no longer exists")


#######
# RUN #
#######


if __name__ == "__main__":
    app.run(debug=True)
