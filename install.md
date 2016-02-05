## Install

### Preheat the Oven

#### [Download VirtualBox](https://www.virtualbox.org/wiki/Downloads) the package for your OS:

- [Ubuntu 15.03](http://download.virtualbox.org/virtualbox/5.0.14/virtualbox-5.0_5.0.14-105127~Ubuntu~wily_amd64.deb)
- [any Linux](https://www.virtualbox.org/wiki/Linux_Downloads)
- [OSX](http://download.virtualbox.org/virtualbox/5.0.14/VirtualBox-5.0.14-105127-OSX.dmg)
- [Win64](http://download.virtualbox.org/virtualbox/5.0.14/VirtualBox-5.0.14-105127-Win.exe)

#### [Download Vagrant](https://www.vagrantup.com/downloads.html)

[Download](https://www.vagrantup.com/downloads.html) the package for your OS (choose Debian for Ubuntu). Open the package with your installer (double click on the package in your Downloads directory). On Ubuntu "Software Center" will launch and you click either the orange "Install" or "Upgrade" button.

### While you Wait for the Oven

#### Web Accounts

- [GitHub](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiU15m349_KAhVLy2MKHVy7C3YQFggdMAA&url=https%3A%2F%2Fgithub.com%2Fjoin&usg=AFQjCNF6nezHQWX1hKwEFQVYRrUheS9_Ig)
  - Keep track of your projects
    - Roll back to previous versions when things break   
  - Your forks of others' projects
  - Give back to the class by sharing your edits, material, links, code
  - Pull Requests to the Hack University projects
- [the PDXData Slack org](https://pdxdata.slack.com/)
  - Head to the #hacku Channel once you have an account and are signed in to pdxdata.slack.com

#### You probably Want a Local IDE

You can survive with an XWin connection to Sublime or PyCharm on the Vagrant Box ("guest" machine). But if you'd like a bit higher bandwidth and "native" feel, install them on your laptop (the Vagrant "host" machine)

- PyCharm
- Sublime
- Atom

- `git` (or git-bash)
  - Google Drive account
  - Vagrant + VirtualBox + Docker
      - [Mac Instructions](http://cjlarose.com/2014/03/08/run-docker-with-vagrant.html)
    - Windows alternative
        - Conda
        - Jupyter
        - Git-bash
        - cygwin
    - OSX alternative
        - Brew
        - Scikit-learn, etc
    - Ubuntu alternative
        - Ansible script to install everything?
        - `sudo -H pip install -r requirements.txt`?

### Install Docker

### Get Going

Once VirtualBox and vagrant are downloaded and installed [Get Started](https://www.vagrantup.com/docs/getting-started/) crank up your first VirtualBox.

```bash
$ mkdir huml
$ cd huml
$ vagrant init hashicorp/precise64
$ vagrant up
```

