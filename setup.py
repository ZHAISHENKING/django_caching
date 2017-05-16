# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django_caching',
    version='0.5.0',
    keywords=('django', 'cache', 'caching'),
    description='A easy using django cache manager.',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: MacOS X',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Environment :: Win32 (MS Windows)',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    license='Apache License',
    install_requires=['django>=1.8'],

    author='NineChapter',
    author_email='daniel48@126.com',
    maintainer='NineChapter',
    maintainer_email='daniel48@126.com',
    download_url='https://github.com/ninechapter/django_caching',
    url='https://github.com/ninechapter/django_caching',

    packages=find_packages(),
    platforms='any',
)
