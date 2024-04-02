Dashboard Financiero - DigiData Salta
=====================================

Este repositorio contiene archivos y scripts relacionados con un dashboard financiero, con datos ficticios, desarrollado en PowerBI, para tener de ejemplo para mi emprendimiento DigiData Salta.

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

Detalles del Dashboard
---------------------------------

El archivo `digiDataSalta - dashboard ejemplo.pbix` es un dashboard interactivo desarrollado en Power BI. Contiene lo siguiente:

### Página de Inicio

<img src="img\cargas de combustible en colectivos\login.PNG" alt="Pagina Inicio de Dashboard" width="85%">

La página de inicio del dashboard presenta una interfaz simple y accesible para navegar hacia las secciones principales del mismo. Características de esta página:

*   **Logo de DigiData Salta:** Se muestra el logo de la empresa para una identificación rápida.
*   **Botones de Navegación:** Se presentan botones claramente etiquetados que permiten acceder a las secciones clave del dashboard, incluyendo Beneficios, Ingresos y Gastos.

* * *

### Página de 
<img src="img\cargas de combustible en colectivos\login.PNG" alt="Pagina Beneficios de Dashboard" width="85%">

La página de Beneficios proporciona un análisis detallado de los beneficios obtenidos por la empresa. Características y elementos destacados de esta página:

*   **Tarjetas de Resumen:**
    
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