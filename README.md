# API de Infracciones de Tránsito

Esta API está construida con Django y Django REST Framework para gestionar infracciones de tránsito. Permite registrar, listar y gestionar información sobre personas, vehículos y oficiales de policía.

## Instalación

# 1. Clona este repositorio:

   git clone https://github.com/hugojbustos/API_Transito.git
   cd API_Transito

# 2. Entorno virtual:
    python -m venv venv
    source venv/bin/activate  # o venv\Scripts\activate en Windows

# 3. Instalar dependencias:
    pip install -r requirements.txt

# 4. Migraciones:
    python manage.py makemigrations
    python manage.py migrate

# 5. Crer usuario para administrar app:
    python manage.py createsuperuser

# 6. Ejecutar servidor:
    python manage.py runserver

# 7. Administración:
    Accede al panel de administración en http://localhost:8000/admin/ con las credenciales del superusuario.
    Administra las entidades Persona, Vehiculo y Oficial desde el panel de administración.

# 8. API Endpoints:
    Cargar Infracción

    URL: /api/cargar_infraccion/
    Método: POST
    Payload de ejemplo:
    {
    "placa_patente": "AB89",
    "timestamp": "2019-09-01T12:00:00",
    "comentarios": "Infracción",
    "numero_identificativo_oficial": 2
    }
    
    Generación de Token para poder generar una infracción, el token es único para cada oficial/policia 
    Ingresar al shell con el comando:

        python manage.py shell

    Una vez en el prompt de Python ejecutar estas líneas( a modo de ejemplo queda el id=1) y así generan token:

        from rest_framework.authtoken.models import Token
        from app.models import Policia
        oficial = Policia.objects.get(id=1)
        token, created = Token.objects.get_or_create(user=oficial.user)
        print(f"Token del oficial {oficial.user}: {token.key}")
    

    Listar Infracciones por Correo

    URL: /api/listar_infracciones/?email_propietario=correo_ejemplo@dominio.com
    Método: GET
    Parámetros de consulta:
    email_propietario: Correo electrónico del propietario de los vehículos(Modelo Persona).

    Doc de la documentación en el endpoint por defecto
        http://127.0.0.1:8000/