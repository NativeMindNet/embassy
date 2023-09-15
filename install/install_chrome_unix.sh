apt-get install curl
curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
bash -c "echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google-chrome.list"
apt -y update
apt -y install google-chrome-stable