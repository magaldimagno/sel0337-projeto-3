"""
Checkpoint 1 - Código Blink que será executado no Boot da Raspberry Pi
Eduardo Magaldi Magno - 15448780
Lucas Garcia Pereira - 15496307
"""

import RPi.GPIO as GPIO
import time

# Desabilita avisos e define o padrão BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configura o pino GPIO 23 como saída digital para controlar o LED
GPIO.setup(23, GPIO.OUT)
estado = False  # Estado inicial do LED

try:
    while True:
        GPIO.output(23, estado)  # Atualiza o estado do LED
        if estado:
            print("LED aceso")
        else:
            print("LED apagado")
        estado = not estado  # Alterna o estado do LED
        time.sleep(2)  # Aguarda 2 segundos
except KeyboardInterrupt:
    # Trata a interrupção por teclado (CTRL+C) de forma segura
    print("\nPrograma interrompido pelo usuário.")
finally:
    # Libera e reseta os pinos GPIO para o estado seguro padrão antes de encerrar
    print("Limpando configurações do GPIO.")
    GPIO.cleanup()
