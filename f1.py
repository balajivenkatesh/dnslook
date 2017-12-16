import sys
import pickle
import json

import spi

def save_obj(obj, name):
  with open("obj/"+ name + ".pkl", "wb") as f:
      pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


count = 0
ant = 0
ans = {}
xx = []

try:
  with open("d77.txt") as f:
    for line in f:
      email = line.rstrip()
      # print email
      if "gmail" in email:
        dom = email.split("@")[1]
        print email + ", "  + "2, " + dom + ", " + "gmail"
        count += 1
      else:
        dom = email.split("@")[1]
        resp = spi.lookup(dom)
        ans[email] = resp
        # print "resp", resp
        # if not resp:
        #   print email+ ", "+ dom+ ", "+ "pass"+ ", 0"
        #   continue

        # print resp
        y = json.loads(resp)
        # fdns = y["ReportingNameServer"]
        fdns = y[0]["value"]

        if "google" in fdns or "GOOGLE" in fdns:
          ant += 1
          print email + ", 1" + ", " + dom + ", " + fdns
        else:
          print email + ", 0" + ", " + dom + ", " + fdns

except Exception as e:
  print type(e), e
  sys.exit(0)

# save_obj(ans, "ans2")
# print count
# print ant