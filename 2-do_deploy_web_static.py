#!/usr/bin/python3

"""a Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy"""


import os.path
from fabric.api import *


env.hosts = ["54.164.162.231", "54.87.210.192"]


def do_deploy(archive_path):
    """deply archive"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')[-1]
        file_name_noext = file_name.split('.')[0]
        new_folder = '/data/web_static/releases/' + file_name_noext + '/'
        run('sudo mkdir -p {}'.format(new_folder))
        run('sudo tar -xzf /tmp/{} -C {}'.format(file_name, new_folder))
        run('sudo rm /tmp/{}'.format(file_name))
        #run('sudo mv {}web_static/* {}'.format(new_folder, new_folder))
        run('sudo rm -rf {}web_static'.format(new_folder))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(new_folder))
        print("New version deployed!")
        return True
    except:
        return False
