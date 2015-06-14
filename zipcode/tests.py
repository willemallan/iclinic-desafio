import json
import requests
import httplib
import urllib
import urllib2
from django.test import TestCase
from zipcode.models import ZipCode


def test_add_zipcode(zipcode):
    print '\nAdd zip_code {0}'.format(zipcode)
    req = urllib2.Request(
        'http://localhost:8000/zipcode/', 
        urllib.urlencode({'zip_code': zipcode})
    )
    return urllib2.urlopen(req)

def test_add_response(zipcode):
    r = test_add_zipcode(zipcode)
    print 'Response: {0} / {1}'.format(r.code, r.read())

def test_delete_response(zipcode):
    r = requests.request('DELETE', 'http://localhost:8000/zipcode/{0}'.format(zipcode))
    print '\nDelete: {0} / Return: {1}'.format(zipcode, r.status_code)

def test_show_response(zipcode):
    req = urllib2.Request(
        'http://localhost:8000/zipcode/{0}'.format(zipcode)
    )
    r = urllib2.urlopen(req)
    print '\nShow: {0} / Code Return: {1} / Return: {2}'.format(zipcode, r.code, r.read())

class ZipCodeMethodTests(TestCase):

    def tests(self):
        print '\n########################'
        print 'ADD ZIPCODES'
        print '########################'

        test_add_response('14020260')
        test_add_response('14110000')
        test_add_response('1402260')

        print '\n########################'
        print 'SHOW ZIPCODES'
        print '########################'

        test_show_response('?limit=1')
        test_show_response('?limit=2')
        test_show_response('14020260')
        test_show_response('14110000')
        test_show_response('1402260')

        print '\n########################'
        print 'DEL ZIPCODES'
        print '########################'

        test_delete_response('14020260')
        test_delete_response('14110000')
        test_delete_response('1402260')