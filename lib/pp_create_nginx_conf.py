#!/usr/bin/env python
"""
Created by Omer ben shushan
App name: pyPanel Cli
Description: create ngnix configuration file
"""
import os

def create_nginx_conf(account_name , domain_name):
    #open nginx conf file template
    conf_file = open("./templates/nginx_server_block")
    data = conf_file.read();
    #replace vars
    data = data.replace("###ACCOUNT_NAME###" , account_name)
    data = data.replace("###DOMAIN###" , domain_name)
    #new file path
    new_conf_file_path = "/etc/nginx/sites-available/" + account_name + ".conf"
    os.system("ln -s /etc/nginx/sites-available/" + account_name + ".conf /etc/nginx/sites-enabled/")
    conf_file.close()
    # new conf file
    new_conf_file = open(new_conf_file_path , "w")
    #write data into new file
    if new_conf_file.write(data):
        # create symlink 
        #restart nginx and return true
        os.system("service nginx restart")
        return True
    else:
        return False

def create_phpfpm_conf(account_name):
    #open php-fpm conf file template
    conf_file = open("./templates/phpfpm_conf")
    data = conf_file.read();
    # unique php fpm port counter
    unique_port_file = open("./lib/phpfpm_counter", "rw+")
    unique_port = unique_port_file.read()
    unique_port = int(unique_port) + 1
    unique_port = str(unique_port)
    #unique_port = unique_port.encode("utf-8")
    # truncate file
    print("truncate file ./lib/phpfpm_counter")
    os.system("cat /dev/null > ./lib/phpfpm_counter")
    print("new port: " + unique_port)
    unique_port_file.write("9015".encode("utf-8"))
    unique_port_file.close()
    #replace vars
    data = data.replace("###ACCOUNT_NAME###" , account_name)
    data = data.replace("###UNIQUE_PORT###" , unique_port)
    #new file path
    new_conf_file_path = "/etc/php/7.1/fpm/pool.d/" + account_name + ".conf"
    print new_conf_file_path
    new_conf_file = open(new_conf_file_path , "w")
    conf_file.close()
    #write data into new file
    if new_conf_file.write(data):
        #restart nginx and return true
        os.system("service php-fpm restart")
        return True
    else:
    	return False

    conf_file.close()
