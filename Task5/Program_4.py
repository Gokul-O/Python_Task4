import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_bangladesh_mobile(mobile):
    pattern = r'^(?:\+88|88)?01[3-9]\d{8}$'
    return re.match(pattern, mobile) is not None

def validate_usa_telephone(telephone):
    pattern = r'^\+1-\d{3}-\d{3}-\d{4}$'
    return re.match(pattern, telephone) is not None

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    return re.match(pattern, password) is not None

# Testing the functions
emails = ["test@example.com", "invalid-email", "name@domain.co"]
bangladesh_mobiles = ["+8801712345678", "01712345678", "088012345678"]
usa_telephones = ["+1-123-456-7890", "123-456-7890", "+1-123-4567-890"]
passwords = ["A1b2c3d4e5f6g7h8", "aA1@defgH2ijklmn", "invalidpassword", "Short1!"]

for email in emails:
    print(f"Email '{email}' is valid: {validate_email(email)}")

for mobile in bangladesh_mobiles:
    print(f"Bangladesh Mobile '{mobile}' is valid: {validate_bangladesh_mobile(mobile)}")

for telephone in usa_telephones:
    print(f"USA Telephone '{telephone}' is valid: {validate_usa_telephone(telephone)}")

for password in passwords:
    print(f"Password '{password}' is valid: {validate_password(password)}")
