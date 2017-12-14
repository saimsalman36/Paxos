import xmlrpclib
proxy = xmlrpclib.ServerProxy("http://localhost:8000/")

print str(proxy.phase1A("msg"))
print str(proxy.phase2A("msg"))