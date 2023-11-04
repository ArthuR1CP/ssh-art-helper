# SSH Helper

**SSH Helper** is a Python script that simplifies SSH connections to multiple hosts and allows you to execute commands on those hosts remotely using the Paramiko library.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Configuration](#configuration)

## Features

- Connect to multiple hosts via SSH.
- Execute commands on remote hosts.
- Automatically add host SSH keys.
- Logging of executed commands and results.

## Prerequisites

Before using SSH Helper, ensure you have the following:

- Python 3.x
- Paramiko library
- SSH key (or password) for authentication
- A list of host IP addresses or domain names in an inventory file

## Usage

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/your-username/ssh-helper.git
   ```

2. Install the Paramiko library if you haven't already:

   ```shell
   pip install paramiko
   ```

3. Prepare an inventory file (e.g., hosts) with a list of host IP addresses or domain names, one per line.

4. Modify the script to set your key_filename, username, and any other configurations as needed.

5. Run the script:

    ```shell
    python ssh_helper.py
    ```

## Configuration
You can customize the script's behavior by modifying the following variables in the script:

`key_filename`: Path to your SSH key for authentication.

`username`: The username for SSH connections (e.g., 'ec2-user' for AWS EC2).

`password`: If not using SSH keys, you can set a password for authentication.
