#!/usr/bin/env python
"""
Created by Omer ben shushan
App name: pyPanel Cli
Description: create ngnix configuration file
"""
import os,platform
import ConfigParser

# Created configuration file
def setup_software(conf_file_path):
	cfgfile = open(conf_file_path,'w')
	Config = ConfigParser.ConfigParser()
	dist_name = platform.dist()[0].lower()
	Config.add_section('configPath')
	if dist_name == 'ubuntu' or dist_name == 'debian':
		# create configuration for Ubuntu / Debian.
		if os.path.isdir('/etc/nginx/sites-available/') and os.path.isdir('/etc/nginx/sites-enabled/'):
			print('create configuration path for Ubuntu')
			Config.set('configPath','nginx_site_available','/etc/nginx/sites-available/')
			Config.set('configPath','nginx_site_enabled','/etc/nginx/sites-enabled/')
			Config.set('configPath','phpfpm_conf','/etc/nginx/sites-enabled/')
		else:
			print('create configuration path for CentOS')
			print("can't find Nginx configuration folder path.")
	elif dist_name == 'centos':
		# create configuration for CentOS
		if os.path.isdir('/etc/nginx/sites-available/') and os.path.isdir('/etc/nginx/sites-enabled/'):
			# create CentOS 2 dir's configuration
			Config.set('configPath','nginx_site_available','/etc/nginx/sites-available/')
			Config.set('configPath','nginx_site_enabled','/etc/nginx/sites-enabled/')
		elif os.path.isdir('/etc/nginx/conf.d/'):
			# create CentOS conf.d dir configuration
			Config.set('configPath','conf_d','/etc/nginx/conf.d/')
	else:
		print('Sorry your dist is not supported :(')
		manually_install = raw_input('Do you want to install manually [y/n]?')
		if manually_install.lower() == 'y':
			nginx_site_available = raw_input('nginx site available path:')
			nginx_site_enabled = raw_input('nginx site enabled path:')
			# set configuration path's
			Config.set('configPath','nginx_site_available', nginx_site_available)
			Config.set('configPath','nginx_site_enabled', nginx_site_enabled)
	Config.write(cfgfile)
	cfgfile.close()
if __name__ == '__main__':
	setup_software('config/config.cfg')