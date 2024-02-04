from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)

email_password = os.getenv("EMAIL_PASSWORD")

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/bases')
def bases():
    return render_template('Bases.html')

@app.route('/contacto')
def contacto():
    return render_template('Contacto.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

def send_email(subject, body, recipient):
    sender = 'ventas@fabricancion.com'
    password = "fabricancion3710460"  # Usar la contrase�a desde la variable de entorno

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient

    try:
        server = smtplib.SMTP_SSL('mail.fabricancion.com', 465)
        server.login(sender, password)
        server.send_message(message)
        server.quit()
        return "Correo enviado exitosamente"
    except Exception as e:
        return f"Error al enviar el correo: {e}"

@app.route('/send_email', methods=['POST'])
def handle_send_email():
    data = request.json
    subject = data.get('subject', 'Formulario')
    body = data.get('body', '')
    recipient = data.get('recipient', 'ramsesescauriza@gmail.com')

    result = send_email(subject, body, recipient)
    return result

if __name__ == '__main__':
    app.run(debug=True, port=8080)
