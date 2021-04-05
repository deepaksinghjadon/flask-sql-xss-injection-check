# -*- coding: utf-8 -*-
"""
    extension
    ~~~~
    Flask-SQL-XSS-Injection-check is a simple extension to Flask allowing you to support SQL &
    XSS Injection check.
"""
import logging
from flask import request
from .utils import has_sql, has_xss

LOG = logging.getLogger(__name__)

class SQLXSSCHECK(object):
    """
    Adds a `before request` method to check for sql and XSS injection.
    The pre-processor method returns a 403 if either sql or XSS check is true
    """
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.before_request(self.check_vulnerability)

    def check_vulnerability(self):
        url = request.url
        body = request.get_data().decode('UTF-8')
        is_vulnerable = (
            has_sql(url) or
            has_sql(body) or
            has_xss(url) or
            has_xss(body)
        )
        if is_vulnerable:
            LOG.debug("Vulnerability found, rejecting the request with 400")
            return "Bad request", 400
        else:
            LOG.debug("No SQL or XSS vulnerability found, clean request allowed")