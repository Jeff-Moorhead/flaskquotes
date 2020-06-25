from setuptools import setup

version = {}

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("./version.py", "r") as vh:
    exec(vh.read(), version)

setup(name="flaskquotes",
      description="Get AFI top 100 quotes",
      author="Jeff Moorhead",
      author_email="jeff.moorhead1@gmail.com",
      long_description=long_description,
      long_description_content_type="text/markdown",
      version = version.get("__version__", "0.0.0"),
      entry_points={
          'console_scripts': [
              'quotes=flaskquotes.console:main'
          ]
      }, install_requires=['BeautifulSoup4', 'Flask']
      )
