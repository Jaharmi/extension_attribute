#!/usr/bin/python

import subprocess
import sys
sys.path.append("/usr/local/munki")
from munkilib import FoundationPlist as plistlib

pkgutil_path = "/usr/sbin/pkgutil"


def list_packages_as_plist(this_pkg_id):
    cmd = [pkgutil_path, "--pkgs={0}".format(this_pkg_id)]
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
