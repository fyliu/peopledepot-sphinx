# Ssh

## Overview

Secure shell (SSH) is a secure way to log into remote systems via a terminal interface.

## Install

Windows users should install wsl with ubuntu. Then run `sudo apt-get install ssh`
Mac and linux users may already have it installed.

## Basics

To log into an ssh host

```bash
ssh <user>@<host>[:<port>]
```

user is the username to login as
host is the hostname or IP
port is 22 by default if unspecified, or can be specified if it's different

The default way to login will prompt you for a password. It won't show the characters as you type them, so just type and press Enter. Now your terminal is showing the remote system. You can run commands on the remote system, such as `ls` to list the directory contents.

To quit the ssh session

```bash
exit
```

## Keys

The preferred way to authenticate with the ssh server is using public key cryptography.

## Config file
