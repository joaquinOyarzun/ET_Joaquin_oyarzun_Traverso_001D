# ET_Joaquin_oyarzun_Traverso_001D

# Diccionarios iniciales
arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano']
    'FLO4': ['centro mesa ', 'ramo', 'amarillo', 'S', False, 'verano']
}

bodega = {
    'FLO1': [12000, 5],
    'FLO2': [18000, 3],
    'FLO3': [9000, 0]
}

# Validaciones
def validar_codigo(codigo):
    return codigo.strip() != "" and codigo.upper() not in arreglos and codigo.upper() not in bodega

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_tipo(tipo):
    return tipo.strip() != ""

def validar_color(color):
    return color.strip() != ""

def validar_tamaño(tamaño):
    return tamaño in ['S','M','L']

def validar_tarjeta(valor):
    return valor in ['s','n']

def validar_temporada(temp):
    return temp.strip() != ""

def validar_precio(precio):
    return precio > 0

def validar_unidades(unidades):
    return unidades >= 0

# Funciones principales
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe ingresar valores enteros")

def unidades_tipo(tipo):
    total = 0
    for codigo, datos in arreglos.items():
        if datos[1].lower() == tipo.lower():
            total += bodega[codigo][1]
    print("Total unidades disponibles:", total)

def busqueda_precio(p_min, p_max):
    resultados = []
    for codigo, datos in bodega.items():
        precio, unidades = datos
        if p_min <= precio <= p_max and unidades > 0:
            resultados.append(f"{arreglos[codigo][0]}-{codigo}")
    if resultados:
        for r in sorted(resultados):
            print(r)
    else:
        print("No hay arreglos en ese rango de precios")

def buscar_codigo(codigo):
    return codigo.upper() in arreglos

def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo):
        bodega[codigo.upper()][0] = nuevo_precio
        return True
    else:
        return False

def agregar_arreglo(codigo, nombre, tipo, color, tamaño, tarjeta, temporada, precio, unidades):
    if not validar_codigo(codigo):
        print("El código ya existe o es inválido")
        return False
    arreglos[codigo.upper()] = [nombre, tipo, color, tamaño, tarjeta == 's', temporada]
    bodega[codigo.upper()] = [precio, unidades]
    print("Arreglo agregado")
    return True

def eliminar_arreglo(codigo):
    if buscar_codigo(codigo):
        del arreglos[codigo.upper()]
        del bodega[codigo.upper()]
        print("Arreglo eliminado")
        return True
    else:
        print("El código no existe")
        return False

# Menú principal
while True:
    print("\n========== MENU PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("====================================")

    opcion = leer_opcion()

    if opcion == 1:
        tipo = input("Ingrese tipo de arreglo: ")
        unidades_tipo(tipo)
    elif opcion == 2:
        try:
            p_min = int(input("Ingrese precio mínimo: "))
            p_max = int(input("Ingrese precio máximo: "))
            busqueda_precio(p_min, p_max)
        except ValueError:
            print("Debe ingresar valores enteros")
    elif opcion == 3:
        codigo = input("Ingrese código de arreglo: ")
        try:
            nuevo_precio = int(input("Ingrese nuevo precio: "))
            if actualizar_precio(codigo, nuevo_precio):
                print("Precio actualizado")
            else:
                print("El código no existe")
        except ValueError:
            print("Debe ingresar valores enteros")
    elif opcion == 4:
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        tipo = input("Tipo: ")
        color = input("Color principal: ")
        tamaño = input("Tamaño (S/M/L): ")
        tarjeta = input("Incluye tarjeta (s/n): ")
        temporada = input("Temporada: ")
        try:
            precio = int(input("Precio: "))
            unidades = int(input("Unidades: "))
            agregar_arreglo(codigo, nombre, tipo, color, tamaño, tarjeta, temporada, precio, unidades)
        except ValueError:
            print("Debe ingresar valores enteros")
    elif opcion == 5:
        codigo = input("Ingrese código de arreglo: ")
        eliminar_arreglo(codigo)
    elif opcion == 6:
        print("Programa finalizado")
        break
        
