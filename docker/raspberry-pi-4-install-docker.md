# Raspberry Pi 4 install docker

## Upgrade and Update
```bash
sudo apt-get update && sudo apt-get upgrade
```

## Install docker
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

## Append a non-root user on the Docker group
```bash
sudo usermod -aG docker [user_name]
```

## Check
```bash
docker version
```

## Run
```bash
docker run hello-world
```

## Install docker-compose
```bash
sudo apt-get install libffi-dev libssl-dev
sudo apt install python3-dev
sudo apt-get install -y python3 python3-pip
sudo pip3 install docker-compose
```

## Enable the Docker system service to start your containers on boot
```bash
sudo systemctl enable docker
```

# Reference
* https://www.simplilearn.com/tutorials/docker-tutorial/raspberry-pi-docker
* https://dev.to/elalemanyo/how-to-install-docker-and-docker-compose-on-raspberry-pi-1mo