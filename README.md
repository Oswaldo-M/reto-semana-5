# Perfilador de Datasets

Herramienta desarrollada en Python que analiza archivos CSV y genera reportes básicos de calidad de datos.

El programa identifica:
- valores nulos
- valores únicos
- porcentajes de nulidad
- tipos de datos inferidos
- ejemplos de valores por columna

---

## Requisitos

- Python 3.8 o superior

---

## Instalacion

### 1. Clonar el repositorio

```bash
git clone https://github.com/Oswaldo-M/reto-semana-5.git
cd reto-semana-5
```

### 2. Crear ambiente virtual

```bash
python -m venv .venv
```

### 3. Activar ambiente virtual

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Uso

Ejecutar el programa indicando:
- archivo CSV de entrada
- archivo CSV de salida

```bash
python main.py --input <archivo_entrada.csv> --output <archivo_salida.csv>
```

### Ejemplo

```bash
python main.py --input data/ventas.csv --output outputs/perfil_ventas.csv
```

---

## Formato de Salida

El archivo generado contiene las siguientes columnas:

| Columna | Descripcion |
|---|---|
| nombre_columna | Nombre de la columna analizada |
| tipo_inferido | Tipo detectado (numerico, texto, fecha o booleano) |
| total_registros | Cantidad total de registros |
| valores_nulos | Cantidad de valores vacios |
| porcentaje_nulos | Porcentaje de valores nulos |
| valores_unicos | Cantidad de valores diferentes |
| porcentaje_unicos | Porcentaje de unicidad |
| ejemplo_valor | Primer valor no nulo encontrado |

---

## Autor

Oswaldo Morales 