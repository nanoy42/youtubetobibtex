# Youtubetobibtex

[![Documentation Status](https://readthedocs.org/projects/youtubetobibtex/badge/?version=latest)](https://youtubetobibtex.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/nanoy42/youtubetobibtex/badge.svg?branch=main)](https://coveralls.io/github/nanoy42/youtubetobibtex?branch=main)
[![github-actions](https://github.com/nanoy42/youtubetobibtex/workflows/tests/badge.svg)](https://github.com/nanoy42/youtubetobibtex/workflows/tests)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Code style black](https://img.shields.io/badge/code%20style-black-000000.svg)]("https://github.com/psf/black)
[![GitHub release](https://img.shields.io/github/release/nanoy42/youtubetobibtex.svg)](https://github.com/nanoy42/youtubetobibtex/releases/)
[![PyPI - Status](https://img.shields.io/pypi/status/youtubetobibtex)](https://pypi.org/project/youtubetobibtex/)

Youtubetobibtex is a small library to export information from a YouTube video in a bibtex format.

The bibtex looks like :

```
@online{video:tomscott2019,
    title = {Why Electronic Voting Is Still A Bad Idea},
    date = {2019},
    organization = {YouTube},
    author = {Tom Scott},
    url = {https://youtube.com/watch?v=LkH2r-sNjQs},
}
```

(example with the video https://www.youtube.com/watch\?v=v=LkH2r-sNjQs).


Youtubetobibtex is available online at : https://pypi.org/project/youtubetobibtex/

## Usage

The documentation can be found at : https://youtubetobibtex.readthedocs.io/en/latest/

### Class usage

The main part of the code is the `YoutubetobibtexClient` class. It implements methods to easily retrieve the bibtex

```
In [1]: from youtubetobibtex import YoutubetobibtexClient
In [2]: client = YoutubetobibtexClient("secret")
In [3]: client.check() # check if the client is correctly connected to google api
Out[3]: True
In [4]: video_id = client.get_video_id("https://www.youtube.com/watch\?v=v=LkH2r-sNjQs") # get id from url. several schemes of url are supported
In [5]: video_id                                     
Out[5]: 'LkH2r-sNjQs'
In [6]: client.get_bibtex(video_id) # get bibtex
Out[6]: '\n@online{video:tomscott2019,\n    title = {Why Electronic Voting Is Still A Bad Idea},\n    date = {2019},\n    organization = {YouTube},\n    author = {Tom Scott},\n    url = {https://youtube.com/watch?v=LkH2r-sNjQs},\n}\n  
```

The secret refers at the API key.

### Cli usage

There is a command line interface shipped with youtubetobibtex. It can be used as follows :

```
youtubetobibtex https://youtube.com/watch?v=LkH2r-sNjQs secret
```

You can also use the python script :

```
python3 youtubetobibtex/cli.py https://youtube.com/watch?v=LkH2r-sNjQs secret
```

## TODO

* Allow to enable more information in the bibtex, using options in the class
* Allow the command line interface to get the api key form file
* Properly close the socket if the api key is wrong

## Run the tests

Command to run the tests : 

```
python3 setup.py
```

or with coverage

```
coverage run --source=youtubetobibtex/ setup.py test
```