#!/usr/bin/python3
"""script that generates a .tgz archive from the contents
of the web_static folder"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """generates a .tgz archive"""
    try:
        local('mkdir -p versions')
        date_format = '%Y%m%d%H%M%S'
        arch_path = 'versions/web_static_{}.tgz'.format(
            datetime.now().strftime(date_format))
        local('tar -cvzf {} web_static'.format(arch_path))
        print('web_static packed:{} -> {}'.format(arch_path,
              os.path.getsize(arch_path)))
    except TypeError:
        None
