#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import json  # 该模块用于解析 Json 文件
import os
import re  # 用于匹配字符串
from libcore.exception.config_key_not_exist_exception import ConfigKeyNot_ExistException
from libcore.utill.system_information import SystemInformation


class Jsonfile(SystemInformation):
    __all_url = []  # 保存所有可能的下载 url
    __json_list = None
    __jsonfile_path = None  # 保存 Json 文件路径
    __now_system = None  # 保存当前操作系统
    __download_url = None  # 保存下载文件的 url
    __DocumentContent = None  # 保存 Json 内容
    __now_system_architecture = None  # 保存系统的架构信息
    __file_encryption_algorithm = None  # 保存文件加密算法
    __file_encryption_algorithm_id = None  # 文件加密算法产生的id

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
            self.__jsonfile_path = "repository-server-template/apps/oracle/versions"
        elif app == "python":
            pass
        elif app == "Go":
            pass

        return self.__jsonfile_path + "/" + version + ".json"

    def analysis_json(self, app: str = None, version: str = None) -> list:
        """
        解析的 Json 文件, 转换为 list 格式
        return: jsonstr
        """
        # 获取 Json 文件路径
        jsonfile_path = self.__get_json_path(app="java", version="17.0.5")  # 此处参数待修改
        # 打开并解析 Json文件
        self.__json_list = json.loads(self.open_json(filename=jsonfile_path))  # 将 Json 字符串转换为 python list 格式
        return self.__json_list

    def analysis_json_url(self, app: str = None, version: str = None) -> None:
        """
        根据解析的 Json 文件内容, 获得对应版本 Java 的下载 Url。
        :return: None
        """
        # 获取系统信息
        self.system_information()
        self.__now_system = self.now_system()  # 获取操作系统信息
        self.__now_system_architecture = self.now_system_architecture()  # 获取系统架构信息

        jsonlist = self.analysis_json()
        for dict_m in jsonlist:  # 遍历list， 取出字典
            for key in dict_m:  # 遍历字典， 匹配key
                if dict_m[key] == self.__now_system:  # 如果key(os) = 系统，进行下一步
                    var_machine = dict_m["arch"]
                    if var_machine == self.__now_system_architecture:  # 如果key(os) = 系统，而且 key(arch) = 系统架构，取得对应url并保持到变量__Url中。
                        url = dict_m["url"]
                        self.__all_url.append(url)  # 存储所有可用的url

    def get_download_url(self) -> str:
        """
        获取指定url
        :return:
        """
        self.analysis_json_url()

        if self.__now_system == "Windows":
            pattern = r".zip"
            for url_zip in self.__all_url:
                if re.search(pattern, url_zip):  # 如果目标url以.exe结尾，则返回下载url.
                    self.__download_url = url_zip
                    return url_zip

        elif self.__now_system == "Linux":
            pass
        elif self.__now_system == "macOS":
            pass

    def get_url_exe(self):
        pass

    def get_file_encryption_algorithm_and_id(self):
        """
        解析文件的 加密算法 和 id
        """
        json_str = self.analysis_json()
        dict_value = self.get_download_url()

        for algo_l in json_str:
            for algo_d in algo_l:
                if algo_l["url"] == dict_value:
                    self.__file_encryption_algorithm = algo_l["checksum"]["algo"]
                    self.__file_encryption_algorithm_id = algo_l["checksum"]["content"]

    def get_file_encryption_algorithm(self):
        """
        ## 前置函数: __get_file_security_algorithm_and_id ##
        获取加密算法名
        """
        return self.__file_encryption_algorithm

    def get_file_encryption_algorithm_id(self):
        """
        ## 前置函数: __get_file_security_algorithm_and_id ##
        获取加密算法后的ID
        """
        return self.__file_encryption_algorithm_id


if __name__ == "__main__":
    pass
