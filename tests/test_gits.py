#!/usr/bin/env python

import _setup

import unittest
import gits

class TestGitClient(unittest.TestCase):
	def setUp(self):
		self.client = gits.GitClient()
		self.account = 'fukata'

	def testAccountUrls(self):
		urls = self.client.accountUrls(self.account)
		for repo in urls:
			print "%s: %s" % (repo, urls[repo])

if __name__ == '__main__':
	unittest.main()
