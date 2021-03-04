cd ./brain/
call npm run build
cd ..

set winscp="C:\Program Files (x86)\WinSCP\WinSCP.exe"
pause
%winscp% /console /command "option confirm off" "open root:vmwareca$hc0w@testhpi.eng.vmware.com:22" "put .\brain\dist /home/doctorjoe/prod/" "put .\back-end\src /home/doctorjoe/prod/" "call service appstart restart" "exit" /log=log_winscp.txt

