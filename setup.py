#!/usr/bin/python
import setuptools
setuptools.setup(
    name = 'docker-get-run',
    version = '0.1',
    packages = setuptools.find_packages(),
    scripts = ['docker-get-run'],
    install_requires = ['docker'],
    package_data = {
        '': ['LICENSE', 'README.md']
    },
    author = 'Pavel Odvody',
    author_email = 'podvody@redhat.com',
    description = 'Get a suitable `docker run` command from a running container',
    license = 'MIT',
    keywords = 'docker cli run inspect',
    url = 'https://github.com/shaded-enmity/docker-get-run'
)
