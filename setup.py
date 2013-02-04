from distutils.core import setup
from distutils.sysconfig import get_python_lib
from os.path import join
import glob, os

setup(
    name='YATES Monitor',
    version='0.1.0',
    author='Mark Wallsgrove',
    author_email='mark.wallsgrove@gmail.com',
    scripts=['yates_monitor'],
    url='http://github.com/smokedice/YATESMonitor',
    license='',
    description='YATES client monitor',
    install_requires=[ 
        'Twisted==12.3.0',
        'argparse==1.2.1',
        'autobahn==0.5.9',
        'distribute==0.6.24',
        'wsgiref==0.1.2',
        'zope.interface==4.0.3',
    ],
)
