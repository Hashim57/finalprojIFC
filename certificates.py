import api
from gevent.pywsgi import WSGIServer
import pem
from pem import RSAPrivateKey
from pem import Certificate
import os

Mylist = pem.parse_file(r"key.pem")
if os.path.exists("APIKEY.key") == False:
    for ele in Mylist:
        if isinstance(ele, RSAPrivateKey):
            f = open ("APIKEY.key","w")
            f.write(str(ele))
            f.close()

if os.path.exists("APICERTIFICATE.crt") == False:
    for ele in Mylist:
        if isinstance(ele, Certificate):
            f= open ("APICERTIFICATE.crt","a")
            f.write(str(ele))
            f.close


http_server = WSGIServer(("localhost", 443), keyfile='APIKEY.key', certfile='APICERTIFICATE.crt')
http_server.serve_forever()