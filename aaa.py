import urllib.request
import os

path = os.path.dirname(__file__)

with urllib.request.urlopen("https://example.com/latest.zip") as upd:
    with open(path, "wb+") as f:
        f.write(upd.read())