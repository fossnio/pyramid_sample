pyramid-sample
==============

Getting Started
---------------

- Install required system packages first.

    sudo apt install python3-venv -y

- Create a Python virtual environment.

    mkdir ~/venv
    python3 -m venv ~/venv/pyramid_sample 

- Upgrade packaging tools in your virtual environment.

    cd ~/venv/pyramid_sample
    ./bin/pip install --upgrade pip setuptools

- Clone the project and install it in editable mode in your virtual environment.

    mkdir ~/git && cd ~/git
    git clone https://github.com/fossnio/pyramid_sample && cd pyramid_sample
    ./bin/pip install -e .

- Run your project in your virtual environment.

    ~/venv/pyramid_sample/bin/pserve development.ini

- Open your browser to visit http://localhost:6543.
