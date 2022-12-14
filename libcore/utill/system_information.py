#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import os
import platform  # 该模块用于显示操作系统信息
import getpass  # 该模块用于显示当前用户名

from libcore.exception.file_is_empty import FileIsEmpty
from libcore.exception.get_system_info_exception import GetSystemInfoException
from libcore.exception.not_support_system_type_exception import NotSupportSystemTypeException


class SystemInformation:
    """
    系统信息
    """
    # 字典用于统一不同版本架构的系统信息
    System_architecture_information_correction = {
        "x86_64": "x64",
        "win64": "x64",
        "AMD64": "x64",
        "win32": "x64"
    }

    def __init__(self):
        self.__System_architecture = None  # 保存操作系统的架构信息
        self.__System = None  # 保存操作系统名
        self.__now_user = None  # 保存当前用户名
        self.__now_user_path = None  # 保存当前 home目录
        self.__now_system_Root = None  # 保存windows操作系统盘符

    def system_information(self) -> None:
        """
        本方法用于获取当前系统信息。
        :return:  None
        """
        self.__System = platform.system()  # 得出操作系统名称
        self.__System_architecture = self.System_architecture_information_correction[platform.machine()]  # 得到操作系统的架构
        self.__now_user_path = getpass.getuser()  # 获取当前用户

        if FileIsEmpty.is_empty(self.__now_user_path):
            raise GetSystemInfoException("Failed to get system user!")

        if self.__System == "Windows":
            self.__now_user_path = os.path.expandvars('$HOMEPATH').strip()  # windows python3.8 以上使用本参数获取用户路径
            self.__now_system_Root = os.getenv("SystemDrive", default="C:").strip()  # 获取windows操作系统盘符
            if FileIsEmpty.is_empty(self.__now_system_Root):
                raise GetSystemInfoException("Illegal system path: {}!".format(self.__now_system_Root))

        elif self.__System == "Linux":
            self.__now_user_path = getpass.getuser().strip()

        elif self.__System == "mac0S":
            self.__now_user_path = getpass.getuser().strip()

        else:
            raise NotSupportSystemTypeException("{} is an unsupported operating system!".format(self.__System))

    def now_system(self) -> str:
        """
        返回当前系统，需要先调用 "system_information" 函数。
        :return: self.__System
        """
        return self.__System

    def now_system_architecture(self) -> str:
        """
        返回当前系统架构，需要先调用 "system_information" 函数。
        :return: self.__System_architecture
        """
        return self.__System_architecture

    def now_user(self) -> str:
        """
        本方法返回当前系统用户。
        :return:
        """
        return self.__now_user_path

    def now_system_Root(self):
        """
        本方法返回windows操作系统的系统盘盘符
        :return: str
        """
        return self.__now_system_Root


if __name__ == "__main__":
    pass
