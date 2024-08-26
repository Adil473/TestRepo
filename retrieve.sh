
# export VAULT_ADDR='http://192.168.1.103:8200'
# export VAULT_TOKEN='myroot'

# # Fetch credentials from Vault and store them in variables
# EMAIL=$(vault kv get -field=email secret/my_secret)
# PASSWORD=$(vault kv get -field=password secret/my_secret)

# # Save credentials to files
# echo "$EMAIL" > credentials/email.txt
# echo "$PASSWORD" > credentials/password.txt

# # Print the credentials for debugging (ensure this is secure and not used in production)
# echo "Fetched Email: $EMAIL"
# echo "Fetched Password: $PASSWORD"




#  ==================================================== #
export VAULT_ADDR='http://192.168.1.103:8200'
export VAULT_TOKEN='myroot'

EMAIL=$(vault kv get -field=email secret/my_secret)
PASSWORD=$(vault kv get -field=password secret/my_secret)
PG_USER=$(vault kv get -field=PG_USER secret/my_secret)
PG_PASS=$(vault kv get -field=PG_PASS secret/my_secret)
PG_DB=$(vault kv get -field=PG_DB secret/my_secret)

mkdir -p credentials
chmod +x credentials
echo "$EMAIL" > credentials/email.txt
echo "$PASSWORD" > credentials/password.txt
echo "$PG_USER" > credentials/pg_user.txt
echo "$PG_PASS" > credentials/pg_pass.txt
echo "$PG_DB" > credentials/pg_db.txt

# Print the credentials for debugging (ensure this is secure and not used in production)
echo "Fetched Email: $EMAIL"
echo "Fetched Password: $PASSWORD"
echo "Fetched PG_USER: $PG_USER"
echo "Fetched PG_PASS: $PG_PASS"
echo "Fetched PG_DB: $PG_DB"

# echo "export EMAIL=$email" > credentials/secrets.sh
# echo "export PASSWORD=$password" >> credentials/secrets.sh

# chmod +x credentials/secrets.sh
# #contents of secrets-output

ls -l credentials

# cat credentials/secrets.sh
# echo "Fetched email: $EMAIL"
# echo "Fetched password: $PASSWORD"
