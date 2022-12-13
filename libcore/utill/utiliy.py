#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


class Utiliy:

    def Convert_string_to_tuple(self, line: str) -> tuple:
        """
        将字符串解析为 Python 对象
        :param line: 字符串数据
        :return: Python 对象
        """
        if (len(line) <= 0) or (line is None):
            return ()

        tmp = []

        line = line.strip()
        cols = line.split("}, ")

        for col in cols:
            if (len(col) == 0) or (col is None):
                tmp.append(None)
            else:
                tmp.append(col.strip())

        return tuple(tmp)

    pass


if __name__ == "__main__":
    pass
