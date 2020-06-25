from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="flaskquotes",
      description="Get AFI top 100 quotes",
      long_description=long_description,
      long_description_content_type="text/markdown",
      entry_points={
          'console_scripts': [
              'quotes=flaskquotes.console:main'
          ]
      }, install_requires=['BeautifulSoup4', 'Flask']
      )
