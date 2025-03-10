# Protecto_Final_Data - Análisis de Datos

## Primera Sesión
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

## Segunda Sesión
### ETL - Preeliminar

En esta segunda sesión, se procederá a la lectura y exploración de los archivos **uno por uno** con el objetivo de:
- Obtener una visión general de la estructura y contenido de cada dataset.
- Identificar posibles transformaciones necesarias para la limpieza y normalización de datos.
- Evaluar la calidad de los datos, incluyendo tipos de variables, valores nulos y posibles inconsistencias.

###  **Exploración Inicial del Dataset `categories.csv`**
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


### **Exploración Inicial del Dataset `cities.csv`**
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


### **Exploración Inicial del Dataset `countries.csv`**
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


### **Exploración Inicial del Dataset `customers.csv`**
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


###  **Exploración Inicial del Dataset `employees.csv`**
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

### **Exploración Inicial del Dataset `products.csv`**
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

### **Exploración Inicial del Dataset `sales.csv`**
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
- Se limpiaron los nombres de columnas → `Country_Id`, `Country_Name`, `Country_Code`.
- Se verificaron duplicados en `Country_Id`, `Country_Name` y `Country_Code`.
- Se normalizaron los nombres de los países (eliminando espacios y pasando a minúsculas).
- Se identificó un valor nulo en `Country_Code` para Australia, pero no se modificó por el momento.
- Se guardó el dataset limpio en `data_limpios/`.

#### customers.csv:
- Se eliminó la columna `MiddleInitial` porque no aportaba valor.
- Se limpiaron los nombres de columnas → `Customer_Id`, `First_Name`, `Last_Name`, `City_Id`, `Address`.
- Se concatenaron las columnas `First_Name` y `Last_Name` en `Full_Name`, eliminando las originales.
- Se guardó el dataset limpio en `data_limpios/`.


#### employees.csv:
- Se eliminó la columna `MiddleInitial` porque no aportaba valor.
- Se limpiaron los nombres de columnas → `Employee_Id`, `Full_Name`, `Birth_Date`, `Gender`, `City_Id`, `Hire_Date`.
- Se concatenaron las columnas `First_Name` y `Last_Name` en `Full_Name`, eliminando las originales.
- Se convirtieron las fechas `BirthDate` y `HireDate` a formato `YYYY-MM-DD`.
- Se calculó la edad (`Age`) a partir de `BirthDate`.
- Se calculó la antigüedad (`YearsInCompany`) a partir de `HireDate`.
- Se guardó el dataset limpio en `data_limpios/`.
**Análisis de `describe()`**
- **Edad (`Age`)**:Rango de edad: 36 a 74 años. Promedio: 57 años. El 50% de los empleados tienen entre 51 y 63 años.
- **Años en la empresa (`YearsInCompany`)**: Rango: 8 a 15 años. Promedio: 11.8 años. El 50% de los empleados tienen entre 10.5 y 14 años en la empresa.
**Conclusiones:**
- La empresa tiene una plantilla mayormente **senior**, con edades promedio de 57 años.
- La mayoría de los empleados tienen más de 10 años de antigüedad, lo que sugiere una buena retención laboral.
- Se recomienda analizar la distribución de edades en Power BI para evaluar la planificación de talento y sucesión.

#### products.csv:
- Se limpiaron los nombres de columnas con `limpiar_nombres_columnas()`, manteniendo el contenido original.  
- Se convirtió la columna `Modify_Date` a formato `YYYY-MM-DD`.  
- Se reemplazó `"Unknown"` por `"Unspecified"` en `Resistant` e `Is_Allergic` para facilitar el análisis en Power BI.  
- Se convirtió `Vitality_Days` de `float` a `int`.  
- Se analizaron los valores con `describe()` y se identificaron posibles valores extremos en `Price` y `Vitality_Days`.  
- Se generaron gráficos (histograma y boxplot) para evaluar su distribución y detectar outliers.  
- Se analizaron los productos con `Vitality_Days = 0`, identificando sus categorías y clases. 
- Se guardó el dataset limpio en `data_limpios/`. 
**Análisis de `describe()`**  
- **Price**: Rango de valores entre 0.0449 y 99.87. Distribución normal sin valores extremos preocupantes.  
- **Vitality_Days**: Rango de 0 a 120 días. Se detectaron valores en 0, analizados por categoría y clase.  
**Conclusiones:**  
- La mayoría de los productos con `Vitality_Days = 0` pertenecen a clases `Medium` y `High`, con categorías diversas.  
- No se detectaron valores atípicos en `Price`, por lo que no se realizaron modificaciones.  
- Se recomienda analizar en Power BI la distribución de `Vitality_Days` y su relación con las categorías de productos.  

#### **sales.csv:**
- Se verificaron los valores nulos en la columna `SalesDate` y se decidió eliminar los valores nulos (1%) para mantener la consistencia de los datos.
- Se limpiaron los nombres de columnas con `limpiar_nombres_columnas()`, estandarizando los nombres de las columnas.
- Se separaron las fechas en dos nuevas columnas: `Day_Sales` (con solo la fecha) y `Hour_Sales` (con solo la hora) para facilitar su análisis en Power BI.
- Se determinó que las columnas `SalesID` y `Transaction_Number` eran redundantes, por lo que se eliminó `Transaction_Number`.
- Se analizó el dataset con `describe()` y se encontraron valores típicos en las columnas como `Quantity` y `SalesID`.
- Se guardó el dataset limpio en `data_limpios/`.
**Análisis de `describe()`**
- **SalesID**: Rango de valores entre 1 y 6758125.
- **TotalPrice**: Todos los valores son 0, no se realizaron modificaciones.
- **Quantity**: Valores típicos de productos vendidos entre 7 y 25.
**Conclusiones:**
- Se eliminaron los valores nulos de `SalesDate` para asegurar la consistencia del dataset.
- Los nombres de las columnas fueron estandarizados.
- La separación de las fechas en `Day_Sales` y `Hour_Sales` permite explorar más fácilmente las tendencias de ventas por hora en Power BI.
- Se eliminó `Transaction_Number` ya que era redundante con `SalesID`.


#### Script de limpieza:
Se creó el script sp_limpieza.py en la carpeta src, con las siguientes funciones:
- Limpiar_nombres_columnas(df): Normaliza los nombres de las columnas eliminando espacios, caracteres especiales y aplicando formato estandarizado.
- Valores_unicos(df): Muestra los valores únicos de cada columna del DataFrame.
- Concatenar_nombres(df): Concatena First_Name y Last_Name en Full_Name, posicionándola después de Customer_Id y eliminando las columnas originales.
- limpiar_fechas(df): Para eliminar la horas de la fechas y dejar solo formato fecha
- calcular_edad (df): Partiendo de la fecha de nacimiento sacamos la edad actual
- años_trabajados (df): partiendo de la fecha de contratacion sacamos los años trabajados.
- convertir_a_entero (df): Convierte un numero float a int.
- separar_fecha_hora (df) : partiendo de la fecha de compra, sacamos dia y hora.


#### Script de visualizacion:
Se creó el script sp_visualizacion.py en la carpeta src, con las siguientes funciones:
- graficar_histograma (df): Genera un histograma para visualizar la distribución de una variable.
- graficar_boxplot(df): Genera un boxplot para identificar outliers.



## Cuarta Sesión
### Power BI  

Este documento detalla todos los pasos realizados en **Power BI** hasta el momento, desde la carga de datos hasta la optimización del modelo y las tablas.  
## Fase 1: Carga de Datos  
### **Importación de Datos**  
- Se importaron los archivos **limpios** desde la carpeta `data_limpios/` a Power BI.  
- Se verificó la estructura y calidad de los datos antes de proceder a modelarlos.  

## Fase 2: Transformación del Modelo de Datos  
### **Conversión de Copo de Nieve a Modelo Estrella**  
- Se estableció `sales_clean` como la **tabla de hechos** y el resto como **tablas de dimensión**.  
- Se corrigieron y crearon **relaciones 1:* (uno a muchos)** para optimizar la estructura.  
- Se realizaron **agregaciones y combinaciones de consultas** en Power Query para mejorar el modelo.  
#### **Agrupación y Combinación de Consultas**  
- **`customers_clean`** se combinó con **`cities_clean`** a través de `City_Id` para simplificar la estructura.  
- **`products_clean`** se combinó con **`categories_clean`** a través de `Category_Id` para reducir el número de tablas en el modelo.  
- **Deshabilitación de carga de `cities_clean` y `categories_clean`** para mejorar la eficiencia del modelo.  
- **Corrección en `cities_clean` en Python**, donde se restauró una columna eliminada por error.  
- **Revisión y ajuste de tipos de datos en todas las tablas** en Power Query.  

## Fase 3: Relaciones en Power BI  
### **Relaciones Establecidas en el Modelo Estrella**  
 **Tabla de Hechos (`sales_clean`)**  
- Se conecta con `products_clean` mediante **`Product_Id`**.  
- Se conecta con `employees_clean` mediante **`Employee_Id`** *(anteriormente `Sales_Person_Id`)*.  
- Se conecta con `customers_clean` mediante **`Customer_Id`**.  
 **Dimensiones con Relaciones Internas**  
- `customers_clean` incluye información de `cities_clean` (ciudad y código postal).  
- `products_clean` incluye información de `categories_clean` (nombre de categoría).  

## Fase 4: Optimización y Preparación para Visualización   
✅ **Limpieza y Optimización de `sales_clean`**  
- **`Discount`** convertido a decimal y multiplicado por 100 para representarlo como porcentaje.  
- **Eliminación de columnas innecesarias:**  
  - ❌ `Hour_Full` (ya tenemos `Hour_Sales`).  
  - ❌ `Total_Price` (siempre estaba en 0).  
- **Reorganización de columnas** para mejorar la interpretación de los datos.  

✅ **Limpieza y Optimización de `products_clean`**  
- **Corrección del formato de precios** → Volvimos a **Python** para verificar y corregir valores.  
- **Confirmación de que podemos calcular `Total_Ventas` en Power BI** con:  
  ```DAX
  Total_Ventas = SUMX(sales_clean, sales_clean[Quantity] * RELATED(products_clean[Price]))

✅ **Limpieza y Optimización de `employees_clean`**
- **Reorganización de columnas** para mejorar la interpretación de los datos.   
**Corrección de Tipos de Datos**  
- `Employee_Id`, `City_Id`, `Years_Worked`, `Age` → **Numérico (entero)**.  
- `Full_Name`, `Gender`, `Work_Category` → **Texto**.  
- `Birth_Date`, `Hire_Date` → **Fecha**.  
**Renombre de Columnas**: `Edad` → **`Age`**. `Años Trabajados` → **`Years_Worked`**. `Categoría Laboral` → **`Work_Category`**.  
**Nueva Columna: `Work_Category`** : Clasificación de empleados según `Years_Worked`:  
- 🟢 **Junior** → ≤5 años.  
- 🔵 **Mid-Level** → 6-10 años.  
- 🔴 **Senior** → >10 años.  
**Método de Creación:**  
- Se utilizó una **columna condicional en Power Query** basada en `Years_Worked`.  

# ✅ Limpieza y Optimización de `customers_clean`
- **Unión de `customers` con `cities` y `countries`** usando `City_Id` para traer el nombre de la ciudad y el país.  
- **Eliminación de columnas innecesarias:**  
  - ❌ `City_Id` (porque ya tenemos el nombre de la ciudad).  
  - ❌ `Country_Id` (porque ya tenemos el nombre del país).  
- **Reorganización de columnas** para mejorar la interpretación de los datos.  
---
## Quinta Sesión
### Power BI  

## Hoja 1: Ventas / Rentabilidad  
### Análisis Realizado  
 **Total de Productos Vendidos (87 millones) y Ventas Totales ($4.02 billones)**  
   - Se ha vendido un volumen alto de productos, lo que indica una **alta demanda**.  
   - Falta contexto temporal para saber si las ventas **están creciendo o son estables**.  
 **Variación de Precio de Venta ($99.83 mil) y Precio Promedio de Venta ($46.3 mil)**  
   - Existen **diferencias significativas** entre los productos más baratos y más caros.  
   - Se identificó la presencia de productos **premium y económicos**, lo que sugiere una segmentación de precios en el mercado.  
 **Productos Más Vendidos (Ranking por cantidad de unidades vendidas)**  
   - Los productos con mayor demanda son **Longos - Chicken Wings y Yoghurt Tubes**.  
   - Sin embargo, **tener alta demanda no significa que sean los más rentables**.  
 **Productos con Mayor Ingreso (Ranking por ventas totales en dólares)**  
   - **Apricots - Dried y Yoghurt Tubes** generan los mayores ingresos.  
   - Algunos productos con menos unidades vendidas **tienen precios altos y generan más ingresos**.  
###  Hallazgos Clave  
**Diferenciar entre volumen de ventas e ingresos es clave para definir estrategias comerciales.**  
**Se necesita analizar márgenes de ganancia por producto para identificar oportunidades de optimización.**  
**Es importante considerar descuentos y promociones estratégicas para mejorar rentabilidad.**  
---

##  Hoja 2: Categoría / Producto  
### Análisis Realizado  
 **Ventas Totales por Categoría**  
   - **Confections y Meat** son las categorías con mayores ingresos, con más de **$500M cada una**.  
   - Las categorías **Grain y Shell Fish** tienen los ingresos más bajos.  
 **Ventas Totales por Producto**  
   - El producto con mayor facturación es **Beef - Texas Style Burger ($17.65B)**.  
   - Se destacan productos con precios altos, como **Chestnuts - Whole, Canned y Eggplant - Asian**.  
**Comparación de Precio Unitario vs Total Price**  
   - Algunos productos de precio alto generan más ingresos a pesar de venderse en menor volumen.  
   - Se detectó una **fuerte relación entre el precio unitario y la rentabilidad total** de ciertos productos premium.  
###  Hallazgos Clave  
**No siempre los productos con mayor volumen de ventas son los más rentables.**  
**Se recomienda analizar márgenes de ganancia por categoría para optimizar la rentabilidad.**  
**Podría ser útil estudiar estrategias de precios dinámicos para mejorar ingresos.**  
---

## Hoja 3: Clientes  
###  Análisis Realizado  
**Total Clientes: 98.76 mil** → Mercado amplio, pero falta evaluar retención y recurrencia.  
**Clientes VIP (17.2%)** → Representan **76.42% de las compras**, mostrando su alto valor.  
**Frecuencia de Compra** → Mayoría de clientes son **Ocasionales (≤ 50 compras)**, mientras que pocos superan **80 compras**.  
**Distribución Geográfica** → Alta concentración en **Norteamérica, Europa y Oceanía**, con baja presencia en África y Sudamérica.  
**El 80/20 del negocio:** La mayor parte de las ventas proviene de un grupo reducido de clientes.  
**Desafío:** Mantener y expandir la base de clientes VIP sin descuidar el crecimiento de los clientes ocasionales.  
### Hallazgos Clave  
 **Los clientes VIP generan la mayor parte del ingreso** → Se deben fidelizar con estrategias exclusivas.  
 **El segmento de menor consumo es una oportunidad** → Se pueden incentivar compras recurrentes con promociones.  
 **Análisis geográfico** → Evaluar si la baja presencia en ciertas regiones es una limitación o una oportunidad de expansión.  isis geográfico puede ayudar a definir estrategias de crecimiento en ubicaciones estratégicas.**  
---

## Organización de Medidas en Power BI  
Para mejorar la accesibilidad dentro de Power BI, las medidas fueron organizadas en **subcarpetas**:  
 **Clientes**  
   - **Clientes con más compras**  
   - **Frecuencia de Compra**  
   - **Segmentación de Clientes**  
   - **Distribución Geográfica**  
 **Ventas y Rentabilidad**  
   - **Total de Ventas**  
   - **Cantidad de Productos Vendidos**  
   - **Precio Promedio de Venta**  
   - **Variación de Precio de Venta**  
   - **Producto Más Caro / Más Barato**  
 **Desempeño por Categoría y Producto**  
   - **Ventas por Categoría**  
   - **Ventas por Producto**  
   - **Comparación de Precio Unitario vs Total Price**  

📌 **Beneficios de la Organización**  
🔹 **Permite una búsqueda rápida y eficiente de medidas en Power BI.**  
🔹 **Reduce el desorden en el modelo de datos y mejora la estructura del análisis.**  

---

## 🔜 Próximos Pasos  
📌 **Optimización del dashboard para mejorar la experiencia visual.**  
📌 **Análisis de la rentabilidad de clientes y estrategias de fidelización.**  
📌 **Incorporación de filtros dinámicos para segmentación más detallada.**  

🔎 **Estado del Proyecto:**  
✅ **ETL completada en Power Query (Limpieza y Transformación).**  
✅ **Modelo de Datos estructurado con relaciones correctas.**  
✅ **Medidas organizadas en subcarpetas para mejor accesibilidad.**  
📊 **Dashboards en desarrollo con métricas clave.**  

🚀 **Próxima fase: Optimización del análisis de clientes y presentación final en Power BI.**  
