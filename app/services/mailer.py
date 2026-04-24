import os
import smtplib
from email.message import EmailMessage


def _smtp_config():
    host      = os.getenv("SMTP_HOST", "").strip()
    port      = int(os.getenv("SMTP_PORT", "587"))
    username  = os.getenv("SMTP_USER", "").strip()
    password  = os.getenv("SMTP_PASSWORD", "").strip()
    use_tls   = os.getenv("SMTP_USE_TLS", "true").strip().lower() in {"1", "true", "yes"}
    from_email = os.getenv("SMTP_FROM", username or "no-reply@cuure.health").strip()
    return host, port, username, password, use_tls, from_email


def _patient_html(name, doctor_name, date, slot, mode):
    return f"""
    <html><body style="font-family:Arial;background:#f4f6f8;">
      <table width="100%" align="center"><tr><td align="center">
        <table width="500" style="background:#fff;padding:20px;border-radius:10px;">
          <tr><td align="center">
            <h2>🏥 Cuure.health</h2>
            <p>Appointment Confirmed</p>
          </td></tr>
          <tr><td>
            <p>Hello <b>{name}</b>,</p>
            <p>Your appointment is confirmed with <b>{doctor_name}</b>.</p>
          </td></tr>
          <tr><td>
            <table width="100%">
              <tr><td><b>Date:</b></td><td>{date}</td></tr>
              <tr><td><b>Time:</b></td><td>{slot}</td></tr>
              <tr><td><b>Mode:</b></td><td>{mode}</td></tr>
            </table>
          </td></tr>
          <tr><td align="center" style="font-size:12px;color:#aaa;padding-top:20px;">
            © 2026 Cuure.health
          </td></tr>
        </table>
      </td></tr></table>
    </body></html>
    """


def _doctor_html(doctor_name, patient_name, date, slot, mode):
    return f"""
    <html><body style="font-family:Arial;background:#f4f6f8;">
      <table width="100%" align="center"><tr><td align="center">
        <table width="520" style="background:#fff;padding:24px;border-radius:10px;">
          <tr><td align="center">
            <h2>🏥 Cuure.health</h2>
            <p>New Appointment Scheduled</p>
          </td></tr>
          <tr><td>
            <p>Hello <b>{doctor_name}</b>,</p>
            <p>A new patient appointment has been booked.</p>
          </td></tr>
          <tr><td style="background:#f9fbfd;padding:12px;border-radius:6px;">
            <b>Patient:</b> {patient_name}
          </td></tr>
          <tr><td>
            <table width="100%" style="margin-top:15px;">
              <tr><td><b>Date:</b></td><td>{date}</td></tr>
              <tr><td><b>Time:</b></td><td>{slot}</td></tr>
              <tr><td><b>Mode:</b></td><td>{mode}</td></tr>
            </table>
          </td></tr>
          <tr><td align="center" style="font-size:12px;color:#aaa;padding-top:20px;">
            © 2026 Cuure.health
          </td></tr>
        </table>
      </td></tr></table>
    </body></html>
    """


def _send_email(to_email, subject, plain_body, html_body):
    if not to_email:
        print("Email skipped: recipient is empty.")
        return

    host, port, username, password, use_tls, from_email = _smtp_config()
    if not host:
        print("Email skipped: SMTP_HOST not configured.")
        return

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"]    = from_email
    msg["To"]      = to_email
    msg.set_content(plain_body)
    msg.add_alternative(html_body, subtype="html")

    try:
        with smtplib.SMTP(host, port, timeout=20) as server:
            if use_tls:
                server.starttls()
            if username:
                server.login(username, password)
            server.send_message(msg)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"SMTP ERROR sending to {to_email}:", e)


def send_booking_confirmation_emails(
    *,
    doctor_email: str,
    doctor_name:  str,
    patient_email: str,
    patient_name:  str,
    date:  str,
    slot:  str,
    mode:  str,
):
    subject = f"Booking Confirmed – {date} {slot}"

    # Patient
    _send_email(
        patient_email,
        subject,
        f"Hello {patient_name},\n\nYour appointment with {doctor_name} is confirmed.\nDate: {date}\nTime: {slot}\nMode: {mode}",
        _patient_html(patient_name, doctor_name, date, slot, mode),
    )

    # Doctor
    _send_email(
        doctor_email,
        subject,
        f"Hello Dr. {doctor_name},\n\nNew appointment booked.\nPatient: {patient_name}\nDate: {date}\nTime: {slot}\nMode: {mode}",
        _doctor_html(doctor_name, patient_name, date, slot, mode),
    )