import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import SMTP_PASSWORD

def load_email_template(file_path):
    """
    Charge le modèle d'email depuis un fichier HTML.
    """
    with open(file_path, 'r') as file:
        return file.read()

def send_alert(subject, alert_type, alert_message):
    """
    Envoie un e-mail d'alerte avec le sujet, le type d'alerte et le message.
    """
    # Définir l'adresse e-mail de l'expéditeur et des destinataires
    sender_email = "amar.ailane@alumni.univ-avignon.fr"
    receiver_emails = [ "ailaneamar9@gmail.com"]

    # Configuration SMTP
    smtp_ssl_host = 'smtpz.univ-avignon.fr'
    smtp_ssl_port = 465  # Port SSL
    smtp_username = "amar.ailane@alumni.univ-avignon.fr"
    smtp_password = SMTP_PASSWORD

    # Charger le modèle d'email
    email_template_file = "/home/vboxuser/mini-projet/parte_3/templates.html"
    email_template = load_email_template(email_template_file)

    # Remplacer les placeholders par les valeurs réelles
    email_content = email_template.replace("{username}", "amar")  # Remplace par le nom réel
    email_content = email_content.replace("{alert_type}", alert_type)  # Type d'alerte
    email_content = email_content.replace("{alert_message}", alert_message)  # Message d'alerte

    # Créer le message e-mail
    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = ', '.join(receiver_emails)
    msg['Subject'] = subject  # Sujet de l'alerte (e.g., "Alerte Disque")

    # Attacher le corps du message (en texte HTML)
    msg.attach(MIMEText(email_content, 'html'))

    # Connexion au serveur SMTP et envoi de l'e-mail
    try:
        with smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port) as server:
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_emails, msg.as_string())
        print(f"Alerte envoyée avec succès : {subject}")
    except Exception as e:
        print(f"Échec de l'envoi de l'alerte : {e}")
