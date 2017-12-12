apiKey = "d6e1e049-21ae-4771-ba2a-c800c3659fca";

import urllib2
def lookup(url):
  # print "https://api.mxtoolbox.com/api/v1/lookup/dns/" + url + "/"

  hit = "https://dns-api.org/MX/" + url
  try:
    response = urllib2.urlopen(
      urllib2.Request(hit,
      headers={"Authorization": apiKey})
    )
    return response.read()
  except Exception as e:
    return ""
    pass

  # print resp.json()


# x =  lookup("getdecentralized.com")
# print x
