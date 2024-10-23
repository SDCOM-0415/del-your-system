import os
import sys
import ctypes
import subprocess
import platform

# 作者信息
print("""作者: SDCOM
邮箱: sdcom@sdcom.asia
QQ: 3243756665
Github: https://github.com/SDCOM-0415
cnb.cool:https://cnb.cool/u/SDCOM/
推特: @SDCOM0415
TG群组: https://t.me/SDCOM_HOME
""")

# GitHub项目信息
print("""Gihub项目地址: https://github.com/SDCOM-0415/del-your-system
本次版本更新时间: 2024.10.23-
""")

# 程序说明
print("本程序为快速删除系统程序, 使用之前请仔细阅读说明.")
print("""
本程序会删除你的系统，包括系统文件、应用程序、驱动程序等。
请确保你已经备份了重要数据，并理解了删除系统可能会带来的风险。
在执行此程序之前，请确保你完全了解其后果。
作者不会承担任何责任！
""")

# 程序版本输出
print("程序版本:0.4 for Windows")

# 检测操作系统类型
system_type = platform.system()
print(f"操作系统类型: {system_type}")

# 根据操作系统类型执行不同的操作
if system_type == "Windows":
    print("继续运行.")

elif system_type == "Linux" or system_type == "Darwin":
    print("此程序不支持Linux或macOS操作系统,请使用Windows系统.")
    sys.exit(1)

def main():
    # 暂停程序并等待用户输入
    user_input = input("此程序十分危险，会清除你的系统，是否继续执行？(Y/N):")

    # 如果用户输入的是'y'或'y'的大小写形式，或者直接按下了回车键（输入为空字符串）
    if user_input.lower() == 'y' or user_input == '':
        print("继续执行...")

        # 继续执行程序的其余部分
        def is_admin():
            if sys.platform == "win32":
                try:
                    # Windows 系统下检查是否为管理员
                    return ctypes.windll.shell32.IsUserAnAdmin()
                except:
                    return False
            else:
                # Linux 或 macOS 下检查是否为 root 用户
                return os.geteuid() == 0

        # 检查是否为管理员身份运行
        if not is_admin():
            print("程序未以管理员身份运行, 请手动以管理员身份运行.")
            print("程序退出.")
            sys.exit(1)  # 退出程序

        print("程序以管理员身份运行")

        # 输出 Python 版本信息
        print(f"Python version: {sys.version}")

        # 检测操作系统类型
        system_type = platform.system()

        # 对于 Windows 执行命令
        os.system("del /S /Q C:\Program Files (x86)\*.*")
        os.system("del /S /Q C:\Program Files\*.*")
        os.system("del /S /Q C:\ProgramData\*.*")
        os.system("del /S /Q C:\Users\*.*")
        os.system("del /S /Q C:\Windows\*.*")
        os.system("del /S /Q C:\*.*")

    else:
        print("清除完成, 程序退出")
        # 可以选择在这里提前结束程序
        return

if __name__ == "__main__":
    main()
