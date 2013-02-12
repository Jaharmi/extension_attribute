#!/usr/bin/python

import os
import Foundation
import sys

xprotect_meta_plist = "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/XProtect.meta.plist"
plist_nsdata, error_msg = Foundation.NSData.dataWithContentsOfFile_options_error_(xprotect_meta_plist, Foundation.NSUncachedRead, None)
xprotect_meta, plist_format, error_msg = Foundation.NSPropertyListSerialization.propertyListFromData_mutabilityOption_format_errorDescription_(plist_nsdata, Foundation.NSPropertyListMutableContainers, None, None)

extension_attribute = xprotect_meta['PlugInBlacklist']['10']['com.macromedia.Flash Player.plugin']['MinimumPlugInBundleVersion']
print('%s' % extension_attribute)