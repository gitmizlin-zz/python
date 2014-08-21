#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Execute a .py-file that has the same filename as this file. 
A file hello.cgi will execute the file hello.py and wrap its
output with a HTTP header to be able to display the output as 
a webpage. 

"""

import sys
import cgitb
import os

def enc_print(string='', encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')

cgitb.enable()    


#enc_print("Content-Type: text/plain")
#enc_print("")

print("Content-Type: text/plain")
print("")

print("""
<!doctype html>
<meta charset="utf-8">
<title>Min me-sida</title>
<pre>
Min Me-sida
==============================================================================

Hej, 

Jag heter Mikael Roos och är lärare på denna kurs i Python. 
          ,     ,
         (\____/)
          (_oo_)
            (O)
          __||__    \)
       []/______\[] /
       / \______/ \/
      /    /__\ 
     (\   /____\ 

Detta är min me-sida i kursen. Denna sidan innehåller en presentation av mig
själv. Underhåll denna sidan under hela kursen och uppdatera den efter hand
och behov.

Så, en presentation en bra början. Skriv några ord om dig själv. Jag börjar.

Mitt namn är Mikael Roos. Född och uppvuxen i Bankeryd, Småland, strax utanför
Jönköping, i ett villaområde som byggdes upp samtidigt som vi flyttade in där.
En längre historia om mig finns att läsa i min me-sida för kursen oophp. Du 
når den via länken:
http://dbwebb.se/oophp/me/kmom01/me.php


Om jag skall nämna någon hobby, förutom webbprogrammering, så får det bli att
bära sten på sommarstugetomten, och det finns sten så det räcker ett par 
livstider. Till och från får jag för mig att börja på lite hobbies, ett år 
satsade jag på pokerspel, ett annat år var det geocaching. 

Årets hobby är Turfing:
http://dbwebb.se/blogg/forsmak-infor-hosten-2014#hobby

Vi syns och hörs i forum och chatt!

</pre>
""")