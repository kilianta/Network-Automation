# khai báo thư viện netmiko và datetime

from netmiko import ConnectHandler
from datetime import datetime
 
#khai báo thông số các thiết bị Cisco
Router_HCM= {
                     'device_type': 'cisco_ios',
                     'ip': '192.168.1.1',
                     'username': 'admin',
                     'password': 'admin',
                     'verbose': False,
                     }
Switch_HCM={
                     'device_type': 'cisco_ios',
                     'ip': '192.168.1.2',
                     'username': 'admin',
                     'password': 'admin',
                     'verbose': False,
                     }
# khai báo mảng gồm các tâ
all_devices=[Router_HCM,Switch_HCM]
current_time=datetime.now()
current_date=current_time.strftime("%d")
current_month=current_time.strftime("%m")
current_year=current_time.strftime("%Y")
for devices in all_devices:
 net_connect=ConnectHandler(**devices)
 net_connect.enable()
 command="copy running-config tftp://192.168.1.3/"
 send_bk_command = net_connect.send_command_timing(command)
 if ("Address or name of remote host" in send_bk_command):
  send_Enter= net_connect.send_command_timing("\n")
 if ("Destination filename" in send_Enter):
  index1=send_Enter.find("[")+1
  index2=send_Enter.find("]")
  device_hostname=send_Enter[index1:index2]
  send_Filename= net_connect.send_command_timing(device_hostname+"_"+current_date+"_"+current_month+"_"+current_year)
  if ("Error" in send_Filename):
   print (send_Filename)
 print("Success "+device_hostname)
