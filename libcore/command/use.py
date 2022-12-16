#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import ctypes
import os
import re
import winreg
from os.path import join

from libcore.config.config import Config
from libcore.utill.plms_rar import PlmsRAR
from libcore.utill.downloader import Download
from libcore.utill.system_information import SystemInformation


class USE:

    @staticmethod
    def use_java_for_windows(filename=str):
        """
        切换java版本
        """
        config = Config()
        DD = Download()

        config.init_path()
        app_install_path = config.get_app_install_path()
        print(app_install_path)
        if ctypes.windll.shell32.IsUserAnAdmin() == 1:  # 检查当前系统用户是否具备 Root 权限
            var = os.environ['PATH'].split(";")

            if var[-1] == filename:
                print("无需重复设置同版本的jdk!")  # 这里抛异常
            else:
                tmp = []
                for acc in var:
                    pattern_1 = r"jdk-"
                    pattern_2 = r"\\java\\"
                    if re.search(pattern_1, acc) or re.search(pattern_2, acc) is None:
                        tmp.append(acc)

                filepath = config.get_app_install_path()
                JAVA_HOME = filepath + "\\" + filename
                PATH = ";".join(tmp)
                aa = os.system("wmic ENVIRONMENT where \"name='JAVA_HOME'\" delete")

                bb = os.system(
                    f"wmic ENVIRONMENT create name=\"JAVA_HOME\","
                    f"username=\"<system>\", VariableValue= \"{JAVA_HOME}\""
                )

                cc = os.system(
                    f"wmic ENVIRONMENT where \"name='Path' and username='<system>'\" "
                    f"set VariableValue= \"{PATH};{JAVA_HOME}\\bin\""
                )

        else:
            pass


if __name__ == "__main__":
    pass
