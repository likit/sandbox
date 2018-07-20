# Install home brew

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

# Install Python
```
brew install python
```

# Install virtualenv
```
pip3 install virtualenv
```

# Install virtualenvwrapper
```
pip3 install virtualenvwrapper
```

# Install virtualenvwrapper scripts
# Add the following to .bash_profile
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

# Make sure the python path is correct
# export VIRTUALENVWRAPPER_PYTHON=/usr/local/Cellar/python/3.7.0/bin/python3

# Git command
```
git status
git add <file>
git commit -m "<message>"
git push

git fetch upstream
git diff master upstream/master
git merge upstream/master
```