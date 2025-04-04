# 📸 PhotoCampus

**PhotoCampus** es un emprendimiento dedicado a la fotografía profesional. Con el fin de organizar y optimizar sus servicios, este proyecto busca implementar un sistema de gestión para los servicios fotográficos disponibles. El desarrollo del proyecto se apoya en herramientas de control de versiones como **Git** y **GitHub**, lo que permite mantener una trazabilidad clara y efectiva del proceso de desarrollo.

---

## 🚀 Objetivos del Proyecto

- Registrar, editar y eliminar servicios fotográficos.
- Garantizar un almacenamiento local eficiente mediante archivos JSON.
- Promover buenas prácticas de desarrollo colaborativo utilizando Git y GitHub.

---

## ⚙️ Especificaciones Técnicas

### Módulo: Gestión de Servicios Fotográficos

- **Información Básica**:
  - Nombre del paquete fotográfico
  - Precio
  - Tipo de evento (boda, retrato, producto, etc.)
  - Duración estimada (en horas)

- **Funcionalidades**:
  - Agregar nuevos servicios
  - Editar servicios existentes
  - Eliminar servicios obsoletos

- **Almacenamiento**:
  - Toda la información se guarda en un archivo local `servicios.json` para facilitar el acceso y la manipulación de datos.

---

## 🛠️ Configuración y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Jharmo05/Examen-3-abril.git
   cd Examen-3-abril
   ```

2. **Instalar dependencias (si aplica)**:
   - Este proyecto no depende de paquetes externos (por ahora), solo necesitas tener instalado **Python 3.x**.

3. **Ejecutar el sistema**:
   - Abre el archivo principal (`main.py` o similar) en tu entorno preferido y ejecútalo para comenzar a gestionar los servicios.

---

## 🌳 Estructura del Repositorio

```
Examen-3-abril/
│
├── almacenamiento.py           # Archivo donde se cargan y suben al JSON
├── servicios.py                # Archivo de almacenamiento local
├── main.py                     # Código principal del sistema
├── servicios_fotograficos.json # Archivo JSON donde se guardan los servicios fotograficos
├── README.md                   # Documentación del proyecto
```

---

## 🧪 Control de Versiones

### 🔀 Ramas del Proyecto

Se trabajó con múltiples ramas para mantener el desarrollo organizado:

- `main`: Rama principal con la versión estable del sistema.
- `feature/add-services`: Desarrollo de la funcionalidad para agregar servicios.
- `feature/edit-services`: Implementación de la edición de servicios existentes.
- `feature/delete-services`: Funcionalidad para eliminar servicios.

### 📌 Commits

Se realizaron commits frecuentes y descriptivos en cada rama, por ejemplo:

- `feat: función para agregar nuevos servicios fotográficos`

---

## 📎 Enlace al Repositorio

🔗 [GitHub - Examen 3 abril](https://github.com/Jharmo05/Examen-3-abril)
