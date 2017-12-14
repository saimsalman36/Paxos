import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

def phase2A(msg):
	return "2B"

def phase1A(msg):
	return "1B"

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(phase1A, "phase1A")
server.register_function(phase2A, "phase2A")
server.serve_forever()


# =================================