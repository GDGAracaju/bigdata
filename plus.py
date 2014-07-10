#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'jcgregorio@google.com (Joe Gregorio)'

import sys

from oauth2client import client
from apiclient import sample_tools


def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      argv, 'plus', 'v1', __doc__, __file__,
      scope='https://www.googleapis.com/auth/plus.me')

  try:
    person = service.people().get(userId='me').execute()

    print 'Got your ID: %s' % person['displayName']
    print

    request = service.activities().list( userId=person['id'], collection='public')
    contador = 0

    while request is not None:
      activities_doc = request.execute()
      for item in activities_doc.get('items', []):
        print item
        #print '%-040s -> %s' % (item['id'], item['object']['content'][:30])
        #conteudo = item['object']['content']
        #if conteudo is not None:
        #    contador = contador + 1
        #    print conteudo.encode('ascii', 'ignore')
        #    #print '%-040s -> %s' % (item['id'], conteudo.encode('ascii', 'ignore'))
        #    #print '%-040s' % (item['object']['content'])

      request = service.activities().list_next(request, activities_doc)
    
    print 'Posts : %s' % contador

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run'
      'the application to re-authorize.')

if __name__ == '__main__':
  main(sys.argv)
