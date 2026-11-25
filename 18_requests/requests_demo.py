"""
Requests basics (Corey Schafer - Python Requests Tutorial).

Covers: GET a web page, download an image, status code and headers,
query params, POST form data, JSON response, basic auth and timeouts.
"""

from pathlib import Path

import requests

BASE_DIR = Path(__file__).parent  # folder of this script (18_requests/)


# --- 1. GET a web page -------------------------------------------------------
r = requests.get("https://xkcd.com/353/", timeout=10)
print(r)            # <Response [200]>
# print(dir(r))     # all attributes and methods of the Response object
# help(r)           # full docs (help() prints itself, no print() needed)
print(r.text)       # response body as a string (here: HTML)


# --- 2. Download an image (binary content) ----------------------------------
img_r = requests.get("https://imgs.xkcd.com/comics/python.png", timeout=10)
# img_r.content is raw bytes, the exact file the server sent

with open(BASE_DIR / "comic.png", "wb") as f:   # "wb" = write binary
    f.write(img_r.content)


# --- 3. Status code and headers ---------------------------------------------
print(r.status_code)  # 200 = OK, 404 = Not Found, 500 = server error
print(r.ok)           # True if status_code < 400, otherwise False
print(r.headers)      # response metadata (content type, date, server, ...)


# --- 4. Query parameters ----------------------------------------------------
# Pass params as a dict; requests builds and encodes the URL: ...?page=2&count=25
payload = {"page": 2, "count": 25}
r = requests.get("https://httpbin.org/get", params=payload, timeout=10)
print(r.text)
print(r.url)          # final URL with the query string


# --- 5. POST form data and read JSON ----------------------------------------
payload = {"username": "corey", "password": "testing"}
r = requests.post("https://httpbin.org/post", data=payload, timeout=10)
print(r.text)

r_dict = r.json()     # parse JSON body into Python objects (dict or list)
print(r_dict["form"])  # the form data the server received


# --- 6. Basic authentication ------------------------------------------------
r = requests.get(
    "https://httpbin.org/basic-auth/corey/testing",
    auth=("corey", "testing"),   # (username, password)
    timeout=10,
)
print(r.text)


# --- 7. Timeout and error handling ------------------------------------------
# The server waits 6 s, our limit is 3 s, so requests raises ReadTimeout.
# Without try/except the whole script would crash here.
try:
    r = requests.get("https://httpbin.org/delay/6", timeout=3)
    r.raise_for_status()      # raises HTTPError for 4xx/5xx status codes
    print(r)
except requests.exceptions.Timeout:
    print("Request timed out after 3 seconds")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
