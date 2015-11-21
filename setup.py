import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mara",
    version = "1.0.0",
    author = "Richard Terry",
    author_email = "python@richardterry.co.uk",
    description = ("A framework for network services, talkers and MUDs"),
    license = "BSD",
    keywords = "socket telnet",
    url = "http://richardterry.co.uk/projects/mara/",
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: BSD License",
        'Operating System :: OS Independent',
        "Topic :: Communications :: Chat",
        "Topic :: Internet",
        "Topic :: Games/Entertainment :: Multi-User Dungeons (MUD)",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    extras_require = {
        'dev':  ['nose'],
        'full': ['bcrypt', 'dateutil'],
    },
    test_suite = 'nose.collector',
    zip_safe=True,
    packages=['mara'],
    scripts=['bin/mara']
)
