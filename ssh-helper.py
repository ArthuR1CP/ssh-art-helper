import paramiko
import logging
import contextlib

logging.basicConfig(level=logging.INFO)


def populate_hosts(inventory):
    hosts_list = []
    with open(inventory, "r") as inventory_file:
        for host in inventory_file:
            host  = host.rstrip("\n")
            hosts_list.append(host)
    return hosts_list


def run_command(client, command):
    with contextlib.closing(client.invoke_shell()) as channel:
        channel.exec_command(command)
        return channel.recv(1024).decode()

def command(client):
    stdin, stdout, stderr = client.exec_command('hostname')
    print(stdout.read().decode())

def command2(client):
    stdin, stdout, stderr = client.exec_command('date')
    print(stdout.read().decode())

if __name__ == "__main__":

    client = paramiko.SSHClient() # Create an SSH client
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Add the host's ssh key automatically

    hosts = populate_hosts("hosts")
    username = 'ec2-user' # AWS EC2 default username 
    key_filename = '' # path to your key
    password = ''

    for host in hosts:
        try:
            client.connect(hostname=host, username=username, key_filename=key_filename)
            cmd_hostname = run_command(client, 'hostname')
            cmd_date = run_command(client, 'date')
            logging.info(f'hostname: {cmd_hostname}')
            logging.info(f'date: {cmd_date}')
        except Exception as e:
            logging.error(f'An error occurred: {e}')
        finally:
            client.close()
