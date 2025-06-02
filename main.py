from flask import Flask, send_from_directory, render_template, redirect
import os

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route('/')
def home():
    return render_template('index.html')

# Redirecciona a microservicio de Guardia
@app.route("/guardia")
def guardia():
    return redirect("https://guardiav2-production.up.railway.app/")

# Redirecciona a microservicio de Distribución
@app.route("/distribucion")
def distribucion():
    return redirect("https://distribucion-1.onrender.com/")

@app.route("/cronograma")
def cronograma():
    return redirect("https://web-production-2feb5.up.railway.app/")

# Archivos estáticos (CSS, JS, imágenes)
@app.route('/img/<path:filename>')
def serve_images(filename):
    return send_from_directory(os.path.join(app.static_folder, 'img'), filename)

@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory(os.path.join(app.static_folder, 'css'), filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory(os.path.join(app.static_folder, 'js'), filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
