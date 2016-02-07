## Install

### Preheat the Oven

#### [Download VirtualBox](https://www.virtualbox.org/wiki/Downloads) 

Find the right package for your OS:

- [Ubuntu 15.03](http://download.virtualbox.org/virtualbox/5.0.14/virtualbox-5.0_5.0.14-105127~Ubuntu~wily_amd64.deb)
- [any Linux](https://www.virtualbox.org/wiki/Linux_Downloads)
- [OSX](http://download.virtualbox.org/virtualbox/5.0.14/VirtualBox-5.0.14-105127-OSX.dmg)
- [Win64](http://download.virtualbox.org/virtualbox/5.0.14/VirtualBox-5.0.14-105127-Win.exe)

#### [Download Vagrant](https://www.vagrantup.com/downloads.html)

On the vagrant [Download page](https://www.vagrantup.com/downloads.html), find the package for your OS (Debian = Ubuntu). Open the package with your installer (double click on the package in your Downloads directory). On Ubuntu "Software Center" will launch and you click either the orange "Install" or "Upgrade" button.

### While you Wait

#### Web Accounts

- [GitHub](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiU15m349_KAhVLy2MKHVy7C3YQFggdMAA&url=https%3A%2F%2Fgithub.com%2Fjoin&usg=AFQjCNF6nezHQWX1hKwEFQVYRrUheS9_Ig)
  - Keep track of your projects
    - "Undo" when you make mistakes
    - `git checkout answer` when you have trouble with a project
  - Your forks of others' projects
  - Give back to the class by sharing your edits, material, links, code
  - Pull Requests to the Hack University projects
- [the PDXData Slack org](https://pdxdata.slack.com/)
  - Head to the #hacku Channel once you have an account and are signed in to pdxdata.slack.com
- [SignUp for a Twitter account](https://twitter.com/signup)
  - You'll need it for the twip project
  - [Tweet @hobsonlane](http://bit.ly/huml-help) so I can follow you
  - [Follow @hackoregon](https://twitter.com/hackoregon)
  - Include #huml in your tweets with questions or comments (**H**ack **U**niversity **M**machine **L**earning)
    - bit.ly shortcut: [http://bit.ly/huml-help](http://bit.ly/huml-help)
  - Follow your classmates tweets and the #huml hashtag 
- Google Drive or Gmail account (optional)

#### Text Editor

You can survive with an ssh and XWin connection to an editor on the Vagrant Box (virtual machine). But if you'd like a bit higher bandwidth and the "native" feel of your OS, install your favorite text editor on IDE on your laptop. Here are some of the features of the most popular python editors: 

- [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux&code=PCC)
  - integrated git
  - integrated execution of python scripts
  - not as useful for editing other languages
- [Sublime Text 2 Free Edition](http://www.sublimetext.com/2)
  - some basic execution of python scripts
  - powerful regular expressions
  - fast, clean
  - useful plugins like linters for almost all languages
  - easily customizable
  - difficult to install and maintain plugins
- [Atom](https://atom.io/)
  - fast
  - open source
  - backed by GitHub and a favorite of Google developers
  - customizable
  - new, bleeding edge

#### Version Control

And you probably want a decent "diff" tool to compare text files. I like [Meld](http://meldmerge.org/).

You probably also want `git` installed locally and have a way of running it from a shell with "readline" (remembers your commands so you don't have to retype them). [Git-Bash](http://www.git-scm.com/downloads) from GitHub does all this for you. On Linux, you probably already have git installed and you definitely have a decent shell ;)

#### Windows

If I have to work on Windows, I always install

- [Sublime Text 2 Free Edition](install-sublime.md)
- [CygWin](http://cygwin.com/install.html)
- [Anaconda](https://www.continuum.io/downloads)
- [Git-Bash](http://www.git-scm.com/downloads)

#### OSX

- [Sublime Text 2 Free Edition](install-sublime.md)
- [Anaconda](https://www.continuum.io/downloads)
- [Git-Bash](http://www.git-scm.com/downloads)

#### Linux

On Linux I can usually get away with using the standard package manager (apt-get on Ubuntu) and [`pip`](https://pip.pypa.io/en/stable/installing/)

`sudo -H pip install -r requirements.txt`?

### Get Going

Once VirtualBox and vagrant are downloaded and installed [Get Started](https://www.vagrantup.com/docs/getting-started/) crank up your first VirtualBox.

```bash
$ mkdir dst
$ cd dst
$ vagrant init data-science-toolbox/dst
$ vagrant up
```

Follow the rest of the instructions for the [Data Science Toolbox](http://datasciencetoolbox.org/) to set up ipython notebook to run on the virtualbox you just built. You might also like having the dsftcl bundle installed on your box, if you like using Linux shell to process lots of data quickly.

### Pro Tip (optional)

If you'd like others to be able to query your database or run and edit your ipython notebooks on your server running on your laptop, you just need to share the IP address of your Vagrant box with them. And you'll need to ensure that your Vagrant box is configured to use NAT and set up the host machine (your laptop) forward port 8888, 80, and 8000 (or whatever ports you need) through Vagrant (VirtualBox).

## Finally

Now you can review the [syllabus](docs/syllabus.md) and start working on some problems.