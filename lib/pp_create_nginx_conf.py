#!/usr/bin/env python
"""
Created by Omer ben shushan
App name: pyPanel Cli
Description: create ngnix configuration file
"""
def create_nginx_conf(account_name , domain_name):
    #open nginx conf file template
    conf_file = open("/scripts/templates/nginx_server_block")
    data = conf_file.read();
    #replace vars
    data = data.replace("###ACCOUNT_NAME###" , account_name)
    data = data.replace("###DOMAIN###" , domain_name)

    #new file path
    new_conf_file_path = "/etc/nginx/conf.d/" + account_name + ".conf"
    new_conf_file = open(new_conf_file_path , "w")

    #write data into new file
    if new_conf_file.write(data):
        #restart nginx and return true
        os.system("service nginx restart")
    	return True
    else:
    	return False

    conf_file.close()
