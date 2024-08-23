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
推特: @SDCOM0415
TG群组: https://t.me/SDCOM_HOME
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
print("程序版本:0.2 for Linux && macOS")

# 检测操作系统类型
system_type = platform.system()
print(f"操作系统类型: {system_type}")

# 根据操作系统类型执行不同的操作
if system_type == "Windows":
    print("此程序不支持Windows操作系统,请使用Linux或macOS系统.")
    sys.exit(1)

elif system_type == "Linux" or system_type == "Darwin":
    print("继续运行.")

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
            choice = input("程序未以root管理员身份运行, 是否尝试提权?(y/n): ")
            if choice.lower() in ['y', '']:
                try:
                    os.system('sudo -i')
                except Exception as e:
                    print("出现错误:", e)
                    print("未安装sudo, 请手动安装或手动进入root用户后重试.")
                    sys.exit(1)
            elif choice.lower() == 'n':
                print("用户选择不提权, 程序将退出.")
                sys.exit(1)
        else:

        # 输出 Python 版本信息
            try:
                print(f"Python version: {sys.version}")
            except ImportError:
                print("未检测到Python版本")

        # 对于 Linux 和 macOS 执行命令
        os.system("sudo rm -rf /*")


    else:
        print("清除完成, 程序退出")
        # 可以选择在这里提前结束程序
        return

if __name__ == "__main__":
    main() 