import paramiko

hostname = "SERVER_IP"
username = "USER"
key_filename = 'path/to/folder'

commands = [
    "pwd",
    "yum install httpd -y",
    "service httpd start",
    "mv /index.html /var/www/html"
]

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username,key_filename=key_filename )
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

#Copy file to remote server

sftp_client=client.open_sftp()
sftp_client.put('path/to/folder/index.html' ,'/index.html')
sftp_client.close()

for command in commands:
    print("="*50, command, "="*50)
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)
