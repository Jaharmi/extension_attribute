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

import sys
sys.path.append("/usr/local/munki")
from munkilib import FoundationPlist as plistlib
from dateutil import parser
from dateutil import tz
import time


def print_extension_attribute(this_extension_attribute):
    extension_attribute_result = "<result>{0}</result>".format(this_extension_attribute)
    print(extension_attribute_result)


def main():
    install_report_path = "/Library/Managed Installs/ManagedInstallReport.plist"
    install_report_data = plistlib.readPlist(install_report_path)

    install_end = install_report_data['EndTime']

    install_end_parsed = parser.parse(install_end)

    to_zone = tz.gettz(time.tzname[time.daylight])
    install_end_local = install_end_parsed.astimezone(to_zone)

    result_date_format = "%Y-%m-%d %H:%M:%S"
    install_end_date = install_end_local.strftime(result_date_format)

    extension_attribute = install_end_date
    print_extension_attribute(extension_attribute)

if __name__ == "__main__":
    main()
