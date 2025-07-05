# 🅿️ Simulador de Disponibilidad de Parqueo

Este es un sitio web simple desarrollado con **Flask** que simula la disponibilidad de espacios de parqueo. El administrador puede cambiar manualmente el estado de los espacios (ocupado o libre), y los usuarios pueden ver una vista pública en tiempo real.

## 📁 Estructura del Proyecto

simulador_parqueo/
│
├── app.py # Lógica principal de la app Flask
├── parqueo_data.py # Lista simulada de espacios de parqueo
├── requirements.txt # Dependencias necesarias
│
├── static/
│ └── style.css # Estilos generales
│
├── templates/
│ ├── login.html # Vista de inicio de sesión
│ ├── admin.html # Panel de administración
│ └── parqueo.html # Vista pública para usuarios
│
└── README.md

## 🚀 Cómo ejecutar el proyecto

1. Clona este repositorio o descarga el proyecto:
   ```bash
   git clone https://github.com/tu-usuario/simulador_parqueo.git

2. Navega a la carpeta del proyecto:

cd simulador_parqueo

3. Instala las dependencias:

pip install -r requirements.txt

4. Ejecuta el servidor Flask:

python app.py

5. Abre tu navegador y visita:

🛠️ Panel Admin: http://localhost:5000/
👀 Vista Pública: http://localhost:5000/parqueo

🔐 Credenciales del Administrador
Usuario: admin
Contraseña: 1234

✨ Características
- Login para administrador
- Cambiar estado de parqueos (ocupado/libre)
- Vista pública sin login
- Recuadros verdes o rojos según disponibilidad
- Conteo de espacios libres y ocupados
- Recarga automática cada 5 segundos

🛠️ Pendientes/Futuros Mejoras
- Refrescar automáticamente con JavaScript sin recargar
- Persistencia con base de datos (SQLite o similar)
- Soporte para múltiples administradores
- Diseño adaptable para móvil