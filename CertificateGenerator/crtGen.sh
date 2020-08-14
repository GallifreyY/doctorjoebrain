
#!/bin/sh
#webCrtGen

##################################
### Certificate Generator
##################################

echo "Creat CSR&KEY"
openssl req -new -nodes -out newcerts/${HOSTNAME}.csr -keyout newcerts/${HOSTNAME}.key -days 1825 -config configfiles/openssl-main.cfg -subj /C=US/ST=California/L=PA/O=VMware/OU=EUCBU/CN=djintelligence.eng.vmware.com

echo "Successfully created CSR&KEY"
echo "Generating Crt"

openssl ca -passin pass:testpassword -batch -out newcerts/${HOSTNAME}.crt -days 1825 -config configfiles/openssl-main.cfg -infiles newcerts/${HOSTNAME}.csr

echo "Crt Generated" 

##################################
### File Copy
##################################

cp newcerts/${HOSTNAME}.crt /etc/nginx/
cp newcerts/${HOSTNAME}.key /etc/nginx/

sed -i "s#djintelligence.eng.vmware.com#${HOSTNAME}#g" /etc/nginx/nginx.conf
