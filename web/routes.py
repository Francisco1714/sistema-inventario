from flask import render_template
from web import web_bp

@web_bp.route("/")
def inicio():
    return render_template("inicio.html")