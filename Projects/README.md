# OpenSUTD/Projects
This is a crowd-sourced collection of useful projects, scripts, and tools from the SUTD community.
## List of Projects
* **SUTD to Simei Bot**, benghaun
`python` `telegram`
Telegram bot that helps you decide which bus stop to go to in order to take Bus 5/20 to Simei.

## Contributing a folder
### 1. Uploading your folder
#### Your project is an existing Github repository
* Create a new branch `myprojectname`
* `cd` to `opensutd` on your disk
* `git checkout myprojectname` to switch to your branch
* `cd Projects`
* `git submodule add https://github.com/you/repo`, replace with your repo
* `git add -A`, `git commit -m "added myprojectname"`, `git push myprojectname`
* Submit pull request into `master`

#### Your project resides on a folder on your computer
* Create a new branch `myprojectname`
* `cd` to `opensutd` on your disk
* `git checkout myprojectname` to switch to your branch
* Copypasta your folder into `Projects`
* `git add -A`, `git commit -m "added myprojectname"`, `git push myprojectname`
* Submit pull request into `master`
### 2. Documentation
#### What's your project about?
Your folder should include a `README.md` file at the top level. For example, `opensutd/Projects/MyProjectName/README.md`. For markdown formatting help there's [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) or [Stackedit](https://stackedit.io/app)!
#### Update *this* readme
Remember to update the list of projects on this readme with a short overview as well!

