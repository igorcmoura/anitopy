import sys
from distutils.core import setup

if sys.version_info < (3, 5):
    sys.exit('Python 3.5 or above is required.')

setup(
    name='anitopy',
    packages=['anitopy'],
    version='1.0.1',
    description='An anime video filename parser',
    author='Igor Cescon de Moura',
    author_email='igorcesconm@gmail.com',
    url='https://github.com/igorcmoura/anitopy',
    python_requires='>=3.5',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only'
    ]
)
