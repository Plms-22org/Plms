#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import hashlib

from libcore.utill.json_parser import Jsonfile


class FileVerifier(Jsonfile):
    __encryption_algorithm_id = None
    __encryption_algorithm_type = None

    def judge_cultural_security(self, file: str):
        """
        根据文件判断需要选择的加密算法

        file: 文件的绝对路径
        """
        self.__get_encryption_type_and_id()
        file_name = file.split("\\")[-1].split("-")[0]

        if file_name == "jdk":
            return self.check_file_sha256(filepath=file)
        pass

    def __get_encryption_type_and_id(self):
        """
        获取目标文件的加密算法类型和id
        """
        self.get_file_encryption_algorithm_and_id()

        self.__encryption_algorithm_type = self.get_file_encryption_algorithm()  # 获取目标文件的加密算法类型
        self.__encryption_algorithm_id = self.get_file_encryption_algorithm_id()  # 获取目标文件的加密id

    def check_file_sha256(self, filepath: str) -> bool:
        """
        校验文件的sha256是否正确
        """
        with open(filepath, "rb") as f:
            sha256_obj = hashlib.sha256()
            sha256_obj.update(f.read())
            hash_value = sha256_obj.hexdigest()

        if hash_value == self.__encryption_algorithm_id:
            return True
        else:
            return False


if __name__ == "__main__":
    pass
