from flask import Blueprint, render_template, url_for

site_bp = Blueprint('site', __name__)


@site_bp.route('/')
def index():
    return render_template('site/index.html')
