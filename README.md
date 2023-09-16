# Taller práctico de visión por computadora: Entrenando tu propio modelo de YOLOv8

_Taller orientado al entrenamiento de un modelo de detección de objetos con YOLOv8 en un conjunto de datos personalizado._

<details>
  <summary>Dataset Sugeridos</summary>
  <ul>
    <li><a href="https://universe.roboflow.com/mbconv/mb-detection/dataset/1">Motos</a></li>
    <li><a href="https://universe.roboflow.com/objek-dalam-ayunda/kacamata-model/dataset/2">Lentes</li>
    <li><a href="https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4">Patentes</a></li>
    <li><a href="https://universe.roboflow.com/nn-vfff7/pens-xbrvj/dataset/1">Lapiz</a></li>
    <li><a href="https://universe.roboflow.com/dpow/laptopmodel/dataset/1">Laptop</a></li>
    <li><a href="https://universe.roboflow.com/fiap-fumtz/bike-model-object-detection/dataset/1">Bicicletas</a>
    <li><a rel="me" href="https://universe.roboflow.com/chung-w1zpa/phone-faxfz/dataset/1">Smartphone</a></li>
  </ul>
</details>

## Autor

- Vicente Aguilera Arias - vicente.aguilera2001@alumnos.ubiobio.cl

### 🛠️ Construido con

- [Python v3.11](https://www.python.org/) - Lenguaje de programación

### Instalación

- Se clona el repositorio de GitHub
  ```bash
  git clone https://github.com/ubiobio/TallerYolov8.git detector-script
  ```
- Se ingresa a la carpeta del proyecto
  ```bash
  cd TallerYolov8
  ```
- Se crea un entorno virtual

  ```bash
  python -m venv venv
  ```

- Se activa el entorno virtual

  ```bash
  .\venv\Scripts\activate
  ```

- Se instala los requerimientos del proyecto

  ```bash
  pip install -r requirements.txt
  ```

- En la carpeta _data_ ingresa las imagenes y su respectivo archivo .txt para el entrenamiento.

- Se ejecuta el script
  ```bash
  python main.py
  ```

## Licencia 📄

Este proyecto está bajo la GNU Affero General Public License v3.0 - mira el archivo [LICENSE](LICENSE) para detalles
