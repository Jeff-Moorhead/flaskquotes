from setuptools import setup

setup(name="flaskquotes",
      description="Get AFI top 100 quotes",
      long_description=None,
      entry_points={
          'console_scripts': [
              'quotes=flaskquotes.console:main'
          ]
      }, install_requires=['beautifulsoup4']
      )
