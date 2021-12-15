import random 
import string

# Genera codigo random de 4 digitos para utilizar como codigo de verificacion 
def code_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))