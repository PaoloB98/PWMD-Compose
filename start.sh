mkdir -p /opt/projects/6green/DMPW-compose/certs/
sudo cp -R /etc/letsencrypt/archive/6green.eu/* /opt/projects/6green/PWMD-Compose/nginx
docker compose build --no-cache
docker compose up -d
docker exec -i mailman-web /bin/bash -c "DJANGO_SUPERUSER_PASSWORD=my_password ./manage.py createsuperuser --no-input --username=mailadmin --email=admin@example.234es.it"