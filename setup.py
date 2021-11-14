import sys
from distutils.core import setup

REQUIRED_PACKAGES = []
if sys.version_info < (3, 4):
    REQUIRED_PACKAGES.append('enum34')

setup(
    name='anitopy',
    packages=['anitopy'],
    version='2.0.2',
    description='An anime video filename parser',
    author='Igor Cescon de Moura',
    author_email='igorcesconm@gmail.com',
    url='https://github.com/igorcmoura/anitopy',
    python_requires='>=2.7',
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
