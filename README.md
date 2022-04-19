# indx
Python script to submit URLs to Google via Indexing API

## Usage
First you will need to set up a [project on Google Cloud Platform](https://console.developers.google.com/start/api?id=indexing.googleapis.com&credential=client_key).

Once you do that, you will need to [create a service account](https://console.developers.google.com/iam-admin/serviceaccounts). Download the JSON key file from the service account and save it in the same directory as this repository and rename it to _key_file.json_

To verify the ownership of the website, you will need to add the service account as a delegated owner to the Google Search Console.

### Prerequisites
- Python 3.* 
- argparse (for Python >= 3.2 included in the Python Standard Library)
- Google Client Library
- httplib2

If you already have Python 3.* installed, for the most part, running the following command in the terminal will do:

`pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

In a nutshell, to use the script:

arguments: 
- {i,r} - set if you want to index (i) or remove (r) URLs
- {s,m} - set if you are submitting a single (s) (URL) or multiple (m) URLs (CSV)
- path - URL or path to csv file


### Examples

***Index a single URL***

```python indx.py i s https://example.com/my-path```

***Index multiple URLs***

```python indx.py i m myurllist.csv```

***Remove a single URL from the index***

```python indx.py r s https://example.com/my-path```

***Remove multiple URLs from the index***

```python indx.py r m myurllist.csv```
