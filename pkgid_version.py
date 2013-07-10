#!/usr/bin/python

# Copyright (c) 2013 by Jeremy Reichman <jaharmi@jaharmi.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import subprocess
import sys
sys.path.append("/usr/local/munki")
from munkilib import FoundationPlist as plistlib

pkgutil_path = "/usr/sbin/pkgutil"


def list_packages_as_plist(this_pkg_id):
    cmd = [pkgutil_path, "--pkgs-plist"]
    cmd_output = subprocess.check_output(cmd)
    cmd_output_plist = plistlib.readPlistFromString(cmd_output)
    return cmd_output_plist


def get_pkgid_version(this_pkg_plist, this_pkg_id):
    if this_pkg_id in this_pkg_plist:
        cmd = [pkgutil_path, "--pkg-info-plist", this_pkg_id]
        cmd_output = subprocess.check_output(cmd)
        cmd_output_plist = plistlib.readPlistFromString(cmd_output)
        pkg_version = cmd_output_plist['pkg-version']
        return pkg_version
    else:
        return False


def print_extension_attribute(this_extension_attribute):
    extension_attribute_result = "<result>{0}</result>".format(this_extension_attribute)
    print(extension_attribute_result)


def main():
    pkg_id = "com.googlecode.munki.core"
    pkg_plist = list_packages_as_plist(pkg_id)
    extension_attribute = get_pkgid_version(pkg_plist, pkg_id)
    print_extension_attribute(extension_attribute)

if __name__ == "__main__":
    main()
