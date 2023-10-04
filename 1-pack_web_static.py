#!/usr/bin/python3
"""
Fabric script that generates a tgz archive
"""


from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Compresses the web_static folder into a .tgz archive.

    Returns:
        Archive path on success, None on failure.
    """
    try:
        local("mkdir -p versions")

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        archive_name = "web_static_{}.tgz".format(timestamp)

        local("tar -cvzf versions/{} web_static".format(archive_name))

        return "versions/{}".format(archive_name)

    except Exception as e:
        return None
