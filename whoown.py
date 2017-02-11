#!/usr/bin/env python
"""
Created by Omer ben shushan
App name: pyPanel Cli
Description: create new account
"""
import sys

accounts_file = "account_domains"
input_domain = sys.argv[1]

with open( accounts_file ) as f:
	accounts = f.readlines()

for acc in accounts:
	acc_domain = acc.split(" ", 1)
	# if domain name is equal to the user input
	if input_domain == acc_domain[0]:
		print acc_domain[1].rstrip('\n')
