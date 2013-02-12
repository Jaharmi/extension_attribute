#!/usr/bin/python

#   Copyright (c) 2013 by Jeremy Reichman <jaharmi@jaharmi.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import os
import Foundation
import sys

xprotect_meta_plist = "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/XProtect.meta.plist"
plist_nsdata, error_msg = Foundation.NSData.dataWithContentsOfFile_options_error_(xprotect_meta_plist, Foundation.NSUncachedRead, None)
xprotect_meta, plist_format, error_msg = Foundation.NSPropertyListSerialization.propertyListFromData_mutabilityOption_format_errorDescription_(plist_nsdata, Foundation.NSPropertyListMutableContainers, None, None)

extension_attribute = xprotect_meta['LastModification']
print('%s' % extension_attribute)