# -*- coding: utf-8 -*-
"""
    Tests for utility methods
    ~~~~
    Flask-SQL-XSS-Injection-Check is a simple extension to Flask allowing you to check for
    sql and xss injection attacks.
    
    :copyright: (c) 2021 by Deepak Singh.
    :license: MIT, see LICENSE for more details.
"""

import unittest
import urllib.parse

from flask_sql_xss_injection_check.utils import has_sql, has_xss

class UtilitiesTestCase(unittest.TestCase):
    def test_blank_sql_content(self):
        self.assertFalse(has_sql(''))

    def test_blank_xss_content(self):
        self.assertFalse(has_xss(''))

    def test_safe_simple_url_content(self):
        content = 'http://localhost:5000?name=deepak'
        self.assertFalse(has_sql(content))
        self.assertFalse(has_xss(content))

    def test_safe_complex_url_content(self):
        complex_content = 'http://localhost:5000?name=deepak&role=developer'
        self.assertFalse(has_sql(complex_content))
        self.assertFalse(has_xss(complex_content))

    def test_unsafe_param_with_sql_content(self):
        some_partial_sql = 'WHERE field = \'anything\' OR \'x\'=\'x\'\''
        self.assertTrue(has_sql("http://localhost:5000/" + urllib.parse.quote(some_partial_sql)))

    def test_unsafe_querystring_with_sql_content(self):
        some_params = {'name': 'WHERE field = \'anything\' OR \'x\'=\'x\'\''}
        self.assertTrue(has_sql("http://localhost:5000?" + urllib.parse.urlencode(some_params)))

    def test_unsafe_param_with_XSS_content(self):
        some_XSS_script = '<script>alert("OK")</script>'
        self.assertTrue(has_xss("http://localhost:5000/" + urllib.parse.quote(some_XSS_script)))

    def test_unsafe_querystring_with_XSS_content(self):
        some_params = {'name': '<script>alert("OK")</script>'}
        self.assertTrue(has_xss("http://localhost:5000?" + urllib.parse.urlencode(some_params)))


if __name__ == "__main__":
    unittest.main()