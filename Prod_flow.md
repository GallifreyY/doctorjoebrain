### Prod_flow

> backend:

1. move "back-end" file to "doctorjoe" in prod server

2. run build.sh in prod server

3. run the following commands in prod server:

   ```powershell
   $ lsof -i:5000  #search PID
   $ kill -9 (PID)
   $ service appstart restart
   ```

> front-end:

1. run build command in your own computer

   ```po
   npm run build
   ```

2. move "dist" file to \prod in prod server