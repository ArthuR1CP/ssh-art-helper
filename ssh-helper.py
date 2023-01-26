import paramiko


client = paramiko.SSHClient() # Create an SSH client
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Add the host's ssh key automatically


username = 'ec2-user' # AWS EC2 default username 
key_filename = '' # path to your key
password = ''

client.connect(hostname='35.180.208.17', username='ec2-user', key_filename=key_filename) # you can use password inseat key_filename


stdin, stdout, stderr = client.exec_command('date')
print(stdout.read().decode())

# Close the connection
client.close()

