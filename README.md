🌍 Renewable Energy Dashboard
Este proyecto es una aplicación web interactiva que permite visualizar datos relacionados con la producción, consumo, inversión y otros indicadores clave de energía renovable a nivel mundial.

📊 Funcionalidades principales
Visualización de métricas energéticas por país, año y tipo de energía.

Selección dinámica de tipos de gráfico: barras, líneas, torta, etc.

Filtros interactivos para personalizar la visualización.

Interfaz responsiva y atractiva desarrollada con HTML, CSS, JS y Chart.js.

Backend construido con Flask que procesa los datos y entrega los resultados.

📦 Instalación
1. Clonar el repositorio
git clone https://github.com/EdisonGrGr/Energias-renovables.git)
2. Crear y activar entorno virtual
python -m venv env
env\Scripts\activate        # Windows
source env/bin/activate     # Linux/macOS
3. Instalar dependencias
pip install -r requirements.txt
4. Descargar el dataset
Ir a: Global Renewable Energy Dataset - Kaggle

Descargar el archivo .csv.

Renombrar el archivo a complete_renewable_energy_dataset.csv

Colocarlo en la carpeta: static/data/.

🚀 Ejecución del proyecto
python app.py
Luego abre tu navegador en:

http://127.0.0.1:5000/
📁 Dataset original
Fuente: Kaggle

Nombre: Global Renewable Energy and Indicators Dataset

Autor: Anish Vijay

Link: [Ir al dataset](https://www.kaggle.com/datasets/anishvijay/global-renewable-energy-and-indicators-dataset?resource=download)

Este dataset incluye información de más de 50 países entre 2000 y 2020, con más de 50 indicadores que cubren producción, capacidad instalada, inversión, emisiones de CO₂, entre otros.

🧠 Tecnologías usadas
Frontend: HTML5, CSS3, JavaScript, Chart.js

Backend: Python + Flask

Data: Pandas


🧑‍💻 Autores
Nombre: Edison García - Sebastian Correa
Talentotech: Bootcamp de Programación
