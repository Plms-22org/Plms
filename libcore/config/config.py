#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import configparser
import os.path

from libcore.exception.config_key_not_exist_exception import ConfigKeyNot_ExistException
from libcore.exception.configuration_file_parsing_error import ConfigurationFileParsingError
from libcore.exception.file_is_empty import FileIsEmpty
from libcore.utill.system_information import SystemInformation


class Config:
    __version = None
    __default_config = None
    __default_mirror = None
    __default_language = "en_US"
    __default_publisher = "Oracle"

    __install_path = None
    __app_install_path = None
    __cache_path = None
    __config_path = None

    __allow_config_keys = (
        'mirror',
        'language',
        'publisher'
    )

    def __init_default_install_path(self):
        System = SystemInformation()
        System.system_information()
        system_usr = System.now_user()
        system = System.now_system()
        if system == "Windows":
            system_Root = System.now_system_Root()
            self.__install_path = system_Root + "\Program Files\Plms"
            self.__app_install_path = system_Root + "\Program Files\Plms\installed"
            self.__cache_path = system_Root + "\Program Files\Plms\cache"
            self.__config_path = system_Root + system_usr + "\AppData\Local\Plms\config"
        elif system == "Linux":
            self.__install_path = "/usr/local/bin/Plms"
            self.__app_install_path = "/usr/local/Plms/installed"
            self.__cache_path = "/usr/local/Plms/cache"
            self.__config_path = "/home/" + system_usr + "/.Plms/config"
        elif system == "Darwin":
            self.__install_path = "/usr/local/bin/Plms"
            self.__app_install_path = "/usr/local/Plms/Installed"
            self.__cache_path = "/usr/local/Plms/Cache"
            self.__config_path = "/Users/" + system_usr + "/.Plms/Config"

    def __init_config_path(self):
        """
        初始化配置文件默认路径。
        :return: None
        """
        config_path = SystemInformation()
        config_path.system_information()  # 初始化
        system_usr = config_path.now_user()  # 系统用户
        now_system = config_path.now_system()  # 操作系统
        if now_system == "Windows":
            system_Root = config_path.now_system_Root()  # 如果系统为windows， 则需要配置系统盘盘符
            self.__default_config = system_Root + system_usr + "\AppData\Local\Plms\config\.Plms\config\Plms-config.ini"
        elif now_system == "Linux":
            self.__default_config = "/home/" + system_usr + "/.Plms/config/Plms-config.ini"
        elif now_system == "Darwin":
            self.__default_config = "/Users/" + system_usr + "/.Plms/Config/Plms-config.ini"

    def __load_config_file(self) -> bool:
        """
        加载配置文件,
        如果文件不存在, 使用默认路径;
        如果文件存在, 加载配置文件。
        :return: None
        """
        self.__init_config_path()

        filename = self.__default_config
        if os.path.exists(filename):
            self.__config = configparser.ConfigParser()
            self.__config.read(filename, encoding="utf-8")
            section = self.__config.sections()
            if "MainConfiguration" not in section:
                raise ConfigurationFileParsingError("An error occurred in the configuration file."
                                                    " Please check the configuration item.")
            else:
                self.__install_path = self.__config.get("MainConfiguration", "Install_path")
                self.__app_install_path = self.__config.get("MainConfiguration", "app_install_path")
                self.__cache_path = self.__config.get("MainConfiguration", "cache_path")
                self.__config_path = self.__config.get("MainConfiguration", "config_path")
                return True
        else:
            return False
            # raise FileDoesNotExist("The configuration file does not exist!")

    def init_path(self):
        """
        初始化各种安装路径。
        :return:
        """
        if self.__load_config_file() is False:
            self.__init_default_install_path()

    def __math_config(self, key: str) -> str:
        if key == "publisher":
            return self.__default_publisher
        elif key == "mirror":
            return self.__default_mirror
        elif key == "language":
            return self.__default_language

    def key_check(self, key: str):
        """
        检查输入的 key 是否正常。
        """
        if FileIsEmpty.is_empty(key):
            raise ConfigKeyNot_ExistException("{} is not in config file, because key is empty!".format(key))

        if key not in self.__allow_config_keys:
            raise ConfigKeyNot_ExistException("{} is not in config file, the specified key is illegal.".format(key))

    def get(self, key: str) -> str:
        """
        获取配置项
        :param key:
        :return:
        """
        self.key_check(key)
        key = key.strip()

        if self.__config is None:
            return self.__math_config(key)
        else:
            val = self.__config.get("MainConfiguration", key).strip()
            self.__math_config(key) if FileIsEmpty.is_empty(val) else val

    def set(self, key: str, value: str) -> bool:
        """
        设置配置项
        :param key:
        :param value:
        :return:
        """

    def get_with_default(self, key: str, default: str):
        """
        获取配置项，如果这个配置为空，则返回 default
        :param key:
        :param default:
        :return:
        """
        pass

    def get_install_path(self) -> str:
        return self.__install_path

    def get_app_install_path(self) -> str:
        return self.__app_install_path

    def get_cache_path(self) -> str:
        return self.__cache_path

    def get_config_path(self) -> str:
        return self.__config_path


if __name__ == "__main__":
    pass
