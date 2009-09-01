import re
import urllib
import urllib2
import random
from BeautifulSoup import BeautifulSoup

from tineye.exceptions import InvalidImageError


# From the TinEye TOS.
# Automated searching on TinEye via search scripts will not be tolerated, and 
# will result in blocking of your IP address and/or other termination of 
# your TinEye account.

# We will randomly choose a user agent from a list of valid user agents, and also
# stagger the intervals that we make calls to the service. This results in much
# longer than necessary queries, but hopefully looks less like an automated script
# and more like someone testing their service.

# We randomly choose a user agent from the list to report to the TinEye service
USER_AGENTS = [
    'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Mozilla/4.61 [en] (X11; U; ) - BrowseX (2.0.0 Windows)',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en; rv:1.8.1.6) Gecko/20070809 Camino/1.5.1',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/3.0.183 Safari/531.0',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.36 Safari/525.19',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8) Gecko/20051111 Firefox/1.5 BAVM/1.0.0',
    'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5 (.NET CLR 3.5.30729)',
    'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.1.14) Gecko/20080821 Firefox/2.0.0.14',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Meridio for Excel 5.0.251; Meridio for PowerPoint 5.0.251; Meridio for Word 5.0.251; Meridio Protocol; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Business Everywhere 7.1.2; GTB6; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0)',
    'Mozilla/1.22 (compatible; MSIE 2.0; Windows 95)',
]

class TinEye(object):
    
    TIN_EYE_SEARCH_URL ='http://tineye.com/search'
    
    def search(self, url):
        # POST values that need to be submitted with the form.
        values = {
            'url' : url,
            'submit' : 'Search'
        }
        
        headers = { 'User-Agent' : random.choice(USER_AGENTS) }
        data = urllib.urlencode(values)
        req = urllib2.Request(self.TIN_EYE_SEARCH_URL, data, headers)
        response = urllib2.urlopen(req)
        soup = BeautifulSoup(response.read())
        if soup.h2:
            if 'string' in dir(soup.h2):
                # try to get the number of results if it exists.
                elements = soup.h2.string.strip().split(' ')
                if len(elements):
                    num_result = int(elements[0])
            else:
                raise InvalidImageError('Problem parsing search data.')
        else:
            raise InvalidImageError('Unable to search for picture.')
        return num_result, response.geturl()
        

class TinEyePhoto(object):
    """
    Object to represent a photo.
    """
    def __init__(self, name, image_url, *args, **kwargs):
        super(TinEyePhoto, self).__init__(*args, **kwargs)
        self.name = name
        self.image_url = image_url

    def __str__(self):
        return self.image_url
