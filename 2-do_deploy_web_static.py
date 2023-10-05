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
    if not exists(archive_path):
        return False

    try:
        archive_filename = archive_path.split("/")[-1]
        archive_name = archive_filename[:-4]

        put(archive_path, "/tmp/")

        release_path = "/data/web_static/releases/{}".format(archive_name)
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_path))

        run("rm /tmp/{}".format(archive_filename))

        run("mv {}/web_static/* {}".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))

        print("New version deployed!")
        return True

    except Exception as e:
        return False
