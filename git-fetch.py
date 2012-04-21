# git-fetch.py – Search all Git repositories inside a folder and fetches the latest changes in them

# Version 1.0
# Author: Mario Cuba <mario@mariocuba.net>
# License: Creative Commons Attribution 3.0 Unported License (see: http://creativecommons.org/licenses/by/3.0)

# import needed modules
import os;
import subprocess;
from sys import argv;

# clears out buffer
os.system('clear');

# check for correct arguments
arglen = len(argv);
maxlen = 2;

if (arglen < 2):
	print "Path was not specified.";
	exit();
elif (arglen > 2):
	for x in range(arglen - maxlen):
		del argv[maxlen];

## unpack parameters
else:
	SCRIPTNAME, PATH = argv;

## does the path exists?
if (os.path.exists(PATH) == False):
	print "Path does not exists.";
	exit();

# walk though the folder
for path, folders, files in os.walk(PATH):
	for current in folders:
		current_folder = os.path.join(path, current);

		# check if the folder is a git repository
		if (os.path.exists(os.path.join(current_folder, ".git"))):
			print "Git repository found in " ,current_folder;

			## navigate to folder and execute the fetching
			os.chdir(current_folder);
			retcode = subprocess.call(["git", "fetch", '--all', '--prune']);

			if (retcode == 0):
				print "Fetched latest changes.";
			else:
				print "Couldn't fetch latest changes.";
			
			# add a line break after each folder
			print;