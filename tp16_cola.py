from heap import HeapMax

cola = HeapMax()

# a
cola.arrive("Empleado A", 1)
cola.arrive("Empleado B", 1)
cola.arrive("Empleado C", 1)

# b)
doc = cola.attention()
print(doc[1]) 

# c
cola.arrive("TI 1", 2)
cola.arrive("TI 2", 2)

# d
cola.arrive("Gerente 1", 3)

# e
doc = cola.attention()
print(doc[1])

doc = cola.attention()
print(doc[1])

# f
cola.arrive("Empleado D", 1)
cola.arrive("Empleado E", 1)
cola.arrive("Gerente 2", 3)

# g
while cola.size() > 0:
    doc = cola.attention()
    print(doc[1])
