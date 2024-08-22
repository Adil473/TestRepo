
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

email=$(vault kv get -field=email secret/my_secret)
password=$(vault kv get -field=password secret/my_secret)

echo "export EMAIL=$email" > credentials/secrets.sh
echo "export PASSWORD=$password" >> credentials/secrets.sh

chmod +x credentials/secrets.sh
#contents of secrets-output

ls -l credentials

cat credentials/secrets.sh
echo "Fetched email: $EMAIL"
echo "Fetched password: $PASSWORD"
