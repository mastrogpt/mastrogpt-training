# saves users2.txt in 1pw ollama users2.txt
: > _users2.caddy
while IFS=: read -r user pass; do
  echo "$user $(caddy hash-password --plaintext "$pass")" >> "_users2.caddy"
done < "users2.txt"
bash getusers.sh eri
bash getusers.sh draco
cat eri/* draco/* >_users.caddy
sudo cp _users2.caddy /etc/caddy/_users2.caddy
sudo cp _users.caddy /etc/caddy/_users.caddy
sudo cp Caddyfile /etc/caddy/Caddyfile
sudo chmod 644 /etc/caddy/*
sudo systemctl restart caddy
