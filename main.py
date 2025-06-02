from flask import Flask, send_from_directory, render_template, redirect
import os

app = Flask(
    __name__,
    static_folder="static",      # Carpeta donde guardas css/, js/, img/
    template_folder="templates"  # Carpeta donde guardas tus .html
)

@app.route('/')
def home():
    # Tu página de inicio (index.html debe estar dentro de /templates)
    return render_template('index.html')

# 1) Redirecciona al microservicio “Control de Guardia”
@app.route("/control")
def guardia_control():
    return redirect("https://controlguardia.onrender.com")

# 2) Redirecciona al microservicio “Guardia”
@app.route("/guardia")
def guardia_principal():
    return redirect("https://guardiav2-production.up.railway.app/")

# 3) Redirecciona al microservicio “Distribución”
@app.route("/distribucion")
def distribucion():
    return redirect("https://distribucion-1.onrender.com/")

# 4) Redirecciona al nuevo microservicio “Web”
@app.route("/web")
def web_principal():
    return redirect("https://web-production-2feb5.up.railway.app/")

# ———————— SERVIR ARCHIVOS ESTÁTICOS ————————

@app.route('/img/<path:filename>')
def serve_images(filename):
    # Sirve cualquier imagen que pongas en static/img/...
    return send_from_directory(
        os.path.join(app.static_folder, 'img'),
        filename
    )

@app.route('/css/<path:filename>')
def serve_css(filename):
    # Sirve cualquier archivo CSS que pongas en static/css/...
    return send_from_directory(
        os.path.join(app.static_folder, 'css'),
        filename
    )

@app.route('/js/<path:filename>')
def serve_js(filename):
    # Sirve cualquier archivo JS que pongas en static/js/...
    return send_from_directory(
        os.path.join(app.static_folder, 'js'),
        filename
    )

# ———————— FIN DE RUTAS ————————

if __name__ == '__main__':
    # Deja debug=True mientras desarrollas. En producción pon debug=False.
    app.run(host='0.0.0.0', port=5000, debug=True)
