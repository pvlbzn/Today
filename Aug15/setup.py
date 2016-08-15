import os

from setuptools import setup, Command

class Housemaid(Command):
    user_options = []
    def initialize_optios(self):
        self.cwd = None
    def finalize_options(self):
        self.cwd = os.getcwd()
    def run(self):
        os.system('rm -rf ./build ./*.pyc ./*.tgz ./*.egg-info')

setup(
    name='setuptools_test',
    version='0.1',
    install_requires=[
        'requests>=2.11.0'
    ],
    cmdclass={
        'clean': Housemaid,
    }
)
