Lessons for a scientific programmer
===================================

Author: Philip Elson (@pelson)

## Abstract

The gradual learning curve of Python along with the rich diversity of third-party scientific packages has
led to a continued increase in the number of self-taught scientific Python users. Whilst it is often the case that these users
can produce powerful and insightful visualisations, have mastered efficient numpy functionality, and can write scripts to address
almost any scientific need, anecdotally it appears that some of the fundamental skills of writing maintainable and verifiable scientific
Python are underdeveloped.

This tutorial will attempt to address some of the oft neglected "softer skills" useful for writing maintainable, readable and
reproducible (scientific) Python software. We will look at: using version control with Git (via Github); using YAML for configuration files;
writing readable, idiomatic Python; testing with Python's unittest; and finally the creation of documentation with Sphinx.

The topics touched upon in this tutorial will have been necessarily used by every regular contributor of open source Python software, so this
will be an excellent opportunity for you to understand how all of the major scientific Python packages are developed and
maintained. It is hoped that by the end of this tutorial, you will have the confidence and skills to contribute to any open
source Python package, perhaps go on to write the next big scientific tool, or simply be able to write better code in pursuit of your scientific goals.

## Requirements
The tutorial will be hands-on, you'll ideally have a modern Python 2.7 distribution available on your machine - Anaconda
is recommended for this purpose. Alternatively you will need at least git, python2.7, pyyaml, and Sphinx on your system. Everybody will
also need a github account (if you don't have one already and don't have an abstract username to hand, many
people just use "{initial}{surname}"). Please follow https://help.github.com/articles/set-up-git to have your git configured correctly.

## Notebooks
The notebooks in this tutorial can all be seen on nbviewer.ipython.org:
 * Euroscipy 2014: http://nbviewer.ipython.org/github/pelson/lessons_for_a_scientific_programmer/tree/master/2014-euroscipy/00_intro.ipynb

