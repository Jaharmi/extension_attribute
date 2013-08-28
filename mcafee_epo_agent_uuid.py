#!/usr/bin/python

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

import ConfigParser


def get_ini_key(this_file, this_section, this_key):
    config = ConfigParser.ConfigParser()
    config.read(this_file)

    try:
        ini_key = config.get(this_section,
                             this_key)
    except ConfigParser.NoOptionError:
        ini_key = '00000000-0000-0000-0000-000000000000'
    except ConfigParser.NoSectionError:
        ini_key = '00000000-0000-0000-0000-000000000000'    
    return ini_key


def clean_ini_key(this_ini_key):
    prefix = 'sz{'
    suffix = '}'
    if this_ini_key.startswith(prefix) and this_ini_key.endswith(suffix):
        ini_key = this_ini_key[len(prefix):-len(suffix)]
    else:
        ini_key = this_ini_key
    return ini_key


def print_extension_attribute(this_extension_attribute):
    extension_attribute_result = "<result>{0}</result>".format(this_extension_attribute)
    print(extension_attribute_result)


def main():
    registry_file = '/Library/McAfee/cma/scratch/registry.ini'
    registry_section = '\\'.join(['HKEY_LOCAL_MACHINE',
                                  'SOFTWARE',
                                  'Network Associates',
                                  'ePolicy Orchestrator',
                                  'Agent'])
    registry_key = 'AgentGUID'
    registry_value = get_ini_key(registry_file, registry_section, registry_key)
    extension_attribute = clean_ini_key(registry_value)
    print_extension_attribute(extension_attribute)


if __name__ == "__main__":
    main()
