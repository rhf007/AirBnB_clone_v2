#!/usr/bin/python3

"""Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy"""


import os.path
from fabric.api import *


env.hosts = ["54.164.162.231", "54.87.210.192"]


def do_deploy(archive_path):
    """deply archive"""
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        archive_no_ext = archive_name.split(".")[0]

        put(archive_path, '/tmp/')

        run('sudo mkdir -p /data/web_static/releases/{}'.format(archive_no_ext))

        run('sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
            archive_name, archive_no_ext))

        run('sudo rm /tmp/{}'.format(archive_name))

        run('sudo mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}'.format(
            archive_no_ext, archive_no_ext))

        run('sudo rm -rf /data/web_static/current')

        run('sudo ln -s /data/web_static/releases/{} /data/web_static/current'.format(
            archive_no_ext))

        print('New version deployed!')
        return True

    except Exception as e:
        return False
