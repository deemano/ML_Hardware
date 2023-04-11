#!/bin/bash

systemctl daemon-reload
systemctl start jetserver.service
cd /home/deeman/jet
export FLASK_APP=jet.py
python3 jet.py
