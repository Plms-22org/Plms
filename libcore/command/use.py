#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import ctypes
import os
import re
import winreg
from os.path import join

from libcore.config.config import Config
from libcore.utill.system_information import SystemInformation


class USE:

    def __str__(self):
        pass

    def java_use(self):
        """

        """

        if ctypes.windll.shell32.IsUserAnAdmin() == 1:  # 检查当前系统用户是否具备 Root 权限
            var = os.environ['PATH'].split(";")
            JAVA_HOME = "C:\Program Files\Plms\installed\jdk-17.0.5"

            if var[-1] == JAVA_HOME:
                print("无需重复设置同版本的jdk!")         # 这里抛异常

            tmp = []
            for acc in var:
                pattern_1 = r"jdk-"
                pattern_2 = r"\\java\\"
                if re.search(pattern_1, acc) or re.search(pattern_2, acc) is None:
                    tmp.append(acc)

            PATH = ";".join(tmp)

            os.system("wmic ENVIRONMENT where \"name='JAVA_HOME'\" delete")

            os.system(
                f"wmic ENVIRONMENT create name=\"JAVA_HOME\","
                f"username=\"<system>\", VariableValue= \"{JAVA_HOME}\""
            )

            os.system(
                f"wmic ENVIRONMENT where \"name='Path' and username='<system>'\" "
                f"set VariableValue= \"{PATH};{JAVA_HOME}\\bin\""
            )

        else:
            pass

            # for url_tar_gz in self.__download_path:
            #     pattern = r".tar.gz"
            #     if re.search(pattern, url_tar_gz):  # 如果目标url以.tar.gz结尾，则将其复制给变量__url，以便调用下载.
            #         urllib.request.urlretrieve(url_tar_gz, self.__install_path + "\\Java.tar.gz")

        pass


if __name__ == "__main__":
    DD = use()
    DD.java_use()
    pass
