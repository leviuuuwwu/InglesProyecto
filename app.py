from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from parqueo_data import espacios

app = Flask(__name__)
app.secret_key = 'clave_secreta_super_segura'

# Credenciales fijas
USERNAME = "admin"
PASSWORD = "1234"

# Ruta principal: login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect('/admin')
        else:
            return "Usuario o contraseña incorrectos"
    return render_template('login.html')

# Vista pública para usuarios visitantes
@app.route('/parqueo')
def vista_publica():
    ocupados = sum(1 for e in espacios if e['estado'] == 'ocupado')
    libres = sum(1 for e in espacios if e['estado'] == 'libre')
    return render_template('parqueo.html', parqueos=espacios, ocupados=ocupados, libres=libres)

# Panel de administración (vista de parqueo)
@app.route('/admin')
def admin_panel():
    if not session.get('logged_in'):
        return redirect('/')
    return render_template('admin.html', parqueos=espacios)

# Cambiar estado del parqueo
@app.route('/toggle/<int:espacio_id>')
def toggle_estado(espacio_id):
    if not session.get('logged_in'):
        return redirect('/')
    for espacio in espacios:
        if espacio['id'] == espacio_id:
            espacio['estado'] = 'ocupado' if espacio['estado'] == 'libre' else 'libre'
            break
    return redirect('/admin')

# Logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')

@app.route("/api/estadisticas-parqueo")
def estadisticas_parqueo():
    total = 192  
    ocupados = sum(1 for p in espacios if p["estado"] == "ocupado")
    disponibles = total - ocupados
    porcentaje_ocupado = round((ocupados / total) * 100, 1)

    return jsonify({
        "total": total,
        "disponibles": disponibles,
        "ocupados": ocupados,
        "porcentaje_ocupado": porcentaje_ocupado
    })


if __name__ == '__main__':
    app.run(debug=True)