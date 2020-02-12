#!/bin/bash
pip --version

if [ $? -eq 1 ]
then
    echo "Pip is not found, installing pip"
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py && python3 -m pip install --upgrade pip
    if [$? -eq false]
    then
        echo "Installed pip."
        pip install virtualenv
    else
        echo "Could not install pip, exiting with code $?"
        read -n1 -r -p "Press any key to continue..." 
    fi
else
    echo "Pip is installed"
    pip install virtualenv
    if [ $? -eq 1 ] 
    then
        echo "Virtual environment module failed to install, exiting with code $?"
        read -n1 -r -p "Press any key to continue..." 
    else
       echo "Virtual environment module installed." 
    fi
fi

virtualenv ../virtual_environment && source ../virtual_environment/bin/activate && pip install -r requirements.txt
if [ $? -eq 1 ]
then
   echo "Exiting with error code $?"
   read -n1 -r -p "Press any key to exit..." 
   
else
    echo "All packages installed"
    read -n1 -r -p "Press any key to continue..." 
fi

