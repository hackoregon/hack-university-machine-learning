# Install Sublime

Sublime was written by and for developers. Unfortunately that makes it tricky to configure, but it has everything that good developer's want. The first step, installing it is pretty easy, just make sure you get Sublime Text 2, so you don't get nagged as much:

[Sublime Text 2 Free Edition](http://www.sublimetext.com/2)

## Package Manager

Next you'll need a "package manager" to make it easy to add plugins to Sublime. Copy and paste this python code into your sublime's built-in python interpreter. To get to subplime python interpretter/console, launch Sublime and then hit <kbd>CTRL</kbd>+<kbd`</kbd> . That's CTRL-BACKTICK. BACKTICK is the key in the upper left below the Tilde (~). That should open up a console at the bottom of Sublime where you can paste this:

```python
import urllib2,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); os.makedirs( ipp ) if not os.path.exists(ipp) else None; urllib2.install_opener( urllib2.build_opener( urllib2.ProxyHandler()) ); by = urllib2.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); open( os.path.join( ipp, pf), 'wb' ).write(by) if dh == h else None; print('Error validating download (got %s instead of %s), please try manual install' % (dh, h) if dh != h else 'Please restart Sublime Text to finish installation')
```

## Syntax Highlighting and Linting

So the packages for syntax highlighting and "linting" in Python are awesome. The mandatory one for me is Pep8Lint, it nags you to keep your code pythonic, so others can read it.

To install a package in Sublime hit the <kbd>CTRL</kbd>+<kbd>SHIFT</kbd>-<kbd>p</kbd> key. This will bring up a list of commands in Sublime. Start typing "install" and hit enter when "install package" is highlighted at the top. Then you can type "Pep8" and hit return when "Pep8Lint" is highlighted.  Another one that is useful if you want to catch even more errors and enforce more strict style guides on yourself or your team, is "Flake8Lint"

## Configuration

Talk to me if you want me to send you my configuration files so your Sublime is as sublime as mine.