from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in slnee_app/__init__.py
from slnee_app import __version__ as version

setup(
	name="slnee_app",
	version=version,
	description="mobile application",
	author="Mohamed",
	author_email="qwertyrioup@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
