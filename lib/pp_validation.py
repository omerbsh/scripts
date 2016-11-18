#!/usr/bin/env python
"""
Created by Omer ben shushan
App name: pyPanel Cli
Description: validation useful functions
"""
import re

def domain_validation(domain_name):
    rule = "^(?:[a-zA-Z0-9]+(?:\-*[a-zA-Z0-9])*\.)+[a-zA-Z]{2,6}$"
    return re.match(rule , domain_name)
