import pycurl
from StringIO import StringIO
import re

buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://www.omerbsh.com/')
c.perform()
c.close()

body = buffer.getvalue()
print(body)