#!/usr/bin/env python
"""
Created by Omer ben shushan
App name: pyPanel Cli
Description: create new account
"""
import sys,os
def remove_acct_from_list(account_name):
	f = open("accounts_list", "r")
	new_accounts_list = ""
	contents = f.readlines()
	f.close()
	with open('accounts_list', 'r+') as accounts_list:
		for account in accounts_list:
			if account_name+'\n' != account and account != '\n':
				#contents =+ account_name
				new_accounts_list = new_accounts_list + account
		print("new account list")
		print(new_accounts_list)
		# delete file content
		with open('accounts_list', 'w'): pass
		# add new content to file
		accounts_list.write(new_accounts_list)

def remove_acct(account_name):
	with open('accounts_list') as accounts_list:
		accounts = accounts_list.readlines()
		if account_name + "\n" in accounts:
			delete_it = raw_input(account_name + " is going to be removed are you sure? (y/N)")
			if delete_it != 'y':
				print(account_name + " is not going to be deleted!")
				return False
				exit
			else:
				print("you agree to delete " + account_name + " account")
				os.system("userdel " + account_name)
				os.system("rm -rf /home/" + account_name)
				# delete from list
				remove_acct_from_list(account_name)
				return True;
		else:
			print("Account not exists!")
			return False
			exit
	
	# delete from system
	os.system("/usr/sbin/userdel -r " + account_name)

	#delete from accounts_list and domains file

if __name__  == "__main__":
	account_name = raw_input("Please enter account name: \n")
	remove_acct(account_name)