http://twitter.com/home?status=Question%20about%20#huml%20@hobsonlane

## Install

### Preheat the Oven

#### [Download VirtualBox](https://www.virtualbox.org/wiki/Downloads) the package for your OS:

- [Ubuntu 15.03](http://download.virtualbox.org/virtualbox/5.0.14/virtualbox-5.0_5.0.14-105127~Ubuntu~wily_amd64.deb)
- [any Linux](https://www.virtualbox.org/wiki/Linux_Downloads)
- [OSX](http://download.virtualbox.org/virtualbox/5.0.14/VirtualBox-5.0.14-105127-OSX.dmg)
- [Win64](http://download.virtualbox.org/virtualbox/5.0.14/VirtualBox-5.0.14-105127-Win.exe)

#### [Download Vagrant](https://www.vagrantup.com/downloads.html)

[Download](https://www.vagrantup.com/downloads.html) the package for your OS (choose Debian for Ubuntu). Open the package with your installer (double click on the package in your Downloads directory). On Ubuntu "Software Center" will launch and you click either the orange "Install" or "Upgrade" button.

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

#### You probably Want a Local IDE

You can survive with an ssh and XWin connection to an editor on the Vagrant Box (virtual machine). But if you'd like a bit higher bandwidth and the "native" feel of your OS, install your favorite text editor on IDE on your laptop. Some of my favorites are: 

- PyCharm
  - integrated git
  - integrated execution of python scripts
  - not as useful for editing other languages
- Sublime
  - some basic execution of python scripts
  - powerful regular expressions
  - fast, clean
  - useful plugins like linters for almost all languages
  - easily customizable
  - difficult to install and maintain plugins
- Atom
  - fast
  - open source
  - backed by GitHub and a favorite of Google developers
  - customizable
  - new, bleeding edge

You probably also want `git` installed locally and have a decent shell with "readline" (remembers your commands so you don't have to retype them).

If I have to work on Windows, I always install

- cygwin
- Anaconda
- Git-bash
- Sublime

On OSX

- Brew
- Sublime
- git
- Upgrade XCode

On Linux I can usually get away with using the standard package manager (apt-get on Ubuntu) and `pip`

`sudo -H pip install -r requirements.txt`?

### Get Going

Once VirtualBox and vagrant are downloaded and installed [Get Started](https://www.vagrantup.com/docs/getting-started/) crank up your first VirtualBox.

```bash
$ mkdir dst
$ cd dst
$ vagrant init data-science-toolbox/dst
$ vagrant up
```

