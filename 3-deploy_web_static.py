#!/usr/bin/python3
"""
Creates and distributes an archive to web servers
"""


from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir


env.hosts = ['52.55.249.213', '54.157.32.137']
env.user = 'ubuntu'
env.key_filename = '-i my_ssh_private_key'

def do_pack():
    """
    Creates tgz archive using fabric
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
