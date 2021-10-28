# Ubuntu 20.10 setup from the beginning

## commands

   6  sudo apt update
    7  sudo apt upgrade
    8  snap refresh
    9  snap install hello-world
   10  sudo snap install hello-world
   11  hello-world
      21  ssh-keygen
   22  cat /home/justinaawd/.ssh/id_rsa.pub
  35  sudo snap install nvim --classic
   37  sudo snap install curl
sudo apt install git
   36  curl -sLf https://spacevim.org/install.sh | bash
nvim
alias vim="nvim"
   54  export EDITOR="nvim"

nvim .SpaceVim.d/init.toml 
/usr/bin/python3
python3 -V
sudo snap install python3-pip
pip -V
echo 'export PATH="$PATH:/home/MYUSERNAME/.local/bin"' >> ~/.bashrc
 73  pip install --user pylint
   74  pip install --user yapf

    sudo apt install gnome-tweaks
    sudo apt install terminator:wq
    sudo apt update
sudo apt install unit
sudo apt install unit-dev unit-go unit-jsc11 unit-jsc15 unit-jsc16 unit-jsc17  \
              unit-perl unit-php unit-python2.7 unit-python3.9 unit-ruby
sudo systemctl restart unit





### NGINX Unit setup
sudo curl -sL https://nginx.org/keys/nginx_signing.key | sudo apt-key add -

sudo touch /etc/apt/sources.list.d/unit.list

sudo echo 'deb https://packages.nginx.org/unit/ubuntu/ hirsute unit' >> /etc/apt/sources.list.d/unit.list
deb-src https://packages.nginx.org/unit/ubuntu/ hirsute unit

sudo apt update
sudo apt install unit
sudo apt install unit-dev unit-go unit-jsc11 unit-jsc15 unit-jsc16 unit-jsc17  \
              unit-perl unit-php unit-python2.7 unit-python3.9 unit-ruby
sudo systemctl restart unit
sudo npm install -g --unsafe-perm unit-http
sudo npm update -g --unsafe-perm unit-http
sudo systemctl enable unit
sudo systemctl restart unit
sudo systemctl stop unit
sudo systemctl disable unit
sudo apt install php

cat << EOF > config.json

    {
        "type": "php",
        "root": "/www/blogs/scripts"
    }
EOF
sudo curl -X PUT --data-binary @config.json --unix-socket \
       /path/to/control.unit.sock http://localhost/config/applications/blogs


   {
        "success": "Reconfiguration done."
    }

sudo curl --unix-socket /path/to/control.unit.sock http://localhost/config/
'
    {
        "listeners": {
            "127.0.0.1:8300": {
                "pass": "applications/blogs"
            }
        },

        "applications": {
            "blogs": {
                "type": "php",
                "root": "/www/blogs/scripts/"
            }
        }
    }'
touch /etc/apt/sources.list.d/mongodb-org-5.0.list
sudo apt-get install gnupg  
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl start mongod
sudo systemctl daemon-reload
sudo systemctl status mongod
sudo systemctl enable mongod

mongosh
disableTelemetry()
reboot
