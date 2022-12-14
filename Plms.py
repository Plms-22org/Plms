#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
from libcore.utill.system_information import SystemInformation
from libcore.utill.json_parser import Jsonfile
from libcore.utill.downloader import Download
from libcore.utill.file_verifier import FileVerifier
from libcore.utill.plms_rar import PlmsRAR
import sys
import os
import optparse
import datetime
from time import strftime
from libcore.install.install import Install

def Plms():
    pass


if __name__ == "__main__":
    install = Install()
    install.install()
    pass
