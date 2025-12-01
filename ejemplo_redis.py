import redis

# Conexión al servidor Redis o Memurai
r = redis.Redis(host='localhost', port=6379, db=0)

# Insertar datos (clave-valor)
r.set("usuario:004", "Dennis")

# Recuperar el valor
valor = r.get("usuario:004")
print(valor.decode("utf-8"))

# Insertar un hash (estructura tipo diccionario)
r.hset("empleado:004", mapping={"nombre": "Dennis", "edad": "25", "ciudad": "Quito"})

# Obtener todos los campos del hash
print(r.hgetall("empleado:004"))

# Insertar datos (clave-valor)
r.set("usuario:001", "Ana")

# Recuperar el valor
valor = r.get("usuario:001")
print(valor.decode("utf-8"))  # → Ana

# Insertar un hash (estructura tipo diccionario)
r.hset("empleado:001", mapping={"nombre": "Ana", "edad": "25", "ciudad": "Quito"})

# Obtener todos los campos del hash
print(r.hgetall("empleado:001"))