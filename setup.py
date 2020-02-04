#!/usr/bin/env python

from distutils.core import setup

setup(name='websocket_console',
      version='0.1',
      description='',
      keywords='websocket console',
      author='Victor Yarmola',
      author_email='std.feanor@gmail.com',
      url='https://github.com/stdk/websocket_console',
      install_requires=['websockets>=3.0'],
      packages=[],
      scripts=['websocket-console'],
      classifiers=[
        'Environment :: Console',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: BSD License',
        'Topic :: Utilities',
      ],
     )