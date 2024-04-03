# README en Español

Dashboard Financiero - DigiData Salta
=====================================

Este repositorio contiene archivos y scripts relacionados con un dashboard financiero, con datos ficticios, desarrollado en PowerBI, para tener de ejemplo para mi emprendimiento DigiData Salta.

Detalles del Dashboard
---------------------------------

El archivo `digiDataSalta - dashboard ejemplo.pbix` es un dashboard interactivo desarrollado en Power BI. Contiene lo siguiente:

### Página de Inicio

<img src="img\dashboard pagina inicio.PNG" alt="Pagina Inicio de Dashboard" width="85%">

La página de inicio del dashboard presenta una interfaz simple y accesible para navegar hacia las secciones principales del mismo. Características de esta página:

*   **Logo de DigiData Salta:** Se muestra el logo de la empresa para una identificación rápida.
*   **Botones de Navegación:** Se presentan botones claramente etiquetados que permiten acceder a las secciones clave del dashboard, incluyendo Beneficios, Ingresos y Gastos.

* * *

### Página de Beneficios
<img src="img\dashboard pagina beneficios.PNG" alt="Pagina Beneficios de Dashboard" width="85%">

La página de Beneficios proporciona un análisis detallado de los beneficios obtenidos por la empresa. Características y elementos destacados de esta página:

*   **Tarjetas:**
    
    *   Total de Ingresos: Muestra la suma total de ingresos registrados.
    *   Total de Gastos: Indica la suma total de gastos incurridos.
    *   Total de Beneficios: Calcula la diferencia entre los ingresos y los gastos, representando así el beneficio neto.
    *   KPI % Margen: Presenta el porcentaje de margen de beneficio, con un indicador visual que señala si se alcanza el objetivo del 15%.
*   **Gráficos y Tablas:**
    
    *   **Gráfico de Columnas "Total Beneficios por Mes":** Representa la evolución mensual de los beneficios.
    *   **Tabla de "Total Beneficios por Mes":** Proporciona una desglose detallado por año y mes, incluyendo los totales de ingresos, gastos, beneficios y el porcentaje de margen, con indicadores visuales.
    *   **Gráfico de Barras "Total Beneficios por Sucursal":** Muestra la distribución de beneficios entre las distintas sucursales.
    *   **Tabla "Total Beneficios por Sucursal":** Detalla los beneficios generados por cada sucursal, junto con el porcentaje de margen.
*   **Segmentadores:**
    
    *   Segmentador de Año: Permite seleccionar un año específico para filtrar los datos.
    *   Segmentador de Sucursal: Permite seleccionar una o varias sucursales para visualizar los datos correspondientes.

Esta página proporciona una visión detallada de los beneficios financieros de la empresa, permitiendo un análisis profundo y una toma de decisiones informada.

### Página de Ingresos
<img src="img\dashboard pagina ingresos.PNG" alt="Pagina Ingresos de Dashboard" width="85%">

La página de Ingresos proporciona una visión detallada de los ingresos generados por la empresa. Aquí están los elementos y características destacados:

*   **Tarjetas:**
    
    *   Total de Ingresos: Muestra la suma total de ingresos registrados.
    *   Promedio de Ingresos por Mes: Calcula el promedio mensual de ingresos.
    *   KPI Ingresos Mes Actual: Indica si se alcanza el objetivo establecido para los ingresos del mes actual, con un indicador visual.
*   **Gráficos y Tablas:**
    
    *   **Gráfico de Columnas "Total Ingresos por Mes":** Presenta la evolución mensual de los ingresos.
    *   **Tabla de "Total Ingresos por Mes":** Detalla los ingresos por año y mes, incluyendo el porcentaje de diferencia con respecto al mes anterior, con indicadores visuales de aumento o disminución.
    *   **Tabla "Productos más Vendidos":** Muestra los productos ordenados por sus ingresos totales, lo que facilita la identificación de los productos más populares.
    *   **Gráficos de Columnas "Ingresos por Sucursal", "Ingresos por Método de Pago" y "Ingresos por Usuario":** Ofrecen una perspectiva detallada de los ingresos desglosados por sucursal, método de pago y usuario.
*   **Segmentadores:**
    
    *   Segmentador "Año": Permite filtrar los datos por año, con opción de selección única.
    *   Segmentador "Sucursal": Permite filtrar los datos por sucursal, con opción de selección múltiple.
    *   Segmentador "Método de Pago": Permite filtrar los datos por método de pago, con opción de selección múltiple.

Esta página permite una análisis detallado de los ingresos, permitiendo a los usuarios entender mejor la distribución y tendencias de los ingresos de la empresa.

* * *

### Página de Gastos
<img src="img\dashboard pagina gastos.PNG" alt="Pagina Gastos de Dashboard" width="85%">

La página de Gastos ofrece una perspectiva detallada de los gastos en la empresa. Aquí están los elementos y características más importantes:

*   **Tarjetas de Resumen:**
    
    *   Total de Gastos: Muestra la suma total de gastos registrados.
    *   Promedio de Gastos por Mes: Calcula el promedio mensual de gastos.
    *   KPI Gastos Mes Actual: Indica si se supera el límite establecido para los gastos del mes actual, con un indicador visual.
*   **Gráficos y Tablas:**
    
    *   **Gráfico de Columnas "Total Gastos por Mes":** Presenta la evolución mensual de los gastos.
    *   **Tabla de "Total Gastos por Mes":** Detalla los gastos por año y mes, incluyendo el porcentaje de diferencia con respecto al mes anterior, con indicadores visuales de aumento o disminución.
    *   **Gráfico de Barras "Gastos por Categoría":** Muestra los gastos ordenados por categoría, facilitando la identificación de las áreas de mayor gasto.
    *   **Gráficos de Columnas "Gastos por Sucursal", "Gastos por Método de Pago" y "Gastos por Usuario":** Ofrecen una perspectiva detallada de los gastos desglosados por sucursal, método de pago y usuario.
*   **Segmentadores:**
    
    *   Segmentador "Año": Permite filtrar los datos por año, con opción de selección única.
    *   Segmentador "Sucursal": Permite filtrar los datos por sucursal, con opción de selección múltiple.
    *   Segmentador "Método de Pago": Permite filtrar los datos por método de pago, con opción de selección múltiple.

Esta página proporciona una visión completa de los gastos de la empresa, permitiendo un análisis exhaustivo y una gestión eficiente de los recursos financieros.

Archivos del Repositorio
------------------------

### `creaDatasetsIngresosYGastos.py`

Este script Python genera conjuntos de datos simulados para ingresos y gastos basados en un archivo de Excel ficticio. Utiliza Pandas para procesar los datos y generar archivos CSV con información detallada sobre ingresos y gastos.

#### Descripción del Script:

*   Lee un archivo de Excel llamado "Finanzas DigiData Salta - ficticio.xlsx".
*   Procesa los datos para generar datos de ingresos y gastos ficticios.
*   Guarda los datos generados como archivos CSV: `ingresos_digiData.csv` y `gastos_digiData.csv`.

### `creaDatasetBeneficios.py`

Este script Python crea un conjunto de datos simulado para los beneficios combinando datos de ingresos y gastos. Utiliza Pandas para procesar los datos y calcular los beneficios.

#### Descripción del Script:

*   Carga archivos CSV de ingresos y gastos.
*   Agrupa los datos por año, mes y sucursal.
*   Calcula los beneficios restando los gastos de los ingresos.
*   Guarda los datos de beneficios como un archivo CSV: `beneficios_digiData.csv`.

### `digiDataSalta - dashboard ejemplo.pbix`

Este archivo es un dashboard financiero desarrollado en Power BI. Proporciona visualizaciones interactivas basadas en datos ficticios de ingresos, gastos y beneficios. Ver detalles más adelante.

### Otros Archivos

*   `gastos_digidata.csv`: Archivo CSV generado por `creaDatasetsIngresosYGastos.py` que contiene información detallada sobre gastos.
*   `ingresos_digiData.csv`: Archivo CSV generado por `creaDatasetsIngresosYGastos.py` que contiene información detallada sobre ingresos.
*   `Finanzas DigiData Salta - ficticio.xlsx`: Archivo de Excel ficticio que proporciona datos de finanzas simulados, utilizado como entrada para generar datos de ingresos y gastos.
*   `beneficios_digiData.csv`: Archivo CSV generado por `creaDatasetBeneficios.py` que contiene datos de beneficios combinados.

---

# README in English

Financial Dashboard - DigiData Salta
=========================================

This repository contains files and scripts related to a financial dashboard, with fictitious data, developed in Power BI, as an example for my venture DigiData Salta.



Dashboard Details
-----------------

The file `digiDataSalta - dashboard ejemplo.pbix` is an interactive dashboard developed in Power BI. It contains the following:

### Home Page

<img src="img\dashboard pagina inicio.PNG" alt="Dashboard Home Page" width="85%">

The dashboard's home page presents a simple and accessible interface for navigating to its main sections. Features of this page include:

*   **DigiData Salta Logo:** Displays the company logo for quick identification.
*   **Navigation Buttons:** Clearly labeled buttons allow access to key sections of the dashboard, including Profits, Income, and Expenses.

* * *

### Profits Page
<img src="img\dashboard pagina beneficios.PNG" alt="Dashboard Profits Page" width="85%">

The Profits page provides a detailed analysis of the profits earned by the company. Features and highlights of this page include:

*   **Cards:**
    
    *   Total Income: Displays the total sum of recorded income.
    *   Total Expenses: Indicates the total sum of incurred expenses.
    *   Total Profits: Calculates the difference between income and expenses, representing the net profit.
    *   % Margin KPI: Presents the percentage profit margin, with a visual indicator signaling if the 15% target is achieved.
*   **Charts and Tables:**
    
    *   **Column Chart "Total Profits per Month":** Represents the monthly evolution of profits.
    *   **Table "Total Profits per Month":** Provides a detailed breakdown by year and month, including totals of income, expenses, profits, and the margin percentage, with visual indicators.
    *   **Bar Chart "Total Profits per Branch":** Displays the distribution of profits among different branches.
    *   **Table "Total Profits per Branch":** Details the profits generated by each branch, along with the margin percentage.
*   **Slicers:**
    
    *   Year Slicer: Allows selection of a specific year to filter the data.
    *   Branch Slicer: Allows selection of one or multiple branches to view corresponding data.

This page provides a detailed view of the company's financial profits, enabling deep analysis and informed decision-making.

### Income Page
<img src="img\dashboard pagina ingresos.PNG" alt="Dashboard Income Page" width="85%">

The Income page provides a detailed view of the income generated by the company. Here are the featured elements and characteristics:

*   **Cards:**
    
    *   Total Income: Displays the total sum of recorded income.
    *   Average Monthly Income: Calculates the average monthly income.
    *   Current Month Income KPI: Indicates whether the target set for the current month's income is achieved, with a visual indicator.
*   **Charts and Tables:**
    
    *   **Column Chart "Total Income per Month":** Presents the monthly evolution of income.
    *   **Table "Total Income per Month":** Details income by year and month, including the percentage difference from the previous month, with visual indicators of increase or decrease.
    *   **Table "Top Selling Products":** Displays products ordered by their total income, facilitating identification of the most popular products.
    *   **Column Charts "Income by Branch", "Income by Payment Method", and "Income by User":** Offer a detailed perspective of income broken down by branch, payment method, and user.
*   **Slicers:**
    
    *   Year Slicer: Allows filtering of data by year, with single selection option.
    *   Branch Slicer: Allows filtering of data by branch, with multiple selection option.
    *   Payment Method Slicer: Allows filtering of data by payment method, with multiple selection option.

This page enables detailed analysis of income, allowing users to better understand income distribution and trends.

* * *

### Expenses Page
<img src="img\dashboard pagina gastos.PNG" alt="Dashboard Expenses Page" width="85%">

The Expenses page offers a detailed perspective of expenses in the company. Here are the key elements and characteristics:

*   **Summary Cards:**
    
    *   Total Expenses: Displays the total sum of recorded expenses.
    *   Average Monthly Expenses: Calculates the average monthly expenses.
    *   Current Month Expenses KPI: Indicates whether the set limit for the current month's expenses is exceeded, with a visual indicator.
*   **Charts and Tables:**
    
    *   **Column Chart "Total Expenses per Month":** Presents the monthly evolution of expenses.
    *   **Table "Total Expenses per Month":** Details expenses by year and month, including the percentage difference from the previous month, with visual indicators of increase or decrease.
    *   **Bar Chart "Expenses by Category":** Displays expenses ordered by category, facilitating identification of areas of higher spending.
    *   **Column Charts "Expenses by Branch", "Expenses by Payment Method", and "Expenses by User":** Offer a detailed perspective of expenses broken down by branch, payment method, and user.
*   **Slicers:**
    
    *   Year Slicer: Allows filtering of data by year, with single selection option.
    *   Branch Slicer: Allows filtering of data by branch, with multiple selection option.
    *   Payment Method Slicer: Allows filtering of data by payment method, with

 multiple selection option.

This page provides a comprehensive view of the company's expenses, enabling thorough analysis and efficient management of financial resources.

Repository Files
----------------

### `creaDatasetsIngresosYGastos.py`

This Python script generates simulated datasets for income and expenses based on a fictitious Excel file. It uses Pandas to process the data and generate CSV files with detailed information about income and expenses.

#### Script Description:

*   Reads an Excel file named "Finanzas DigiData Salta - ficticio.xlsx".
*   Processes the data to generate fictitious income and expense data.
*   Saves the generated data as CSV files: `ingresos_digiData.csv` and `gastos_digiData.csv`.

### `creaDatasetBeneficios.py`

This Python script creates a simulated dataset for profits by combining income and expense data. It uses Pandas to process the data and calculate profits.

#### Script Description:

*   Loads CSV files of income and expenses.
*   Groups the data by year, month, and branch.
*   Calculates profits by subtracting expenses from income.
*   Saves the profit data as a CSV file: `beneficios_digiData.csv`.

### `digiDataSalta - dashboard ejemplo.pbix`

This file is a financial dashboard developed in Power BI. It provides interactive visualizations based on fictitious income, expense, and profit data. See details below.

### Other Files

*   `gastos_digidata.csv`: CSV file generated by `creaDatasetsIngresosYGastos.py` containing detailed information about expenses.
*   `ingresos_digiData.csv`: CSV file generated by `creaDatasetsIngresosYGastos.py` containing detailed information about income.
*   `Finanzas DigiData Salta - ficticio.xlsx`: Fictitious Excel file providing simulated finance data, used as input to generate income and expense data.
*   `beneficios_digiData.csv`: CSV file generated by `creaDatasetBeneficios.py` containing combined profit data.