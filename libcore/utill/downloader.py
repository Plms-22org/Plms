#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import datetime
import os.path  # 关于系统操作的基础库
import urllib.request  # 用于下载文件的包
import zipfile  # 该模块用于解压zip包
from libcore.utill.file_verifier import FileVerifier
from libcore.config.config import Config
from libcore.utill.json_parser import Jsonfile


class Download(Jsonfile, Config):
    __install_path = None
    __check_file_id = None  # 保存 sha256 的值
    __system = None  # 保存当前操作系统
    __cache_path = None  # 缓存保存路径
    __config_path = None  # 配置文件路径
    __download_path = None  # 下载 url
    __local_file_path_for_windows = None  # 保存安装包的保存位置

    def __get_variables(self):
        """
        获得本地文件路径。
        :return:
        """
        self.system_information()
        self.__system = self.now_system()  # 获取当前操作系统信息
        self.__version = "17.0.5"
        self.init_path()  # 初始化 各种路径
        self.__download_path = self.get_download_url()  # 获取文件的下载 url ，来自 libcore.utill.json_parser.Jsonfile
        self.__install_path = self.get_install_path()  # 获取
        self.__cache_path = self.get_cache_path()  # 获取缓存路径， 来自 libcore.config.config.Config
        self.__config_path = self.get_config_path()  # 获取配置文件路径 来自 libcore.config.config.Config

    def download(self):
        pass

    def download_for_windows(self) -> str:
        """
        从指定url下载压缩包。
        :return: None
        """
        now_time = datetime.datetime.now()
        self.__get_variables()
        Path_character_for_windows = "\\"
        Name_character = "-"
        Filename = "jdk"
        Filename_suffix_zip = ".zip"
        self.__local_file_path_for_windows = self.__cache_path + Path_character_for_windows + Filename \
                                           + Name_character + self.__version + Name_character \
                                           + now_time.strftime("%Y%m%d-%H%M%S") + Filename_suffix_zip

        if self.__system == "Windows":
            self.All_directories_must_exist(self.__cache_path)  # 判断目录是否存在，如不存在则创建目录
            urllib.request.urlretrieve(self.__download_path, self.__local_file_path_for_windows)
            check_file = FileVerifier()
            sha256_result = check_file.judge_cultural_security(file=self.__local_file_path_for_windows)
            if sha256_result:
                print("文件下载完成，并通过sha256校验！")
                return self.__local_file_path_for_windows
            else:
                print("文件校验失败！请检查文件(path: {})".format(self.__local_file_path_for_windows))
                return ""

    def download_for_oxs(self):
        if self.__system == "macOS":
            # for url_tar_gz in self.__download_path:
            #     pattern = r".tar.gz"
            #     if re.search(pattern, url_tar_gz):  # 如果目标url以.tar.gz结尾，则将其复制给变量__url，以便调用下载.
            #         urllib.request.urlretrieve(url_tar_gz, self.__install_path + "\\Java.tar.gz")
            self.All_directories_must_exist(self.__cache_path)
            urllib.request.urlretrieve(self.__download_path, self.__cache_path + "\\jdk" + self.__version + ".tar.gz")

    def download_for_linux(self):
        pass

    @staticmethod
    def must_exist(filepath: str) -> None:
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

    def get_local_file_path_for_windows(self) -> str:
        return self.local_file_path_for_windows


if __name__ == "__main__":
    pass
