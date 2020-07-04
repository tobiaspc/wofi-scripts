#!/bin/python3
from argparse import ArgumentParser
import subprocess
import json
import os

ssh_config_file = "~/.ssh/config"

# Returns a list of all hosts
def get_hosts():

    hosts = []

    with open(os.path.expanduser(ssh_config_file)) as f:
        content = f.readlines()
    
    for line in content:
        line = line.lstrip()
        if line.startswith('Host '):
            for host in line.split()[1:]:
                hosts.append(host)

    # Removes duplicate entries
    hosts = list(set(hosts))
    hosts.sort()

    return hosts

# Returns a newline seperated UFT-8 encoded string of all ssh hosts
def parse_hosts(hosts):
    return "\n".join(hosts).encode("UTF-8")

# Executes wofi with the given input string
def show_wofi(hosts):

    command="wofi -p \"SSH hosts: \" -d -i --hide-scroll"
    
    process = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    return process.communicate(input=hosts)[0]

# Returns the id of the window that was selected by the user inside wofi
def parse_id(hosts, selected):
    selected = int(selected.decode("UTF-8"))
    return str(hosts[selected].get('id'))

# Switches the focus to the given id
def ssh_to_host(host, terminal):
    command=terminal + " 'ssh " + host + "'"
    
    process = subprocess.Popen(command,shell=True)

# Entry point
if __name__ == "__main__":
    
    parser = ArgumentParser(description="Wofi based ssh launcher")
    parser.add_argument("terminal")
    args = parser.parse_args()

    hosts = get_hosts()

    parsed_hosts = parse_hosts(hosts)
    
    selected = show_wofi(parsed_hosts)

    selected_host = hosts[int(selected)]

    ssh_to_host(selected_host, args.terminal)