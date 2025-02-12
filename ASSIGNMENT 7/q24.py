
#24. Secure Password Validation

import re

def validate_password(password):
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*?]).{8,}$')
    return bool(pattern.match(password))

print(validate_password('Passw0rd!')) 
 # Output: True



