# -*- coding: utf-8 -*-
"""
    flask_sql_xss_injection_check
    ~~~~
    Flask-SQL-XSS-Injection-check is a simple extension to Flask allowing you to support SQL &
    XSS Injection check.
"""
from .extension import SQLXSSCHECK
from .version import __version__

__all__ = ['SQLXSSCHECK']

# Set default logging handler to avoid "No handler found" warnings.
import logging
from logging import NullHandler

# Set initial level to WARN. Users must manually enable logging for
# flask_cors to see our logging.
rootlogger = logging.getLogger(__name__)
rootlogger.addHandler(NullHandler())

if rootlogger.level == logging.NOTSET:
    rootlogger.setLevel(logging.WARN)