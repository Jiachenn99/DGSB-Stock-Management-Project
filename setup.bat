@ECHO OFF
pip install virtualenv
virtualenv virtual_environment
.\virtual_environment\Scripts\activate & pip install -r requirements.txt
PAUSE
echo Installation Complete
