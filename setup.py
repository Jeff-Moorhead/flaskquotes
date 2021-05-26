import os
import shutil

from setuptools import setup, find_packages

version = {}

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("./flaskquotes/version.py", "r") as vh:
    exec(vh.read(), version)

if not os.path.exists(os.path.expandvars("$HOME/data"):
    os.mkdir(os.path.expandvars("$HOME/app/data")

shutil.copy("data/quotes.json", os.path.expandvars("$HOME/app/data/"))

setup(name="flaskquotes",
      description="Get AFI top 100 quotes",
      author="Jeff Moorhead",
      author_email="jeff.moorhead1@gmail.com",
      long_description=long_description,
      long_description_content_type="text/markdown",
      version = version.get("__version__", "0.0.0"),
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'quotes=flaskquotes.console:main'
          ]
      }, 
      install_requires=['BeautifulSoup4', 'Flask', 'gunicorn'],
      data_files=[(os.path.expandvars("$HOME/app/data"), "data/quotes.json")]
      )
