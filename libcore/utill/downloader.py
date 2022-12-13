#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# import re  # 用于匹配字符串
import os.path
import urllib.request  # 用于下载文件的包
import zipfile  # 该模块用于解压zip包
import winreg
from libcore.utill.system_information import SystemInformation
from libcore.config.config import Config
from libcore.utill.json_parser import Jsonfile


class Download(Jsonfile, Config):
    __install_path = None
    __app_install_path = None
    __cache_path = None
    __config_path = None
    __download_path = None

    def __get_all_path(self):
        """
        获得本地文件路径。
        :return:
        """
        self.get_path()
        self.__download_path = self.get_download_url()       # 获取文件的下载 url ，来自 libcore.utill.json_parser
        self.__install_path = self.get_install_path()   #
        self.__app_install_path = self.get_app_install_path()
        self.__cache_path = self.get_cache_path()
        self.__config_path = self.get_config_path()

    def download(self):
        """
        从指定url下载压缩包。
        :return: None
        """
        self.__get_all_path()
        self.system_information()
        System = self.now_system()

        if System == "Windows":
            self.All_directories_must_exist(self.__install_path)  # 判断目录是否存在，如不存在则创建目录
            urllib.request.urlretrieve(self.__download_path, self.__install_path + "\\Java" + ".zip")
            self.unzip()

        elif System == "macOS":
            # for url_tar_gz in self.__download_path:
            #     pattern = r".tar.gz"
            #     if re.search(pattern, url_tar_gz):  # 如果目标url以.tar.gz结尾，则将其复制给变量__url，以便调用下载.
            #         urllib.request.urlretrieve(url_tar_gz, self.__install_path + "\\Java.tar.gz")
            if os.path.exists(self.__install_path) is False:
                os.makedirs(self.__install_path)

            urllib.request.urlretrieve(self.__download_path, self.__install_path + "\\Java" + ".tar.gz")

    def unzip(self, filepath: str = None):
        """
        本方法用于将 zip 文件解压至指定文件夹。
        :return:
        """
        zipfilepath = "C:\Program Files\Plms\java.zip"
        file = zipfile.ZipFile(zipfilepath, 'r')

        self.Must_exist("C:\Program Files\Plms\installed")

        for zipfile_s in file.namelist():
            file.extract(zipfile_s, "C:\Program Files\Plms\installed")
        pass

    def ungzip(self):
        """
        解压 tar.gz 文件
        :return:
        """

        pass

    @staticmethod
    def Must_exist(filepath: str) -> None:
        """
        如果目录不存在，则创建目录。
        :return:
        """
        if os.path.exists(filepath) is False:
            os.mkdir(filepath)

    @staticmethod
    def All_directories_must_exist(filepath) -> None:
        """
        如果目录不存在，则递归创建目录。
        :return:
        """
        if os.path.exists(filepath) is False:
            os.makedirs(filepath)

    def set_env_var(self):
        """
        该方法用于设置环境变量。
        :return:
        """

        pass


if __name__ == "__main__":
    pass
