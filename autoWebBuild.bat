cd ./brain/
call npm run build
cd ..

set winscp="C:\Program Files (x86)\WinSCP\WinSCP.exe"

%winscp% /console /command "option confirm off" "open root:ca$hc0w1@testhpi.eng.vmware.com:22" "put .\brain\dist /home/doctorjoe/prod/" "put .\back-end\src /home/doctorjoe/prod/" "call service appstart restart" "exit" /log=log_winscp.txt

