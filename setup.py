import distutils.core
import sys

version = '3.0.0'

distutils.core.setup(name='slurpy',
    version=version,
    description="An Arch User Repository (AUR) search/download/update helper",
    author='Randy Morris',
    author_email='randy.morris@rsontech.net',
    url='http://rsontech.net/projects/slurpy',
    packages=['slurpy', 'slurpy.aur'],
    scripts=['scripts/slurpy']
)
