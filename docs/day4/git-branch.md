# Git Branch

Get your own branch so you can work on your files in peace.

Zak and others have already done this.

```bash
# git clone # repository URL with https:// here, skip if you've already done this
git checkout master -b your_name
git push -u origin your_name
```

Open the files in sublime or PyCharm or iPython notebook to see what you've got.

Edit a file and save

```bash
# git clone # repository URL with https:// here, skip if you've already done this
git commit -am "my first commit to my own branch!"
git push
git pull origin master
```

If pulling the master into your branch causes "merge conflicts" or other headaches then

```bash
cp filename.py your_name_filename.py
git add your_name_*.py
git commit -am 'created my own version of filename.py'
git push
```
