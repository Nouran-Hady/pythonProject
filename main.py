import netmiko
try:
    mycon=netmiko.ConnectHandler(ip='192.168.154.5',username='admin',password='cisco',device_type='cisco_ios',secret='cisco')
    mycon.enable()
    output=mycon.send_command('show running-config')
    print(output)
    mycon.disconnect()
except Exception as err:
    print(err)

