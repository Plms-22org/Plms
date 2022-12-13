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

    __filename = None
    __install_path = None

    __cache_path = None
    __config_path = None
    __download_path = None
    __app_install_path = None

    def __get_variables(self):
        """
        获得本地文件路径。
        :return:
        """
        self.__version = "17.0.5"
        self.init_path()  # 初始化 各种路径
        self.__download_path = self.get_download_url()  # 获取文件的下载 url ，来自 libcore.utill.json_parser.Jsonfile
        self.__install_path = self.get_install_path()  # 获取
        self.__app_install_path = self.get_app_install_path()  # 获得app文件的安装路径， 来自libcore.config.config.Config
        self.__cache_path = self.get_cache_path()  # 获取缓存路径， 来自 libcore.config.config.Config
        self.__config_path = self.get_config_path()  # 获取配置文件路径 来自 libcore.config.config.Config

    def download(self):
        """
        从指定url下载压缩包。
        :return: None
        """
        self.__get_variables()
        self.system_information()
        System = self.now_system()

        if System == "Windows":
            self.All_directories_must_exist(self.__cache_path)  # 判断目录是否存在，如不存在则创建目录
            urllib.request.urlretrieve(self.__download_path, self.__cache_path + "\\jdk" + self.__version + ".zip")
            self.unzip()

        elif System == "macOS":
            # for url_tar_gz in self.__download_path:
            #     pattern = r".tar.gz"
            #     if re.search(pattern, url_tar_gz):  # 如果目标url以.tar.gz结尾，则将其复制给变量__url，以便调用下载.
            #         urllib.request.urlretrieve(url_tar_gz, self.__install_path + "\\Java.tar.gz")
            self.All_directories_must_exist(self.__cache_path)
            urllib.request.urlretrieve(self.__download_path, self.__cache_path + "\\jdk" + self.__version + ".tar.gz")

    def check_sha256(self) -> None:
        """
        检查文件的sha是否正确
        """
        pass

    def unzip(self, filepath: str = None):
        """
        本方法用于将 zip 文件解压至指定文件夹。
        :return:
        """
        zipfilepath = self.__cache_path + "\\jdk" + self.__version + ".zip"  # 要解压的文件路径
        self.__filename = ""

        self.Must_exist(self.__app_install_path)
        file = zipfile.ZipFile(zipfilepath, 'r')
        self.__filename = file.namelist()[0].strip("/")
        
        file.read(file.namelist()[0])
        for zipfile_un in file.namelist():
            file.extract(zipfile_un, self.__app_install_path)
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

    def set_jdk_env_var(self):
        """
        该方法用于设置jdk环境变量。
        :return:
        """

        # os.system("wmic ENVIRONMENT where \"name='JAVA_HOME'\" delete")
        java_home = " "
        os.system("set JAVA_HOME=C:\Program Files\Plms\installed\jdk-17.0.5")
        os.system("set PATH=%JAVA_HOME%\bin")
        pass


if __name__ == "__main__":
    pass
