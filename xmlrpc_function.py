from xmlrpc.server import SimpleXMLRPCServer
import datetime
import xmlrpc.client
import logging
import os

logging.basicConfig(level=logging.INFO)

def list_contents(dir_name):
	logging.info('list_contents(%s)',dir_name)
	return os.listdir(dir_name)

def is_even(n):
    return n % 2 == 0

def today():
    today = datetime.datetime.today()
    return xmlrpc.client.DateTime(today)

def python_logo():
    with open("python_logo.png", "rb") as handle:
        return xmlrpc.client.Binary(handle.read())

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x // y

server = SimpleXMLRPCServer(("localhost", 8000))


try:
	print("Escuchando el puerto 8000...")
	print ('presiones ctrl+c para salir')
	server.register_function(list_contents, "list_contents")
	server.register_function(is_even, "is_even")
	server.register_function(today, "today")
	server.register_function(python_logo, "python_logo")
	server.register_multicall_functions()
	server.register_function(add, 'add')
	server.register_function(subtract, 'subtract')
	server.register_function(multiply, 'multiply')
	server.register_function(divide, 'divide')
	server.serve_forever()
except KeyboardInterrupt:
	print('saliendo')

"""
from xmlrpc.server import SimpleXMLRPCServer

import logging
import os

logging.basicConfig(level=logging.INFO)

def list_contents(dir_name):
	logging.info('list_contents(%s)',dir_name)
	return os.listdir(dir_name)

def is_even(n):
	return n % 2 == 0

server=SimpleXMLRPCServer(
	('localhost',8000),
	logRequests=True
)


try:
	print ('Esuchando en puerto 8000...')
	print ('presiones ctrl+c para salir')
	server.register_function('listar contenido ',list_contents)
	server.register_function('es par: ',is_even)
	server.serve_forever()
except KeyboardInterrupt:
	print('saliendo')

"""