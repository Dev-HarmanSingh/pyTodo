# PyTodo

This is a little todolist utility i made in python. This was a hobby project that i started to get comfortable with working in git and using uv. If you want you can totally download this and you can submit PRs. Just remember the chances of me even seeing you PR let alone addressing it are very low. 



  **note**: I will try to give some download instruction shortly. For now if you want to try and download it from source code good luck.

# Installation

Currently, due to limitations of python, you will need pip to install this on your system.
also, this only works for linux(As far as i know). I don't know anything about .whl so if you do just know it was made using uv build.

It also seems it does not let me download it without a virtual environment. You know what just ignore this you dont have to use it there are so many much better options.

## Method 1 (Using pip)

clone this repo on to your computer

`git clone https://github.com/Dev-HarmanSingh/pyTodo.git`

Then, navigate to dist/ directory and run

`pip install pytodo-0.1.0.tar.gz`

This will install the todo package. If you download this using a venv then package will only work when venv is active.

## Method 2 (Using UV)

You may also clone the repo using step one above. then, you can download uv

`sudo dnf/brew/apt install uv`

Then, make a virtual environment

`uv venv`

activate it using this command

`source .venv/bin/activate(For linux/Mac)`

Then navigate to the dist/ directory and run

`uv pip install pytodo-0.1.0.tar.gz`

Now you can use this todo In the command line!
simply run the following command to see all commands.

`todo --help`

you can also run --help in any of the sub commands to check its options and parameters.
