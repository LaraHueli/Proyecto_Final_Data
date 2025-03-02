# Protecto_Final_Data - Análisis de Datos

#### Primera Sesion

## Descripción del Proyecto
Este es un proyecto final donde se trabajará en la transformación, limpieza y análisis de datos. Mi enfoque es hacer una **ETL** (extracción, transformación y carga) utilizando **Python** para la limpieza y transformación de los datos, y luego realizar el análisis y la visualización utilizando **Power BI**.

### Nota de la conversación con Silvia
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
 `sales.csv` → Datos transaccionales de ventas (`SalesID`, `SalesPersonID`, `CustomerID`, `ProductID`, `Quantity`, `Discount`, `TotalPrice`, `SalesDate`, `TransactionNumber`). *(Archivo pesado, disponible en Google Drive).*  
**data_limpios/** → Archivos procesados listos para Power BI  
**src/** → Código fuente en Python para limpieza y transformación  
**jupyters/** → Notebooks para análisis exploratorio  
**documentación/** → Archivo de trabajo  
`.gitignore` → Archivos que no se deben subir al repositorio  
`README.md` → Documento con la descripción del proyecto  
`requirements.txt` → Lista de librerías necesarias  

#### Archivos en data_raw
- **data_raw**: Contiene los siguientes archivos CSV con datos sin procesar:
  - `categories.csv`
  - `cities.csv`
  - `countries.csv`
  - `employees.csv`
  - `products.csv`
  - `customers.csv`
  - `sales.csv` pesa demasiado disponible en descarga desde [Google Drive](https://drive.google.com/file/d/1kjChTjmfu2_TD7GmB4VRy0biWlRjNpdk/view?usp=drive_link).


#### Segunda Sesion

En esta segunda sesión, se procederá a la lectura y exploración de los archivos **uno por uno** con el objetivo de:
- Obtener una visión general de la estructura y contenido de cada dataset.
- Identificar posibles transformaciones necesarias para la limpieza y normalización de datos.
- Evaluar la calidad de los datos, incluyendo tipos de variables, valores nulos y posibles inconsistencias.


# 🚀 **Exploración Inicial del Dataset `categories.csv`**
Se ha realizado una primera exploración del archivo `categories.csv` para entender su estructura y verificar la necesidad de limpieza o transformaciones.

 **Información general:**
- **Número de columnas:** 2 (`CategoryID`, `CategoryName`).
- **Número de filas:** 11.
- **Tipos de datos:**
  - `CategoryID` → `int64` (identificador numérico de categoría).
  - `CategoryName` → `object` (nombre de la categoría en texto).
- **Valores nulos:** No se han encontrado valores nulos en ninguna columna.
- **Ejemplo de valores en `CategoryName`:**
  - `'Confections'`, `'Shell fish'`, `'Cereals'`, `'Dairy'`, `'Beverages'`, ...

✅ **Conclusión:**  
El dataset está limpio y no requiere tratamiento de valores nulos.  
Solo se aplicarán **transformaciones en los nombres de las columnas** para mejorar la legibilidad y estandarización.

---

## **Tareas Pendientes**
Completar el proceso de **ETL** utilizando **Python**.
Crear un **modelo estrella** en **Power BI** para facilitar el análisis.
Implementar y validar el **flujo de trabajo de visualización de datos** en **Power BI**.

---

**Este proyecto está en curso**, y se espera que las próximas fases se centren en la implementación de la **ETL** y en el **análisis con Power BI**. 🚀📊

