import sys 


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
    

def perfilar_columna(nombre,valores):
    
    total = len(valores)
    nulos = 0

    for valor in valores:
        if es_valor_nulo(valores):
            nulos+=1

    valores_no_nulos = []

    for valor in valores:
        if not es_valor_nulo:
            valores_no_nulos.append(valor)
    
    unicos = len(set(valores_no_nulos))

    if len(valores_no_nulos>0):
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



