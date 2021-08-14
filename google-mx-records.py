#!/usr/bin/python
import sys

if len(sys.argv) < 2:
  print("""
  create a DNS zone record for Google's MX settings
  crafted by John Martinelli (john@ISRD.com)

  simply execute "./mx.py domain.com > zone.txt"
  and upload zone.txt in your DNS manager to configure Gmail on your domain""")
  quit()
elif len(sys.argv) > 1:
  zoneRecord = ";; MX Records\n\
DOMAIN.	1	IN	MX	10 alt4.aspmx.l.google.com.\n\
DOMAIN.	1	IN	MX	10 alt3.aspmx.l.google.com.\n\
DOMAIN.	1	IN	MX	5 alt2.aspmx.l.google.com.\n\
DOMAIN.	1	IN	MX	5 alt1.aspmx.l.google.com.\n\
DOMAIN.	1	IN	MX	1 aspmx.l.google.com."
  newMX = zoneRecord.replace("DOMAIN", str(sys.argv[1]))
  print(newMX)
