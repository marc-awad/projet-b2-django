from dotenv import load_dotenv
import resend 
import os

load_dotenv()
resend.api_key = os.getenv('RESEND_SECRET_KEY')

def validation(conge):
    pass
    r = resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": conge.email,
    "subject": "Congés payés : Validation",
    "html": f"""
    <p>Bonjour <strong>{conge.name}</strong>,</p>
    <p>Nous sommes heureux de vous informer que votre demande de <strong>{conge.get_reason_display()}</strong> a été <strong>acceptée</strong>.</p>
    <p>Voici les détails de votre demande de congé :</p>
    <ul>
        <li>Date de début : {conge.date}</li>
        <li>Date de fin : {conge.end_date}</li>
        <li>Raison : {conge.get_reason_display()}</li>
    </ul>
    <p>Nous vous souhaitons un excellent congé et restons disponibles pour toute question.</p>
    """
    })

def cancel(conge):
    r = resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": conge.email,
    "subject": "Congés payés : Refus",
    "html": f"""
    <p>Bonjour <strong>{conge.name}</strong>,</p>
    <p>Nous regrettons de vous informer que votre demande de <strong>{conge.get_reason_display()}</strong> a été <strong>refusée</strong>.</p>
    <p>Voici les détails de votre demande de congé :</p>
    <ul>
        <li>Date de début : {conge.date}</li>
        <li>Date de fin : {conge.end_date}</li>
        <li>Raison : {conge.get_reason_display()}</li>
    </ul>
    <p>Nous restons disponibles pour discuter de cette décision si nécessaire.</p>
    """
    })
