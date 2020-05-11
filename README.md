# DGSB-Stock-Management-Project
**__SEGP Group 3A Members__**
1. Lee Ze-Cong
2. Loh Sheng Yong
3. Choong Jiachenn
4. Khizar Azam Syed
5. Keith Arogo Owino

# Description
A web-based application to keep track of stock records, and provide reminders on low stock counts. Developed for Durian Garden as part of our Software Engineering Group Project (SEGP)

# Setup Locally
### Cloning
This repository can be cloned via HTTPS using the command below:
```
$ git clone https://github.com/Jiachenn99/DGSB-Stock-Management-Project.git
```

### Installing required packages
#### Prerequisites 
**Python 3.6 and above** should be installed on your system. To check whether Python is installed on your system, open your terminal (`cmd for Windows, Bash for Linux/MacOS/Unix`), and run 
```
python3 --version
```
or
```
python --version 
```
or
```
py --version
```

If a `command not found` error appears, please refer to the link below to download Python for your system:

https://www.python.org/downloads/source/

#### On Windows
1. Navigate to the cloned repository (`DGSB-Stock-Management-Project`)
2. Navigate to the `Setup` folder.
3. Double click `windows_setup.bat`
4. The installation for required packages and virtual environment should proceed.

#### On Linux / Unix / MacOS
1. Open the terminal (Bash)
2. Navigate to the cloned repository (`/DGSB-Stock-Management-Project/Setup`)
3. Type in `./linux_mac_setup.sh` and press ENTER
4. The installation for required packages and virtual environment should proceed.

All required packages and dependencies will be installed into a virtual_environment named `virtual_environment`

#### Installing XAMPP
To run locally, we are using XAMPP that provides us with the interface to host a simple mySQL server alongside the a Apache Web Server. To install XAMPP, simply head to: https://www.apachefriends.org/download.html to download the distribution that fits your operating system.

# Running our Code Locally
Ensure you are in the project's root directory (DGSB-Stock-Management-Project/)
### Enter the virtual environment
Using a command line interface, perform the commands below:
#### On Command Prompt
```
> .\virtual_environment\Scripts\activate
```
#### On Bash/Powershell
```
$ source virtual_environment/Scripts/activate
```
For confirmation that you have entered the virtual_environment, the command line should display in brackets the virtual_environment name:
```
(virtual_environment) <path>\DGSB-Stock-Management-Project>
```

### Starting the web server and database server
Ensure you have XAMPP Control Panel installed, run the application, and start two services:
1. Apache
2. mySQL

### Creating a database
Using XAMPP Control Panel, click the 'Admin' button on the mySQL service. Then, add a database named 'duriangarden' using phpMyAdmin.

### Running migrations
Since the database is newly created, it does not have the fields or tables that you will require, in that case, follow the steps below:
1. Make sure you are in the virtual_environment, then, run `python manage.py migrate` to apply all migrations.
2. The migrations should be applied, and you can check on phpMyAdmin whether the tables are created.

### Starting the Django app
Run this in the command line:
```
python manage.py runserver
```
The server should start, and you can access it in a web browser with:
```
localhost:8000
```
