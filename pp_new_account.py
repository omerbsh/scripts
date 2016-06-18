#!/usr/bin/env python
"""
Created by Omer ben shushan
App name: pyPanel Cli
Description: create new account
"""
import sys,os
import re

import lib.pp_validation
from lib.pp_create_nginx_conf import create_nginx_conf

def create_acct(domain_name):
        #account name validation
        domain_string = re.split("[^a-zA-Z0-9]*",domain_name)
        
        account_name = ""
        
        for acct in domain_string:
                account_name += acct
                
        if re.match("^[0-9a-zA-Z]+$" , account_name) == False:
            print "this account name is not valid (have to be with letters and numbers only"
            exit
        
        #account name is limited for 8 chars
        account_name = account_name[:8]
        accept_creation = raw_input("account name is: " + account_name + " please eneter y to continue: ")
        
        if accept_creation != "y":
            	#print "bye bye!"
            	#return False
		account_name = raw_input("write account name by youself:")
		account_name = account_name[:8]
        
        dir_path = "/home/" + account_name
        #check if home folder already exist
        if not os.path.isdir(dir_path):
            #create new user
            cmd = os.system("adduser -s /sbin/nologin "+ account_name)
	    # write new account to accounts list
	    accounts_lst = open('accounts_list', 'a')
	    accounts_lst.write(domain_name + " " + account_name  + "\n")
            accounts_lst.close()
	    #create account home directory , and secondery directories
            os.makedirs(dir_path + "/public_html")
            os.makedirs(dir_path + "/access_logs")
            #check if the user creation faild
            if cmd == 1:
                print "for some reason I could not create a user " + account_name + " please check this and come back"
                exit
            #change dir owner
            os.system("chown -R " + account_name + "." + account_name + " " + dir_path)
            print("the account  %s  has been created. " % account_name )
            os.system("chmod 755 /home/%s" % account_name)
            os.system("service nginx restart")
            os.system("service php-fpm restart") 
            return account_name
        else:
            print("this folder is exists: " + account_name)
            print("please write new ")

            return False
            return False

domain_name = raw_input("Please enter the main domain of this account: \n")


if lib.pp_validation.domain_validation(domain_name):
    #call to create acct function
    account_name = create_acct(domain_name)

    if create_acct is not False:
        create_nginx_conf(account_name , domain_name)
    else:
		print "Error with ngnix configuration file creation"
		exit
else:
    print "Sorry the domain is not valid , bye!"
    exit
