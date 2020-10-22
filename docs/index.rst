.. youtubetobibtex documentation master file, created by
   sphinx-quickstart on Thu Oct 22 14:19:47 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to youtubetobibtex's documentation!
===========================================

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

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   client
   cli