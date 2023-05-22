import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import webbrowser

def send_email(sender_email, app_password, recipient_email, subject, message):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create a multipart message
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = recipient_email
    email_message['Subject'] = subject

    # Add the message body
    email_message.attach(MIMEText(message, 'plain'))

    # Create an SMTP session
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(email_message)
        print("Email sent!")


def show(df):
    employee_id = int(input("Employee ID: "))
    employee_info = df[df['ID'] == employee_id]  # Filter DataFrame based on employee ID
    
    if employee_info.empty:
        print("Employee not found.")
        return
    
    employee_row = employee_info.iloc[0]  # Get the first row (assuming unique IDs)
    
    # Extract employee information from the DataFrame
    employee_id = employee_row['ID']
    department = employee_row['Dept']
    job = employee_row['Job']
    name = employee_row['Name']
    surname = employee_row['Surname']
    final_salary = employee_row['Final Salary']
    
    # Fill in the template mail message with employee information
    template = f"Dear {name} {surname},\n\n" \
               f"We are pleased to inform you that your employment details have been updated. Here are the details:\n" \
               f"Employee ID: {employee_id}\n" \
               f"Department: {department}\n" \
               f"Job: {job}\n" \
               f"Name: {name}\n" \
               f"Surname: {surname}\n" \
               f"Final Salary: {final_salary}\n" \
    
    print(template)
    recipient_email = input("Employee mail: ")
    sender_email = input("Company mail: ")
    webbrowser.open("https://myaccount.google.com/security")
    app_password = input("Take GMail app password from browser and paste here: ") 
    subject = "Employment information"
    message = template

    send_email(sender_email, app_password, recipient_email, subject, message)

if __name__ == "__main__":
    show()

