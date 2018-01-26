pyramid-sample
==============

Getting Started
---------------

- Install required system packages first.

    sudo apt install python3-venv -y

- Create a Python virtual environment.

    mkdir ~/venv
    python3 -m venv ~/venv/pyramid_sample 

- Upgrade packaging tools.

    cd ~/venv/pyramid_sample
    ./bin/pip install --upgrade pip setuptools

- Install the project in editable mode

    ./bin/pip install -e .

- Run your project.

    ./bin/pserve development.ini

- Open your browser to visit http://localhost:6543.
