# Protecto_Final_Data - Análisis de Datos

## Primera Sesion
### Descripción del Proyecto
Este es un proyecto final donde se trabajará en la transformación, limpieza y análisis de datos. Mi enfoque es hacer una **ETL** (extracción, transformación y carga) utilizando **Python** para la limpieza y transformación de los datos, y luego realizar el análisis y la visualización utilizando **Power BI**.

#### Nota de la conversación con Silvia
Una vez hablado con Silvia, mi intención es hacer una ETL en Python y utilizar Power BI para el análisis y la visualización. He recibido su aprobación para esta estrategia, siempre y cuando utilice Python para la limpieza y transformación de los datos. 
Le he explicado que tengo 7 bases de datos diferentes y que mi objetivo es pasar de un modelo en copo de nieve a un modelo estrella en Power BI y asi poder usar la herramienta en la que me estoy especializando al maximo, sin olvidar el resto.

## Objetivos
### **Objetivos del Análisis**
El análisis de datos se basará en diferentes áreas clave:
#### **Análisis de Ventas**
- Total de ventas por categoría de producto (`sales.csv` + `categories.csv`).
- Descuentos aplicados y su impacto en las ventas (`sales.csv` → `Discount`, `TotalPrice`).
- Productos más vendidos y menos vendidos (`sales.csv` + `products.csv`).
####  **Análisis de Clientes**
- Distribución geográfica de clientes (`customers.csv` + `cities.csv` + `countries.csv`).
- Clientes con más compras (`sales.csv` + `customers.csv`).
- Segmentación de clientes (según frecuencia de compra, monto total gastado).
####  **Análisis de Empleados y Ventas**
- Rendimiento de los empleados en ventas (`sales.csv` + `employees.csv`).
- Tiempo medio de contratación de empleados (`employees.csv` → `HireDate`).
####  **Otros Análisis Interesantes**
- Productos con mayor margen de ganancia (`products.csv` + `sales.csv`).
- Ciudades y países con mayor volumen de ventas (`sales.csv` + `cities.csv` + `countries.csv`).

## 📂 **Estructura del Proyecto**
El proyecto sigue la siguiente organización de carpetas y archivos:
 **data/** → Carpeta principal de los datos  
 **data_raw/** → Archivos CSV sin procesar  
`categories.csv` → Contiene las categorías de productos (`CategoryID`, `CategoryName`).  
 `cities.csv` → Información de ciudades (`CityID`, `CityName`, `Zipcode`, `CountryID`).  
 `countries.csv` → Información de países (`CountryID`, `CountryName`, `CountryCode`).  
 `customers.csv` → Datos de clientes (`CustomerID`, `FirstName`, `LastName`, `CityID`, `Address`).  
 `products.csv` → Detalles de productos (`ProductID`, `ProductName`, `Price`, `CategoryID`, `Class`, `ModifyDate`).  
 `sales.csv` → Datos transaccionales de ventas (`SalesID`, `SalesPersonID`, `CustomerID`, `ProductID`, `Quantity`, `Discount`, `TotalPrice`, `SalesDate`, `TransactionNumber`). 
**data_limpios/** → Archivos procesados listos para Power BI  
**src/** → Código fuente en Python para limpieza y transformación  
**jupyters/** → Notebooks para análisis exploratorio  
**documentación/** → Archivo de trabajo  
`.gitignore` → Archivos que no se deben subir al repositorio  
`README.md` → Documento con la descripción del proyecto  
`requirements.txt` → Lista de librerías necesarias  

## Segunda Sesion
### ETL - Preeliminar

En esta segunda sesión, se procederá a la lectura y exploración de los archivos **uno por uno** con el objetivo de:
- Obtener una visión general de la estructura y contenido de cada dataset.
- Identificar posibles transformaciones necesarias para la limpieza y normalización de datos.
- Evaluar la calidad de los datos, incluyendo tipos de variables, valores nulos y posibles inconsistencias.

### 🚀 **Exploración Inicial del Dataset `categories.csv`**
Se ha realizado una primera exploración del archivo `categories.csv` para entender su estructura y verificar la necesidad de limpieza o transformaciones.
 **Información general:**
- **Número de columnas:** 2 (`CategoryID`, `CategoryName`).
- **Número de filas:** 11.
- **Tipos de datos:**
  - `CategoryID` → `int64` (identificador numérico de categoría).
  - `CategoryName` → `object` (nombre de la categoría en texto).
- **Valores nulos:** No se han encontrado valores nulos en ninguna columna.
✅ **Conclusión:**  
El dataset está limpio y no requiere tratamiento de valores nulos. Solo se aplicarán **transformaciones en los nombres de las columnas** para mejorar la legibilidad y estandarización.


### 🚀 **Exploración Inicial del Dataset `cities.csv`**
Se ha realizado una primera exploración del archivo `cities.csv` para entender su estructura y verificar la necesidad de limpieza o transformaciones.
**Información general:**  
- **Número de columnas:** 4 (`CityID`, `CityName`, `Zipcode`, `CountryID`).  
- **Número de filas:** 96.  
- **Tipos de datos:**  
  - `CityID` → `int64` (identificador único de la ciudad).  
  - `CityName` → `object` (nombre de la ciudad).  
  - `Zipcode` → `int64` (código postal de la ciudad).  
  - `CountryID` → `int64` (identificador del país al que pertenece la ciudad).  
- **Valores nulos:** No se han encontrado valores nulos.  
✅ **Conclusión:**  
El dataset está **completo y sin valores nulos**, pero se aplicarán algunas **transformaciones de limpieza**


### 🚀 **Exploración Inicial del Dataset `countries.csv`**
Se ha realizado una primera exploración del archivo `countries.csv` para entender su estructura y verificar la necesidad de limpieza o transformaciones.
**Información general:**  
- **Número de columnas:** 3 (`CountryID`, `CountryName`, `CountryCode`).  
- **Número de filas:** 206.  
- **Tipos de datos:**  
  - `CountryID` → `int64` (identificador único del país).  
  - `CountryName` → `object` (nombre del país).  
  - `CountryCode` → `object` (código de país de dos o tres letras, según estándar ISO).  
- **Valores nulos:**  **Se encontró 1 valor nulo en `CountryCode`**, mientras que las demás columnas están completas.  
✅ **Conclusión y Acciones de Limpieza:**  El dataset **está casi completo**, pero se realizarán algunas **transformaciones** para mejorar su estructura. 


### 🚀 **Exploración Inicial del Dataset `customers.csv`**
Se ha realizado una primera exploración del archivo `customers.csv` para entender su estructura y verificar la necesidad de limpieza o transformaciones.
 **Información general:**  
- **Número de columnas:** 6 (`CustomerID`, `FirstName`, `MiddleInitial`, `LastName`, `CityID`, `Address`).  
- **Número de filas:** 98,759.  
- **Tipos de datos:**  
  - `CustomerID` → `int64` (identificador único del cliente).  
  - `FirstName` → `object` (nombre del cliente).  
  - `MiddleInitial` → `object` (inicial del segundo nombre, puede estar ausente en algunos casos).  
  - `LastName` → `object` (apellido del cliente).  
  - `CityID` → `int64` (identificador de la ciudad de residencia).  
  - `Address` → `object` (dirección completa del cliente).  
- **Valores nulos:**  **`MiddleInitial` tiene 977 nulos** (`97782` valores no nulos de `98759`).  Las demás columnas están completas.  
✅ **Conclusión y Acciones de Limpieza:**  El dataset **está casi completo**, pero se realizarán algunas **transformaciones** para mejorar su estructura:  


# 🚀 **Exploración Inicial del Dataset `employees.csv`**
Se ha realizado una primera exploración del archivo `employees.csv` para entender su estructura y verificar la necesidad de limpieza o transformaciones.
**Información general:**  
- **Número de columnas:** 8 (`EmployeeID`, `FirstName`, `MiddleInitial`, `LastName`, `BirthDate`, `Gender`, `CityID`, `HireDate`).  
- **Número de filas:** 23.  
- **Tipos de datos:**  
  - `EmployeeID` → `int64` (identificador único del empleado).  
  - `FirstName` → `object` (nombre del empleado).  
  - `MiddleInitial` → `object` (inicial del segundo nombre del empleado).  
  - `LastName` → `object` (apellido del empleado).  
  - `BirthDate` → `object` (fecha de nacimiento, almacenada como string con formato `YYYY-MM-DD HH:MM:SS.sss`).  
  - `Gender` → `object` (género del empleado).  
  - `CityID` → `int64` (identificador de la ciudad donde reside el empleado).  
  - `HireDate` → `object` (fecha de contratación, almacenada como string con formato `YYYY-MM-DD HH:MM:SS.sss`).  
- **Valores nulos:**  No se han encontrado valores nulos en ninguna columna.  
✅ **Conclusión y Acciones de Limpieza:**  El dataset **está completo y sin valores nulos**, pero se realizarán algunas **transformaciones** para mejorar su estructura y facilitar su análisis:  

# 🚀 **Exploración Inicial del Dataset `products.csv`**
Se ha realizado una primera exploración del archivo `products.csv` para entender su estructura y verificar la necesidad de limpieza o transformaciones.
**Información general:**  
- **Número de columnas:** 9 (`ProductID`, `ProductName`, `Price`, `CategoryID`, `Class`, `ModifyDate`, `Resistant`, `IsAllergic`, `VitalityDays`).  
- **Número de filas:** 452.  
- **Tipos de datos:**  
  - `ProductID` → `int64` (identificador único del producto).  
  - `ProductName` → `object` (nombre del producto).  
  - `Price` → `float64` (precio del producto).  
  - `CategoryID` → `int64` (identificador de la categoría del producto).  
  - `Class` → `object` (clasificación del producto).  
  - `ModifyDate` → `object` (fecha de última modificación, requiere conversión a formato `datetime`).  
  - `Resistant` → `object` (nivel de resistencia del producto, valores incluyen `Durable`, `Weak`, `Unknown`).  
  - `IsAllergic` → `object` (indica si el producto es alergénico, valores incluyen `True`, `False`, `Unknown`).  
  - `VitalityDays` → `float64` (número de días que el producto mantiene su vitalidad o frescura, aunque debería ser un número entero).  
- **Valores nulos:** No se han encontrado valores nulos, pero las columnas `Resistant` e `IsAllergic` contienen valores `"Unknown"` que podrían requerir tratamiento.  
✅ **Conclusión y Acciones de Limpieza:**  El dataset **está completo**, pero se realizarán algunas **transformaciones** para mejorar su estructura:  

# 🚀 **Exploración Inicial del Dataset `sales.csv`**
Se ha realizado una primera exploración del archivo `sales.csv` para entender su estructura y verificar la necesidad de limpieza o transformaciones.
**Información general:**  
- **Número de columnas:** 9 (`SalesID`, `SalesPersonID`, `CustomerID`, `ProductID`, `Quantity`, `Discount`, `TotalPrice`, `SalesDate`, `TransactionNumber`).  
- **Número de filas:** 6,758,125.  
- **Tipos de datos:**  
  - `SalesID` → `int64` (identificador único de la venta).  
  - `SalesPersonID` → `int64` (identificador del vendedor).  
  - `CustomerID` → `int64` (identificador del cliente).  
  - `ProductID` → `int64` (identificador del producto vendido).  
  - `Quantity` → `int64` (cantidad de productos vendidos).  
  - `Discount` → `float64` (descuento aplicado en la venta).  
  - `TotalPrice` → `float64` (precio total de la venta después del descuento).  
  - `SalesDate` → `object` (fecha de la venta, requiere conversión a formato `datetime`).  
  - `TransactionNumber` → `object` (código único de transacción, se evaluará si es realmente necesario).  
- **Valores nulos:**  **`SalesDate` tiene valores nulos**, lo que requiere tratamiento.  El resto de las columnas están completas.  
✅ **Conclusión y Acciones de Limpieza:**  El dataset **es extenso y mayormente completo**, pero se realizarán algunas **transformaciones** para mejorar su estructura y optimizar su análisis.

## Tercera Sesión
### Limpieza y transformación  

En esta tercera sesión, se procederá a la limpieza y transformación de los archivos **uno por uno**.  

#### categories.csv:  
- Se limpiaron los nombres de columnas → `Category_Id`, `Category_Name`.  
- Se verificaron valores únicos.  
- Se generó `describe().T` para analizar datos numéricos.  
- Se guardó el dataset limpio en `data_limpios/`.  

#### cities.csv:  
- Se limpiaron los nombres de columnas → `City_Id`, `City_Name`, `Zipcode`.  
- Se verificaron valores únicos y duplicados en `City_Id` y `City_Name`.  
- Se eliminó la columna `CountryID` (tenía siempre el mismo valor).  
- Se convirtió `Zipcode` a `str` (código postal como identificador).  
- Se guardó el dataset limpio en `data_limpios/`.  

#### countries.csv:
- Se limpiaron los nombres de columnas → Country_Id, Country_Name, Country_Code
- Se verificaron duplicados en CountryID, CountryName y CountryCode
- Se normalizaron los nombres de los países (eliminando espacios y pasando a minúsculas)
- Se identificó un valor nulo en CountryCode para Australia, pero no se modificó por el momento
- Se guardó el dataset limpio en data_limpios/

#### customers.csv:
- Se eliminó la columna MiddleInitial porque no aportaba valor
- Se limpiaron los nombres de columnas → Customer_Id, First_Name, Last_Name, City_Id, Address
- Se concatenaron las columnas First_Name y Last_Name en Full_Name y se eliminó First_Name y Last_Name
- Se guardó el dataset limpio en data_limpios/


#### Script de limpieza:
Se creó el script sp_limpieza.py en la carpeta src, con las siguientes funciones:
- Limpiar_nombres_columnas(df): Normaliza los nombres de las columnas eliminando espacios, caracteres especiales y aplicando formato estandarizado.
- Valores_unicos(df): Muestra los valores únicos de cada columna del DataFrame.
- Concatenar_nombres(df): Concatena First_Name y Last_Name en Full_Name, posicionándola después de Customer_Id y eliminando las columnas originales.



## **Tareas Pendientes**
Completar el proceso de **ETL** utilizando **Python**.
Crear un **modelo estrella** en **Power BI** para facilitar el análisis.
Implementar y validar el **flujo de trabajo de visualización de datos** en **Power BI**.

---

**Este proyecto está en curso**, y se espera que las próximas fases se centren en la implementación de la **ETL** y en el **análisis con Power BI**. 🚀📊

