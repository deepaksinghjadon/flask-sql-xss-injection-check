Flask-CORS
==========

|Build Status| |Latest Version| |Supported Python versions|
|License|

A Flask extension for supporting SQL and XSS injection checks on the incoming request.

This would return a 400 Bad request response for requests where SQL or XSS injection check is positive

Installation
------------

Install the extension with using pip, or easy\_install.

.. code:: bash

    $ pip install -U flask-sql-xss-injection-check

Usage
-----

This package exposes a Flask extension which checkes all incoming requests for SQL and XSS injection attacks.

.. code:: python


    from flask import Flask
    from flask_sql_xss_injection_check import SQLXSSCHECK

    app = Flask(__name__)
    SQLXSSCHECK(app)

    @app.route("/")
    def helloWorld():
      return "Hello, safe world!"


Tests
-----

A simple set of tests is included in ``test/``. 
To run, install nose, and simply invoke ``nosetests`` or ``python setup.py test`` to exercise the tests.
