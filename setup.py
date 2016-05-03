import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name="poetri",
      version="0.0.1",
      description="Pre-OAuth Entity Trust Reference Implementation",
      long_description="""Command line tools and libraries for signing and verifying JWTs according to https://github.com/hhsidealab/poet.""",
      author="Alan Viars",
      author_email="sales@videntity.com",
      url="https://github.com/transparenthealth/poetri",
      download_url="https://github.com/transparenthealth/poetri/tarball/master",
      install_requires=['PyJWT', 'cryptography', ],
      packages= ['poetri', 'tests'],
      package_data={'':['taxonomy-license-crosswalk.csv','fiftythousand.csv']},
      scripts=['poetri/verify_poet.py',
               'poetri/sign_poet.py',
               ]
      )

