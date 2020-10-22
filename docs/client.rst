Client class
============

YoutubeToBibtexClient
#####################
.. module:: youtubetobibtex.client
.. autoclass:: YoutubetobibtexClient
    :members:
    :private-members:

Exceptions
##########


.. module:: youtubetobibtex.errors
.. autoexception:: VideoNotFound
.. autoexception:: ChannelNotFound
.. autoexception:: UrlNotSupported

Usage example
#############

.. code-block:: python

    In [1]: from youtubetobibtex import YoutubetobibtexClient
    In [2]: client = YoutubetobibtexClient("secret")
    In [3]: client.check() # check if the client is correctly connected to google api
    Out[3]: True
    In [4]: video_id = client.get_video_id("https://www.youtube.com/watch\?v=v=LkH2r-sNjQs") # get id from url. several schemes of url are supported
    In [5]: video_id                                     
    Out[5]: 'LkH2r-sNjQs'
    In [6]: client.get_bibtex(video_id) # get bibtex
    Out[6]: '\n@online{video:tomscott2019,\n    title = {Why Electronic Voting Is Still A Bad Idea},\n    date = {2019},\n    organization = {YouTube},\n    author = {Tom Scott},\n    url = {https://youtube.com/watch?v=LkH2r-sNjQs},\n}\n  