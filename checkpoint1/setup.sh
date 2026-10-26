#!/bin/bash

DIR=$PWD

echo "Concedendo permissões de execução..."
chmod +x $DIR/blink_main.py
chmod +x $DIR/blink_stop.py

echo "Copiando o arquivo de serviço..."
sudo cp $DIR/blink_python.service /lib/systemd/system/

echo "Recarregando e habilitando o serviço..."
sudo systemctl daemon-reload
sudo systemctl enable blink_python

echo "Pronto! Iniciando o serviço para teste..."
sudo systemctl start blink_python