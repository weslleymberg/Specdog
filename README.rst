Specdog
=======

An automatic spec runner.
Speddoc do not rely on test running tools. All you need to do is to say which command should be executed every time you make a change on your project.

Usage::

    specdog "<command-to-be-executed>"
    specdog --ext <file-extension> "<command-to-be-executed>"

Example::

    specdog "specloud whatever_spec.py"
    specdog --ext .rb "rspec whatever_spec.rb"

PS.: The default file extension is .py

Installing::
    
    pip install http://github.com/weslleymberg/Specdog/tarball/master
