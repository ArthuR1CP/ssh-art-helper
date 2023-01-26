from fabric import Connection, task

def populate_hosts(inventory):
    hosts_list = []
    with open(inventory, "r") as inventory_file:
        for host in inventory_file:
            host  = host.rstrip("\n")
            hosts_list.append(host)
    return hosts_list

@task
def command(c):
    result = c.run('date')
    print(result.stdout)

if __name__ == "__main__":


    hosts = populate_hosts("hosts")
    username = 'ec2-user' # AWS EC2 default username 
    key_filename = '' # path to your key
    password = ''

    for host in hosts:
        c = Connection(host=host, user=username, connect_kwargs={'key_filename': key_filename})
        command(c)

