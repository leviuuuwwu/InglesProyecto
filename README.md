# 🅿️ Simulador de Disponibilidad de Parqueo

Este es un sitio web simple desarrollado con **Flask** que simula la disponibilidad de espacios de parqueo. El administrador puede cambiar manualmente el estado de los espacios (ocupado o libre), y los usuarios pueden ver una vista pública en tiempo real.

## 🚀 Cómo ejecutar el proyecto

1. Clona este repositorio o descarga el proyecto:
   ```bash
   git clone https://github.com/leviuuuwwu/InglesProyecto

2. Navega a la carpeta del proyecto:

cd inglesproyecto

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