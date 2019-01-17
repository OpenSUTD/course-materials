# Important note: Do NOT submit projects here as of Jan 2019! The projects here will be given another home eventually.
This is a crowd-sourced collection of useful projects, scripts, and tools from the SUTD community.

## List of Projects
* **SUTD to Simei Bot**, benghaun  
`python` `telegram`  
Telegram bot that helps you decide which bus stop to go to in order to take Bus 5/20 to Simei.

* **Edimension Auto-login extension**, joel huang  
`javascript` `chrome extension`  
Hacked together a quick fix to log you in when you're logged out of eDimension. Assumes you have Chrome auto-fill, but doesn't store any of the plaintext (check the source before using).

* **SUTD Timetable**, Shun Git  
`heroku` `timetable`  
A .ics generator for timetables.

* **SUTD Data**, Shun Git  
`raw`  
Static data for SUTD.

* **Jupyter Service**, Isaac  
`python` `jupyter` `telegram`  
Telegram bot that sends you a link to a jupyter notebook once you power your raspberry pi up

* **Laser cut calipers**, Isaac  
`SVG` `hardware` `tools`  
Laser cut vernier calipers with depth rod. Beginner-intermediate project.

* **kyancer_bot**, Isaac
`python` `telegram`  
Telegram bot that converts your text to headaches using inline queries. 

## Contributing a folder
NB: If you are using windows ang git bash, open up a terminal (powershell or cmd is fine) in with admin access and use `git config core.longpaths true` to handle long file names.
### If you are not a collaborator yet!
* If you are not a collaborator yet, it's a little more complicated:
   1. `fork` this repository by clicking the fork button above. This creates a copy of opensutd under your GitHub account
   2. `git clone https://github.com/yourgithubid/opensutd`
   3. `cd opensutd`, add the original repository as remote by running `git remote add upstream https://github.com/joel-huang/opensutd`
   4. On your local copy, either (a) copy your project folder into `/Projects`, or (b) run `git submodule add https://github.com/your/repo` from the `/Projects` directory, depending on whether your project exists as a folder on your computer or another GitHub repository
   5. `git add -A`, `git commit -m "added myprojectname"`, `git push`
   6. Now _your_ copy of opensutd is updated. Navigate to the _original_ opensutd, and click the green pull request button. You should see your fork! Submit your pull request
   7. Remember to update your fork next time you want to contribute, using `git pull upstream master` before doing anything

### If you are a collaborator!
#### 1. Uploading your folder
##### Your project is an existing Github repository
* Create a new branch on the browser `myprojectname`
* `cd` to `opensutd` on your disk
* `git pull` to get the latest version
* `git checkout myprojectname` to switch to your branch
* `cd Projects`
* `git submodule add https://github.com/you/repo`, replace with your repo
* `git add -A`, `git commit -m "added myprojectname"`, `git push`
* Submit pull request into `master`

##### Your project resides on a folder on your computer
* Create a new branch on the browser `myprojectname`
* `cd` to `opensutd` on your disk
* `git pull` to get the latest version
* `git checkout myprojectname` to switch to your branch
* Copypasta your folder into `/Projects`
* `git add -A`, `git commit -m "added myprojectname"`, `git push`
* Submit pull request into `master`

#### 2. Documentation
##### What's your project about?
Your folder should include a `README.md` file at the top level. For example, `opensutd/Projects/MyProjectName/README.md`. For markdown formatting help there's [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) or [Stackedit](https://stackedit.io/app)!
##### Update *this* readme
Remember to update the list of projects on this readme with a short overview as well!

