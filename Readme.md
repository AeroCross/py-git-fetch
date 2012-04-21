# py-git-fetch

Searches all Git repositories inside a folder and fetches the latest changes in them.

__Author:__ Mario Cuba <<mario@mariocuba.net>>

## License

Released to the Public Domain under the [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0).

### Requirements

- Python 2.6.1
- Git 1.7.x

### Instructions

Copy the script anywhere in your hard drive, and execute it via Python:

	python git-fetch.py <path>
	
The scripts accepts a `path` parameter that will be used as the __root folder__ &mdash; where the script start looking in its subfolders for Git repositories.

The script, by default, runs `git fetch --all --prune` in every single Git repository it finds.

### Todo's

- Pass custom parameters to the fetch command
- Use the current folder if no parameter is passed
- Enable simultaneous fetching