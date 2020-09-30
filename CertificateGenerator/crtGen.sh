
#!/bin/sh
#webCrtGen

##################################
### Certificate Generator
##################################

echo "Creat CSR&KEY"
openssl req -new -nodes -out newcerts/${HOSTNAME}.csr -keyout newcerts/${HOSTNAME}.key -days 1825 -config configfiles/openssl-main.cfg -subj /C=US/ST=California/L=PA/O=VMware/OU=EUCBU/CN=${HOSTNAME}

echo "Successfully created CSR&KEY"
echo "Generating Crt"

openssl ca -passin pass:testpassword -batch -out newcerts/${HOSTNAME}.crt -days 1825 -config configfiles/openssl-main.cfg -infiles newcerts/${HOSTNAME}.csr

echo "Crt Generated" 

##################################
### File Copy
##################################

cp newcerts/${HOSTNAME}.crt /etc/nginx/
cp newcerts/${HOSTNAME}.key /etc/nginx/

sed -i "s#/etc/nginx/.*\.crt#/etc/nginx/${HOSTNAME}\.crt#g" /etc/nginx/nginx.conf
sed -i "s#/etc/nginx/.*\.key#/etc/nginx/${HOSTNAME}\.key#g" /etc/nginx/nginx.conf
