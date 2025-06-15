bash getusers.sh eri
bash getusers.sh draco
cat eri/* draco/* >_users.caddy
sudo cp _users.caddy /etc/caddy/_users.caddy
sudo cp Caddyfile /etc/caddy/Caddyfile
sudo chmod 644 /etc/caddy/*
sudo systemctl restart caddy

