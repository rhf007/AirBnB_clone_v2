#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack"""


from datetime import datetime
from fabric.api import local


def do_pack():
    """create an archive and store it somewhere"""
    command1 = "sudo mkdir -p versions"
    local(command1)
    timeofname = datetime.utcnow()
    command2 = (
                f"tar -cvzf versions/web_static_{timeofname.year}"
                f"{timeofname.month}{timeofname.day}{timeofname.hour}"
                f"{timeofname.minute}{timeofname.second}.tgz web_static"
    )
    archv = local(command2)
    if archv.succeeded:
        return archv
    else:
        return None
