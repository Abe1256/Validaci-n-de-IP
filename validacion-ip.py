# Función para comprobar la validez de una dirección IP
def es_ip_valida(ip):
    segmentos = ip.split('.')
    
    if len(segmentos) != 4:
        return False
    
    for segmento in segmentos:
        if not segmento.isdigit() or not 0 <= int(segmento) <= 255:
            return False
            
    return True

# Función para identificar la clase de la IP según su primer segmento
def clase_ip(ip):
    segmentos = ip.split('.')
    primero = int(segmentos[0])
    
    if 1 <= primero <= 126:
        return 'A'
    elif 128 <= primero <= 191:
        return 'B'
    elif 192 <= primero <= 223:
        return 'C'
    elif 224 <= primero <= 239:
        return 'D'
    elif 240 <= primero <= 255:
        return 'E'
    else:
        return 'Clase desconocida'

# Función principal para manejar la interacción con el usuario
def ejecutar():
    ip = input("Por favor, ingresa una dirección IP: ")
    
    if es_ip_valida(ip):
        clase = clase_ip(ip)
        print(f"La dirección IP {ip} es válida y pertenece a la clase {clase}.")
    else:
        print("La dirección IP ingresada no es válida.")

if __name__ == "__main__":
    ejecutar()
