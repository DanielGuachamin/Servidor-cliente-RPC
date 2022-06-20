import xmlrpc.client
import datetime    

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

print(proxy.list_contents('c:'))

print("3 is even: %s" % str(proxy.is_even(3)))

print("100 is even: %s" % str(proxy.is_even(100)))

today = proxy.today()
# convert the ISO8601 string to a datetime object
converted = datetime.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")
print("Today: %s" % converted.strftime("%d.%m.%Y, %H:%M"))

with open("fetched_python_logo.png", "wb") as handle:
    handle.write(proxy.python_logo().data)
print("Imagen guardado exitosamente en la carpeta actual")

multicall = xmlrpc.client.MultiCall(proxy)
multicall.add(7, 3)
multicall.subtract(7, 3)
multicall.multiply(7, 3)
multicall.divide(7, 3)
result = multicall()

print("7+3=%d, 7-3=%d, 7*3=%d, 7//3=%d" % tuple(result))
