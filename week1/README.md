# week1

#### 今週は、環境構築を行います。

#### インストールしてもらうのは ROS と VS Code です。

#### 以下の手順でインストールをしてください。

<br>

##### 1. ROS のインストール
##### terminal(端末)で以下のコマンドを入力し、必要なライブラリをインストールしてください

<br>

```

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt install curl

curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

sudo apt update

sudo apt install ros-noetic-desktop-full

echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

source ~/.bashrc

sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

sudo rosdep init

rosdep update

```

<br>

##### 2. VS Code のインストール
##### [参考サイト](https://mebee.info/2020/03/18/post-7546/?msclkid=63cbc7f7b6aa11ec8066633e25ee0314)通りにインストールしてください
