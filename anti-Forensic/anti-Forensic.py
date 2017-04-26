#!/usr/bin/env python
import os, sys, time
from src import admin_priv, Custom, RunHistory, SearchHistory, UsbLogREG, RecycleBin, Temp, UserAssist, Prefetch
__author__ = '@root_haxor'
__description__  = 'Personal Use Code for performing Anti-forensic actions'
if not admin_priv.isUserAdmin():
	admin.priv.runAsAdmin()
if __name__ == "__main__":
	Custom.clean()
	RunHistory.clean()
	SearchHistory.clean()
	UsbLogREG.clean()
	RecycleBin.clean()
	Temp.clean()
	UserAssist.clean()
	Prefetch.clean()
print "\n\n\nanti-Forensic tool prototype by %s" % __author__