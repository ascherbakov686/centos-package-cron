import os
import sys
import yum

class Package:
	def __init__(self,name,version,release):
		self.name = name
		self.version = version
		self.release = release

class PackageFetcher:
	def fetch_installed_packages(self):
		yb = yum.YumBase()
		yb.setCacheDir()
		packages = yb.rpmdb.returnPackages()
		result = map(lambda x: Package(x.name,x.version,x.release), packages)
		return result