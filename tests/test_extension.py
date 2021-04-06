# -*- coding: utf-8 -*-
"""
    test
    ~~~~
    Flask-SQL-XSS-Injection-Check is a simple extension to Flask allowing you to check for
    sql and xss injection attacks.
    
    :copyright: (c) 2021 by Deepak Singh.
    :license: MIT, see LICENSE for more details.
"""
import unittest
from flask import Flask, Response
from flask_sql_xss_injection_check.extension import SQLXSSCHECK


class FlaskSQLXSSInjectionCheckTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        SQLXSSCHECK(self.app)

        @self.app.route('/test', methods=['GET','PUT','POST','DELETE'])
        def index():
            print("Index controller invoked")
            response = Response(headers={"custom": "dictionary"})
            return 'Welcome'

    def iter_verbs(self, c):
        ''' A simple helper method to iterate through a range of
            HTTP Verbs and return the test_client bound instance
        '''
        for verb in ['get', 'head', 'options']:
            yield getattr(c, verb)

    def iter_responses(self, path, verbs=['get', 'post', 'put', 'delete'], **kwargs):
        for verb in verbs:
            print("Now invoking:", verb)
            yield self._request(verb.lower(), path, **kwargs)

    def _request(self, verb, *args, **kwargs):
        headers = {}
        with self.app.test_client() as c:
            return getattr(c, verb)(*args, headers=headers, **kwargs)

    def get(self, *args, **kwargs):
        print("get Invoked")
        return self._request('get', *args, **kwargs)

    def post(self, *args, **kwargs):
        print("post Invoked")
        return self._request('post', *args, **kwargs)

    def put(self, *args, **kwargs):
        print("put Invoked")
        return self._request('put', *args, **kwargs)

    def delete(self, *args, **kwargs):
        print("delete Invoked")
        return self._request('delete', *args, **kwargs)

    def test_responds_with_200_for_valid_request(self):
        ''' If the request is safe i.e. no sql or XSS match found then
            it should return 200.
        '''
        for resp in self.iter_responses('/test'):
            self.assertEqual(resp.status_code, 200)

    def test_responds_with_400_for_unsafe_sql_request(self):
        ''' If the request is unsafe i.e. sql match found then
            it should return 400.
        '''
        for resp in self.iter_responses('/test?name="--"'):
            self.assertEqual(resp.status_code, 400)

    def test_responds_with_400_for_unsafe_xss_request(self):
        ''' If the request is unsafe i.e. XSS match found then
            it should return 400.
        '''
        for resp in self.iter_responses('/test?name=<script>alert("OK")</script>'):
            self.assertEqual(resp.status_code, 400)

if __name__ == "__main__":
    unittest.main()