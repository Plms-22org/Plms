#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import os  # 与系统有关的模块
import configparser  # 该模块用于解析 ini 文件


class Configfile:
    def __init__(self):
        self.__install_path_default = None
        self.__version_str = None  # 保存将软件版本号修改为 "10-10-10" 形式信息，用于重命名安装包。

    def who_is_my_config(self):
        """
        本方法用于判断程序当前适用的配置信息
        :return: None
        """
        global path
        path_ini = "assets/Plms-confing.ini"
        path_bak = "assets/.Plms-confing.ini.template"
        path_default = self.__install_path_default

        if os.path.exists(path_ini):  # 判断ini文件是否存在，如果存在则直接读取使用
            path = path_ini
        elif not os.path.exists(path_ini):  # 如果 ini 文件不存在，则尝试使用 .Plms-confing.ini.template 文件
            if os.path.exists(
                    path_bak):  # 如果 ini 文件不存在，但是 .Plms-confing.ini.template 文件存在，则使用.Plvmes_confing.ini.template
                path = path_bak
            elif os.path.exists(path_bak):  # 如果 .Plms-confing.ini.template 文件不存在，则使用程序默认路径
                path = path_default

        config = configparser.ConfigParser()
        config.read(path, encoding="utf-8")
        localpath = config["app"]["Local_path"]  # 读取ini文件中的本地安装路径

    def pathname(self, version: str):
        self.__version_str = version.replace(".", "-")  # 将输入的version中的 "." 替换为 "-"
        pass
        pass


if __name__ == "__main__":
    pass
