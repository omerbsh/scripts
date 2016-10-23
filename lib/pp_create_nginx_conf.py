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

<<<<<<< HEAD
    conf_file.close()
=======
>>>>>>> 70a7f67ad1f345b514cc13ea446dab3fcd35f1e3
    #write data into new file
    if new_conf_file.write(data):
        #restart nginx and return true
        os.system("service nginx restart")
<<<<<<< HEAD
        return True
    else:
        return False

def create_phpfpm_conf(account_name):
    #open php-fpm conf file template
    conf_file = open("/scripts/templates/phpfpm_conf")
    data = conf_file.read();
    #replace vars
    data = data.replace("###ACCOUNT_NAME###" , account_name)
    #new file path
    new_conf_file_path = "/etc/php-fpm.d/" + account_name + ".conf"
    new_conf_file = open(new_conf_file_path , "w")
    conf_file.close()
    #write data into new file
    if new_conf_file.write(data):
        #restart nginx and return true
        os.system("service php-fpm restart")
        return True
    else:
        return False
=======
    	return True
    else:
    	return False

    conf_file.close()
>>>>>>> 70a7f67ad1f345b514cc13ea446dab3fcd35f1e3
