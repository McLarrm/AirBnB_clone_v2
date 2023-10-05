#!/usr/bin/python3
"""
Distributes an archive to web servers
"""

from fabric.api import env, put, run
from os.path import exists
from datetime import datetime

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'
env.key_filename = ['my_ssh_private_key']

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers and deploys it
    """
    try:
                if not (path.exists(archive_path)):
                        return False
