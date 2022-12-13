#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import json  # 该模块用于解析 Json 文件
import os
import re
from libcore.exception.config_key_not_exist_exception import ConfigKeyNot_ExistException
from libcore.utill.system_information import SystemInformation


class Jsonfile(SystemInformation):
    __all_url = []
    __file_path = None
    __now_system = None
    __DocumentContent = None

    def open_json(self, filename: str = None) -> str:
        """
        打开并记录 json 文件。
        :param filename:
        :return:
        """
        if (filename is None) or (len(filename)) == 0:
            raise ConfigKeyNot_ExistException("No input file.".format())

        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as Document_content:
                self.__DocumentContent = Document_content.read()  # 将 Json 文件内容保存到变量中
                Document_content.close()  # 信息收集完成即关闭文件
        return self.__DocumentContent

    def __get_json_path(self, app: str, version: str) -> str:
        """
        获得 json 文件路径。
        :return:
        """
        # 判断系统，返回 Json 文件所在文件夹路径
        if app == "java":
            self.__file_path = "repository-server-template/apps/oracle/versions"
        elif app == "python":
            pass
        elif app == "Go":
            pass

        return self.__file_path + "/" + version + ".json"

    def analysis_json(self, app: str = None, version: str = None) -> None:
        """
        解析 Json 文件, 获得对应版本 Java 的下载 Url。
        :return: None
        """
        # 获取系统信息
        self.system_information()
        self.__now_system = self.now_system()  # 获取操作系统信息
        now_system_architecture = self.now_system_architecture()  # 获取系统架构信息

        # 获取 Json 文件路径
        jsonfile_path = self.__get_json_path(app="java", version="17.0.5")  # 此处参数待修改

        # 打开并解析 Json文件
        jsonstr = json.loads(self.open_json(filename=jsonfile_path))  # 将 Json 字符串转换为 python list 格式
        for dict_m in jsonstr:  # 遍历list， 取出字典
            for key in dict_m:  # 遍历字典， 匹配key
                if dict_m[key] == self.__now_system:  # 如果key(os) = 系统，进行下一步
                    var_machine = dict_m["arch"]
                    if var_machine == now_system_architecture:  # 如果key(os) = 系统，而且 key(arch) = 系统架构，取得对应url并保持到变量__Url中。
                        url = dict_m["url"]
                        self.__all_url.append(url)  # 存储所有可用的url

    def get_download_url(self) -> str:
        """
        获取指定url
        :return:
        """
        self.analysis_json()

        if self.__now_system == "Windows":
            pattern = r".zip"
            for url_exe in self.__all_url:
                if re.search(pattern, url_exe):  # 如果目标url以.exe结尾，则返回下载url.
                    return url_exe

        elif self.__now_system == "Linux":
            pass
        elif self.__now_system == "macOS":
            pass

    def get_url_exe(self):
        pass


if __name__ == "__main__":
    pass
