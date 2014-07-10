#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'jcgregorio@google.com (Joe Gregorio)'

import sys

from oauth2client import client
from apiclient import sample_tools

def convert(input):
    if isinstance(input, dict):
        return dict((convert(key), convert(value)) for key, value in input.iteritems())
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      argv, 'plus', 'v1', __doc__, __file__,
      scope='https://www.googleapis.com/auth/plus.me')

  try:
    person = service.people().get(userId='me').execute()

    request = service.activities().search(query='copa 2014', orderBy='recent')
    contador = 0

    while request is not None:
      activities_doc = request.execute()
      for item in activities_doc.get('items', []):
        contador = contador + 1
        #print contador
        print convert(item)
        #print item
        #STRING_DATA = dict([(str(k), v) for k, v in item.items()])
        #print STRING_DATA
        

      request = service.activities().list_next(request, activities_doc)
    
    print 'Posts : %s' % contador

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run'
      'the application to re-authorize.')

if __name__ == '__main__':
    #collections = {}
    main(sys.argv)
