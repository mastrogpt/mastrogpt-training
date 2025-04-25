HOST=${1:-host}
mkdir -p  $HOST
ssh $HOST.geppetto.cloud kubectl -n nuvolaris get whiskuser -o json |\
jq -r '.items[].spec.auth' | awk -F: '{print $1 " " $2}' |\
while read user pass; do
    if ! test -e $HOST/$user
    then echo "$user $(caddy hash-password --plaintext $pass)"  | tee $HOST/$user
    else echo "skip $user"
    fi
done

