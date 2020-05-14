
@ECHO OFF

REM should check whether Python is installed.

REM checking whether pip is installed
pip --version

REM install pip if doesnt exist else install virtualenv
IF ERRORLEVEL 0 (python -m pip install --upgrade pip & pip install virtualenv & echo Installed virtualenv)
IF ERRORLEVEL 1 (python get-pip.py && py -m pip install --upgrade pip & echo Installed pip)

REM Creating the virtual environment
virtualenv ../virtual_environment && ..\virtual_environment\Scripts\activate && pip install -r requirements.txt && IF ERRORLEVEL 0 (echo VIRTUAL ENVIRONMENT SUCCESSFULLY CREATED & echo REQUIREMENTS INSTALLED)




