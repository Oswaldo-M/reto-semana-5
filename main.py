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

    
