
# Cacciuttolo TCT

Sistema de carga y gestión de TCT (Trabajo de Conclusión de Terciario) para la institución Cacciuttolo.

## Requisitos Previos

- Python 3.8 o superior
- PostgreSQL 12 o superior
- pip (gestor de paquetes Python)

## Instalación

1. Clona el repositorio:
```bash
git clone [https://github.com/fdoquezada/cacciuttolo_tct.git]
cd cacciuttolo_tctpython -m venv .venv
source .venv/bin/activate  # Linux/Mac
# o
.venv\Scripts\activate     # Windows
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura la base de datos:
```bash
python manage.py migrate
```

4. Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

5. Accede a la aplicación:
```
http://localhost:8000
```

## Desarrolladores

- Fernando Quezada
