"""
Checkpoint 1 - Script de desligamento em ExecStop
Eduardo Magaldi Magno - 15448780
Lucas Garcia Pereira - 15496307
"""

import RPi.GPIO as GPIO

# Desabilita avisos e define o padrão BCM
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Configura o pino GPIO 23 como saída e o força para nível baixo (desliga o LED)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, False)

# Libera e reseta as configurações da GPIO
GPIO.cleanup()
print("Serviço finalizado: LED desligado e GPIOs liberadas.")