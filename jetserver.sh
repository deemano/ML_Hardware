#!/bin/bash
#!/bin/python3

sudo systemctl daemon-reload
sudo systemctl start jetserver.service
cd /home/deeman/jet
export FLASK_APP=jet.py
python3 jet.py
