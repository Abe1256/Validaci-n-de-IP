# Validación y Clasificación de Direcciones IP

Este programa permite comprobar la validez de una dirección IP y clasificarla en una de las clases estándar (A, B, C, D o E). Es ideal para aprender sobre el funcionamiento de las direcciones IP en redes informáticas.

## Descripción del funcionamiento

El programa está compuesto por tres funciones principales:

1. **`es_ip_valida(ip)`**:  
   Comprueba si una dirección IP ingresada es válida.  
   - Divide la IP en segmentos separados por puntos (`.`).
   - Verifica que cada segmento es un número entre 0 y 255.
   - Devuelve `True` si la IP es válida, y `False` en caso contrario.

2. **`clase_ip(ip)`**:  
   Determina la clase de la dirección IP basándose en el primer segmento.  
   - Clase A: Primer segmento entre 1 y 126.  
   - Clase B: Primer segmento entre 128 y 191.  
   - Clase C: Primer segmento entre 192 y 223.  
   - Clase D: Primer segmento entre 224 y 239. (Multidifusión).  
   - Clase E: Primer segmento entre 240 y 255. (Reservada).  

3. **`ejecutar()`**:  
   Función principal que interactúa con el usuario.  
   - Solicita al usuario que ingrese una dirección IP.  
   - Comprueba su validez usando `es_ip_valida`.  
   - Si es válida, determina y muestra su clase usando `clase_ip`.  
   - Si no es válida, muestra un mensaje de error.

## Requisitos

El programa está escrito en Python y no depende de librerías externas. Solo necesitas tener Python 3 instalado en tu sistema.

## Ejecución

Sigue estos pasos para ejecutar el programa:

1. Descarga o copia el código fuente en un archivo llamado `ip_validador.py`.

2. Abre una terminal y navega al directorio donde guardaste el archivo.

3. Ejecuta el programa con el siguiente comando:
   ```bash
   python ip_validador.py
   ```

4. Introduce una dirección IP cuando se te solicite.

## Ejemplo de uso

### Entrada válida:
```bash
Por favor, ingresa una dirección IP: 192.168.1.1
La dirección IP 192.168.1.1 es válida y pertenece a la clase C.
```

### Entrada inválida:
```bash
Por favor, ingresa una dirección IP: 300.168.1.1
La dirección IP ingresada no es válida.
```

## Notas adicionales

- Las direcciones IP válidas deben tener exactamente cuatro segmentos separados por puntos (`.`).
- Los segmentos deben ser números enteros entre 0 y 255.
