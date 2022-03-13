#!/usr/bin/env python3
#Device backup script

#Import modules
import datetime,pathlib,os,netmiko
from netmiko import ConnectHandler
from getpass import getpass

#Gather credentials
USERNAME = input('Username: ')
PASSWORD = getpass('Password: ')

#File information
filename = 'csrBackup.txt'
current_directory = pathlib.Path.cwd()
open_action = 'w'
backup_file = open(current_directory/filename,open_action)

#Device information
host = '192.168.108.254'
device = {'ip' : host,'username' : USERNAME, 'password' : PASSWORD, 'device_type' : 'cisco_ios'}

#Connect to device
device_connection = ConnectHandler(**device)
output = device_connection.send_command('show run')

#Copy device output to file
backup_file.write(output)
backup_file.close()
