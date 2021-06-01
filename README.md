Flaskquotes
===========

A quote generator built with Flask and BeautifulSoup. Quotes are scraped from the American
Film Institute's top 100 movie quotes list.

Installation
------------

To install, simply run `pip install flaskquotes`.

Usage
-----

NOTE: Flaskquotes is down. I am working on resolving an issue with pulling quotes from the AFI's website.
It seems in the time since my last build, they restricted access to their site by automated web scraping
tools. Since this project uses the requests module, I am no longer able to pull the quotes from the AFI
website itself. Once I have implemented a solution, the application will be back online!

This project is a web application. You can view the project on [Heroku](https://flaskquotes.herokuapp.com).
The package also includes a command line entrypoint called `quotes`.
After installation, run `quotes` for a random quote, or include the `--random` option for a
random quote.

Bugs and Modifications
----------------------

Please feel free to email jeff.moorhead1@gmail.com with ideas for modifications or to
report a bug.
