from setuptools import setup
import re

version = ''
with open('utcardmakr/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = ''
with open('README.md') as f:
    readme = f.read()

packages = [
    'utcardmakr',
    'utcardmakr.types'
]

setup(
    name='utcardmakr',
    author='anasouh',
    url='https://github.com/anasouh/utcardmakr',
    version="0.1.0",
    packages=packages,
    license='MIT',
    description='Create your custom EA FC Ultimate Team card !',
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    python_requires='>=3.9.0',
)