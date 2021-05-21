import getpass
import paramiko

hostname = "localhost"
port = 22

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.load_system_host_keys()

username = input("Username: ")
password = getpass.getpass(prompt="Enter password: ")
cmd = "code ."
ssh_client.connect(hostname, port, username, password)
stdin, stdout, stderr = ssh_client.exec_command(cmd)
print(stdout.read())
