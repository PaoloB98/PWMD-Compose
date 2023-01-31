# PWMD-Compose
Postfix+Web+Mailman on Docker Compose

## Setup
Be root
```
sudo su
```
Create a folder projects in opt
```
mkdir /opt/projects
```
Create a folder for your PROJECT
```
mkdir /opt/projects/PROJECT
```
Enter the folder
```
cd /opt/projects/PROJECT
```
Clone this repo
```
git clone https://github.com/PaoloB98/PWMD-Compose
```
Enter the folder 
```
cd PWMD-Compose/
```
Edit the file /opt/projects/PROJECT/PWMD-Compose/config_templates/dictionary-EXAMPLE.json replacing values with YOUR values. NOTE: PROJECT_NAME must be the same name used when you have created the folder  /opt/projects/PROJECT

Then rename this template in
```
mv ./config_templates/dictionary-EXAMPLE.json ./config_templates/dictionary.json
```
Now (Having installed python) run this script that will generate configuration files for docker's containers
```
python3 ./template_deployer.py
```
Give execution permission to the start file
```
chmod +x start.sh
```
And finally you can start the docker compose throgh
```
./start.sh
```

## Log
For each postfix instance you can find the log in /var/log/postfix/{{PROJECT_NAME}}/
