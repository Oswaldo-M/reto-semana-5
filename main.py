import sys 
import argparse

#Checa si un valor es nulo
def es_valor_nulo(valor):
    if valor is None:
        return True
    
    if isinstance(valor, str) and valor.strip()== "":
        return True
    
    return False


#Checa si un valor es numerico
def es_valor_numerico(valor):
    try: 
        float(str(valor).replace(',', '').strip())
        return True
    except (ValueError,TypeError):
        return False
    
def es_fecha(valor):
    v = str(valor).strip()
    if len(v) >= 10 and v[4] == '-' and v[7] == '-':
        try:
            partes = v[:10].split('-')
            anio, mes, dia = int(partes[0]), int(partes[1]), int(partes[2])
            return 1900 <= anio <= 2030 and 1<= mes <= 12 and 1 <= dia <= 31
        except (ValueError,TypeError):
            pass
    return False

def es_booleano(valor):
    v = str(valor).strip().lower()
    return v in ['true','false','yes','no','si','1','0','t','f']



#Infiere el tipo de dato de una columna 
def inferir_tipo(valores):

    valores_validos = []

    for v in valores:
        if not es_valor_nulo(v):
            valores_validos.append(v)

    if not valores_validos:
        return "texto"
    
    total = len(valores_validos)
    umbral = 0.8

    num_fechas = sum(1 for v in valores_validos if es_fecha(v))
    num_booleanos = sum(1 for v in valores_validos if es_booleano(v))
    num_numericos = sum(1 for v in valores_validos if es_valor_numerico(v))
    
    if num_fechas / total >= umbral:
        return "fecha"
    elif num_booleanos / total >= umbral:
        return "booleano"
    elif num_numericos / total >= umbral:
        return "numerico"
    else:
        return "texto"
    
#Genera el perfil de una columna 
def perfilar_columna(nombre,valores):
    
    total = len(valores)
    nulos = 0

    for valor in valores:
        if es_valor_nulo(valor):
            nulos+=1

    valores_no_nulos = []

    for valor in valores:
        if not es_valor_nulo(valor):
            valores_no_nulos.append(valor)
    
    unicos = len(set(valores_no_nulos))

    if len(valores_no_nulos)>0:
        ejemplo = valores_no_nulos[0]
    else:
        ejemplo= ""

    tipo = inferir_tipo(valores)

    porc_nulos = round(nulos / total * 100, 2) if total > 0 else 0.00
    porc_unicos = round(unicos / total * 100, 2) if total > 0 else 0.00

    return {
        "nombre_columna": nombre,
        "tipo_inferido": tipo,
        "total_registros": total,
        "valores_nulos": nulos,
        "porcentaje_nulos": porc_nulos,
        "valores_unicos": unicos,
        "porcentaje_unicos": porc_unicos,
        "ejemplo_valor": ejemplo
    }

def leer_csv(ruta):
    with open(ruta, 'r',encoding='utf-8') as r:
        lineas = r.readlines()

    if not lineas:
        return [], []
    
    encabezados = lineas[0].strip().split(',')

    filas = []

    for linea in lineas[1:]:
        linea = linea.strip()
        if linea != "":
            partes = linea.split(',')
            filas.append(partes)
    return encabezados, filas


def escribir_csv(ruta, perfiles):
    """Escribe el CSV de perfiles."""
    columnas = [
        "nombre_columna", "tipo_inferido", "total_registros",
        "valores_nulos", "porcentaje_nulos", "valores_unicos",
        "porcentaje_unicos", "ejemplo_valor"
    ]
    
    with open(ruta, 'w', encoding='utf-8') as f:
        f.write(','.join(columnas) + '\n')
        
        for p in perfiles:
            valores = [
                str(p["nombre_columna"]),
                str(p["tipo_inferido"]),
                str(p["total_registros"]),
                str(p["valores_nulos"]),
                f"{p['porcentaje_nulos']:.2f}",
                str(p["valores_unicos"]),
                f"{p['porcentaje_unicos']:.2f}",
                str(p["ejemplo_valor"])
            ]
            f.write(','.join(valores) + '\n')

def main():
    # Parsear argumentos
    parser = argparse.ArgumentParser(
        description="Perfilador de Datasets CSV"
    )
    parser.add_argument("--input", "-i", required=True, 
                        help="Ruta al CSV de entrada")
    parser.add_argument("--output", "-o", required=True,
                        help="Ruta al CSV de salida")
    
    args = parser.parse_args()
    
    print(f"Perfilando: {args.input}")
    
    # Leer CSV
    try:
        encabezados, filas = leer_csv(args.input)
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo {args.input}")
        sys.exit(1)
    
    if not encabezados:
        print("Error: El archivo esta vacio")
        sys.exit(1)
    
    print(f"Columnas encontradas: {len(encabezados)}")
    print(f"Registros: {len(filas)}")
    
   # Perfilar cada columna
    perfiles = []

    for i in range(len(encabezados)):
        nombre_columna = encabezados[i]
        valores = []

        for fila in filas:
            if i < len(fila):
                valores.append(fila[i])
            else:
                valores.append("")
        perfil = perfilar_columna(nombre_columna, valores)
        perfiles.append(perfil)
    
    # Escribir resultado
    escribir_csv(args.output, perfiles)
    print(f"Perfil guardado en: {args.output}")
    print("Completado!")


if __name__ == "__main__":
    main()
