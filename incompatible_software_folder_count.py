#!/usr/bin/python

# Copyright (c) 2016 by Jeremy Reichman <jaharmi@jaharmi.com>
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

# Counts the number of items in the "Incompatible Software" folder
# https://support.apple.com/en-us/HT201861

import os


def print_extension_attribute(this_extension_attribute):
    extension_attribute_result = "<result>{0}</result>".format(this_extension_attribute)
    print(extension_attribute_result)


def main():
    folder_name = "Incompatible Software"
    folder_path = "/{0}".format(folder_name)
    if os.path.isdir(folder_path):
        folder_contents_raw = set(os.listdir(folder_path))
        folder_contents_filters = set(['.DS_Store', '.localized'])
        folder_contents_filtered = folder_contents_raw - folder_contents_filters
        folder_count = len(folder_contents_filtered)
    else:
        folder_count = 0
    extension_attribute = folder_count
    print_extension_attribute(extension_attribute)

if __name__ == "__main__":
    main()
