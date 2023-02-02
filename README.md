# PWMD-Compose
Postfix+Web+Mailman on Docker Compose

## Pre installation steps (1/3)

### Docker installation

???

### Certificates
You will need certificate for your domain. Install **Certbot** and generate your certificate for each domain and subdomain that is needed
```
sudo certbot certonly --standalone --cert-name 6green.eu -d example.eu -d www.example.eu -d private.example.eu -d mail.example.eu
```
This docker compose will need at leas www, mail and private subdomains. Your certificates are now in */etc/letsencrypt/live/{{PUBLIC_SITE_DOMAIN}}/* and will be authoritative for all domain you inserted the previous command.

## Setup (2/3) - Download repo in the right folder
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
cd PWMD-Compose/s
```

## Configuration (3/3)
Edit the file */opt/projects/PROJECT/PWMD-Compose/config_templates/dictionary-EXAMPLE.json* replacing values with YOUR values. 

NOTE: PROJECT_NAME must be the same name used when you have created the folder  /opt/projects/PROJECT

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
And finally you can start the docker compose through
```
./start.sh
```

## Links
Mailman web: http://domain.eu:8000/

Public portal: https://domain.eu/ http://domain.eu/ http://www.domain.eu/ https://www.domain.eu/

Private portal: https://private.domain.eu/ http://private.domain.eu/

Mail are relayed to users into virtusertable, which template is in config_templates/virtusertable-template.jinja  (Example info@domain.eu -> yourPrivate@mail.eu)

## Mailman-Web usage
Access from your private network to 
```
http://domain.eu:8000/
```
Log in using the credentials you have chosen inside the dictionary. The email confirmation will be sent to *info@yourdomain.eu* (Check the linked mail to info@...).

## Logs
### Postfix
-*/opt/projects/{{PROJECT_NAME}}/logs/postfix/*
### Mailman-web
-*/opt/projects/{{PROJECT_NAME}}/web/logs*
