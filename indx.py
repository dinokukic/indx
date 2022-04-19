import argparse
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import os
import sys

SCOPES = ['https://www.googleapis.com/auth/indexing']
ENDPOINT = 'https://indexing.googleapis.com/v3/urlNotifications:publish'

# Add the path to your JSON key file from the service account here
JSON_KEY_FILE = 'key_file.json'

parser = argparse.ArgumentParser(
    prog='indx',
    description='Index or De-index a page from Google')


parser.add_argument('a',
                       action='store',
                       choices=['i', 'r'],
                       help='set if you want to index (i) or remove (r) URLs')

parser.add_argument('n',
                       action='store',
                       choices=['s', 'm'],
                       help='set if you are submitting a single (s) (URL) or multiple (m) URLs (CSV)')

parser.add_argument('path_or_url',
                       metavar='path',
                       type=str,
                       help='URL or path to csv file')


args = parser.parse_args()

action = 'URL_UPDATED' if args.a == 'i' else 'URL_DELETED'

credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)

http = credentials.authorize(httplib2.Http())


if args.n == 'm':
    url_list = open(args.path_or_url, 'r')
    for url in url_list:

      content = '''{
          \"url\": \"''' + url + '''\",
          \"type\": \"''' + action + '''\"
      }'''

      response, content = http.request(ENDPOINT, method="POST", body=content)

      print("URL: " + url)
      print("STATUS: " + str(response.status))
else:
    url = args.path_or_url
    content = '''{
          \"url\": \"''' + url + '''\",
          \"type\": \"''' + action + '''\"
      }'''

    response, content = http.request(ENDPOINT, method="POST", body=content)

    print('URL: ' + url)
    print('STATUS: ' + str(response.status))






# print('\n'.join(os.listdir(input_path)))