#!/usr/bin/env python

class GitClient(object):
	def __init__(self):
		pass

	def accountUrls(self, account):
		return {'hoge': 'aaaaaaaaaaaaaaaaaaaaa'}

	def watchUrls(self):
		pass

	def forkUrls(self):
		pass

class Gits:
	def __init__(self):
		self.account = None
		self.oauth_token = None
		self.oauth_secret = None
		self.client = GitClient()

	def cloneRepos(self, account, watch, fork):
		if account is None:
			self._cloneAccountRepos(account)
		elif watch:
			self._cloneWatchRepos()
		elif fork:
			self._cloneForkRepos()

	def pullRepos(self, account, watch, fork):
		if account is None:
			self._pullAccountRepos(account)
		elif watch:
			self._pullWatchRepos()
		elif fork:
			self._pullForkRepos()

	def _cloneAccountRepos(self, account):
		urls = self.client.accountUrls(account)
		for (repo, url) in urls:
			print "%s: %s" % (repo, url)
	
	def _pullAccountRepos(self, account):
		pass

	def _cloneWatchRepos(self):
		pass

	def _pullWatchRepos(self):
		pass

	def _cloneForkRepos(self):
		pass

	def _pullForkRepos(self):
		pass

def main():
	g = Gits()
	pass


if __name__ == '__main__':
	main()
