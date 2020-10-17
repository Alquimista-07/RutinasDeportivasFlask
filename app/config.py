""" Configuration file for development"""
import os
ENVIRONMENT = os.getenv('ENVIRONMENT', 'develop')
SERVER_DATABASE = os.getenv('SERVER_DATABASE', 'localhost')
USER_DATABASE = os.getenv('USER_DATABASE', 'root')
PASSWORD_DATABASE = os.getenv('PASSWORD_DATABASE', 'root')
PORT_DATABASE = os.getenv('PORT_DATABASE', '3306')
NAME_DATABASE = os.getenv('NAME_DATABASE', 'rutinas')
