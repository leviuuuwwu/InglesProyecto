# app.py
from datetime import datetime
from data.parqueos import parqueos
from flask import Flask, render_template, redirect, url_for, request, session, flash
from datetime import datetime
from data.parqueos import parqueos

app = Flask(__name__)
app.secret_key = 'clave_secreta_muuy_segura'  # Necesaria para usar sesiones


@app.route('/')
def public_view():
    return render_template('public.html', parqueos=parqueos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pw = request.form.get('password')
        if user == 'admin' and pw == 'admin':
            session['admin'] = True
            return redirect(url_for('admin_view'))
        else:
            flash('Credenciales incorrectas', 'error')
    return render_template('login.html')


@app.route('/admin')
def admin_view():
    if not session.get('admin'):
        return redirect(url_for('login'))

    ocupados = [p for p in parqueos if p['estado'] == 'occupied']
    disponibles = [p for p in parqueos if p['estado'] == 'available']
    tiempos = []
    for p in ocupados:
        if p['hora_inicio_ocupado']:
            tiempo = (datetime.now() - p['hora_inicio_ocupado']).total_seconds() / 60
            tiempos.append(tiempo)
    promedio_tiempo = round(sum(tiempos) / len(tiempos), 2) if tiempos else 0
    zona_a = sum(1 for p in ocupados if p['zona'] == 'A')
    zona_b = sum(1 for p in ocupados if p['zona'] == 'B')
    zona_mas_usada = 'A' if zona_a > zona_b else 'B' if zona_b > zona_a else 'Igual'
    porcentaje_ocupados = round(len(ocupados) / len(parqueos) * 100, 2)

    stats = {
        'ocupados': len(ocupados),
        'disponibles': len(disponibles),
        'promedio_tiempo': promedio_tiempo,
        'zona_mas_usada': zona_mas_usada,
        'porcentaje_ocupados': porcentaje_ocupados
    }

    return render_template('admin.html', parqueos=parqueos, stats=stats)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/toggle/<int:pid>')
def toggle_parqueo(pid):
    for p in parqueos:
        if p['id'] == pid:
            if p['estado'] == 'available':
                p['estado'] = 'occupied'
                p['hora_inicio_ocupado'] = datetime.now()
            else:
                p['estado'] = 'available'
                p['hora_inicio_ocupado'] = None
            break
    return redirect(url_for('admin_view'))

if __name__ == '__main__':
    app.run(debug=True)