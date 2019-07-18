from flask import render_template

from . import main


@main.app_errorhandler(404)
def page_not_fount(e):
    return render_template('error.html', code=404, message=e), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', code=500, message=e), 500
