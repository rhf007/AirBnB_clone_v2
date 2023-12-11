#!/usr/bin/python3
"""a Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy"""


import os.path
from fabric.api import *


env.hosts = ["54.164.162.231", "54.87.210.192"]


def do_deploy(archive_path):
    """deply archive"""
    if os.path.exists(archive_path) is True:
        filename = archive_path.split("/")[-1]

        try:
            put(filename, "/tmp/")

            filenoext = filename.split(".")[0]

            mkdircmd = "mkdir -p /data/web_static/releases/{}".format(filenoext)

            uncompresscmd = (
                             f"tar -xzf /tmp/{filename} -C "
                             f"/data/web_static/releases/{filenoext}/"
            )

            deletecmd = "rm {}".format(filename)

            mvcmd = (
                     f"mv /data/web_static/releases/{filenoext}/web_static/* "
                    f"/data/web_static/releases/{filenoext}/"
            )

            deletecpcmd = (
                           f"rm -rf /data/web_static/releases/"
                           f"{filenoext}/web_static"
            )

            deleteslcmd = "rm -rf /data/web_static/current"

            createnewslcmd = (
                              f"ln -sf /data/web_static/releases/{filenoext} "
                              f"/data/web_static/current"
            )

            run(mkdircmd)
            run(uncompresscmd)
            run(deletecmd)
            run(mvcmd)
            run(deletecpcmd)
            run(deleteslcmd)
            run(createnewslcmd)
            return True
        except:
            return False
    else:
        return False
