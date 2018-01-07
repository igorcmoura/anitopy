import sys
from distutils.core import setup

if sys.version_info < (2, 7):
    sys.exit('Python 2.7 or above is required.')

setup(
    name='anitopy',
    packages=['anitopy'],
    version='1.0.1',
    description='An anime video filename parser',
    author='Igor Cescon de Moura',
    author_email='igorcesconm@gmail.com',
    url='https://github.com/igorcmoura/anitopy',
    python_requires='>=2.7',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
