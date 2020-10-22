from setuptools import find_packages, setup

from youtubetobibtex import __author__, __title__, __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=__title__,
    version=__version__,
    author=__author__,
    auhtor_email="me@nanoy.fr",
    description="Get bibtex entry for a video from its url",
    long_description=long_description,
    url="https://github.com/nanoy42/youtubetobibtex",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Multimedia :: Video",
    ],
    packages=["youtubetobibtex"],
    test_suite="tests",
    entry_points={"console_scripts": ["youtubetobibtex=youtubetobibtex.cli:main"]},
    install_requires=["google-api-python-client"],
)
