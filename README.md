# PWMDC
Postfix+Web+Mailman Docker Compose

## 1 - Initial configuration
```
sudo apt update
sudo apt dist-upgrade
```
Install manager for certificates
```
sudo snap install --classic certbot
```
Create certificats that will **automatically update** with the following command
```
sudo certbot certonly --standalone --cert-name 6green.eu -d 6green.eu -d www.6green.eu -d private.6green.eu -d mail.6green.eu
```

## 2 - Project setup
Create the basic structure and clone the docker compose template. Be root
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
Create a folder for shared part between projects
```  
mkdir /opt/projects/shared
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

```
chmod 777 ./
```

Now it is possible to upload the dictionary that you can create from the template in this folder (*/opt/projects/PROJECT/PWMD-Compose/config_templates/dictionary-EXAMPLE.json*).
You can generate random key for dictionary with 
```
gpg --gen-random 2 20 | base64
```

Now, after dictionary have been uploaded, revoke permission for everyone and run the python script that instantiate configurations files
```
chmod 700 ./
cd ..
python3 template_deployer.py
```

### Certificates  
You will need certificate for your domain. Install **Certbot** and generate your certificate for each domain and subdomain that is needed  
```  
sudo certbot certonly --standalone --cert-name example.eu -d example.eu -d www.example.eu -d private.example.eu -d mail.example.eu  
```  
This docker compose will need at leas www, mail and private subdomains. Your certificates are now in */etc/letsencrypt/live/{{PUBLIC_SITE_DOMAIN}}/* (In this case*/etc/letsencrypt/live/example.eu/*) and will be authoritative for all domain you inserted the previous command.

## 3 - Mongo DB
Create the shared mongodb instance
```
cd /opt/projects/shared
mkdir mongo
cd mongo
mkdir data


touch docker-compose.yaml
nano docker-compose.yaml
```

Copy the following content inside the docker-compose.yaml file, changing the password
```
version: '3.1'

services:

  mongo:
    image: mongo
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: password
    volumes:
      - /opt/projects/shared/mongo/data:/data/db
    ports:
      - "130.251.17.118:27017:27017"
```

Then start mongo DB
```
docker compose up -d
```

## 4 - Start the docker compose
We are ready to start the composition of services for the project. The first time we run it, we need to start through the file *./start.sh* , the reason is that there are some configurations steps that still need to be done (you can open and see what it does)
```
cd /opt/projects/6green/PWMD-Compose/
chmod +x start.sh
./start.sh
```

If you need to stop the entire compose run (inside the project folder):
```
docker compose down
```
and to restart it you can use 
```
docker compose up
```

To stop a single service (maybe you need to build it or a configuration file has been changed)
```
docker compose stop <service_name>
```
and then 
```
docker compose start <service_name>
```
or
```
docker compose up
```
## 5 -  Build a service
In this docker compose 2 services are build (Postfix and Nginx), the others are downloaded and configured throught volumes mounting.
If you need to change a build configuration you can edit the Dockerfile in the relative service folder and then run (to build all services, 2 in this compose)
```
docker compose build --no-cache
```
Otherwise to build a single service 
```
docker compose build --no-cache <service_name>
```

Then the **next time this service is started**, it will use the new builded image.

## 6 - Links  
Mailman web: http://domain.eu:8000/  
  
Public portal: https://domain.eu/ http://domain.eu/ http://www.domain.eu/ https://www.domain.eu/  
  
Private portal: https://private.domain.eu/ http://private.domain.eu/  
  
Mail are relayed to users into virtusertable, which template is in config_templates/virtusertable-template.jinja  (Example info@domain.eu -> yourPrivate@mail.eu)  
  
## 7 -Mailman-Web usage  
Access from your private network to   
```  
http://mail.domain.eu/  
```  
Log in using the credentials you have chosen inside the dictionary. The email confirmation will be sent to *info@yourdomain.eu* (Check the linked mail to info@...).

## 6 - Advanced configuration

### 6.1 - Nginx configuration
Nginx is used as reverse proxy, the configuration is copied inside the relative container during the container build. For this reason if you need to change it, you'll need to edit (AFTER configurations files have been deployed, see section 2)
```
./nginx/nginx.conf
```
Then build again the container's image and restart the service (see section 4)

### 6.2 - Postfix configuration

???

### 6. - Volumes configuration files
All configurations files are mounted from the host machine as volumes. You can find them into 
```
mkdir -p /opt/projects/{{PROJECT_NAME}}/volumes/
```
**NOTE**: a very important role in the configuration role is manage by the docker compose file that is generated from the template, using variables in the dictionary.

### Update virt user table (Postfix)
```
cd /opt/projects/{{PROJECT_NAME}}/volumes/postfix/
```
Edit the virt user table as you want (*/opt/projects/{{PROJECT_NAME}}/volumes/postfix/virtusertable*).
Then run the script
```
chmod +x update_virt_user_table.sh
./update_virt_user_table.sh
```


