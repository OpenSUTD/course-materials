# OpenSUTD
**Important note: This is crowd-contributed stuff that's really early in development and it'd be nice if this can be developed into a useful platform before it is shared around!**   

Knowledge should be available for everyone who wants to access it. MIT set up OpenCourseWare in the spirit of sharing knowledge with everybody - this is our take on it, and it'll be interesting to see what this evolves into!
## What this is
Hi there! This should be a space to encourage self-improvement and share knowledge, not spoon-feed it. What's fair game for contribution:
* Past lecture materials
* Past quiz, assignment, and homework questions
* Posters
* Project reports
* Personal notes and projects

What **shouldn't** be here:
* Quiz, examination, and homework **answers** (Tips and notes are fine)

## Contributing to OpenSUTD
**Anyone** can contribute material by submitting a issue or pull request! This prototype is still in its infancy, so we're looking for contributors to act as content curators, which help to manage what's in the repository. In the case of legacy course materials, curators should have taken the course before.

## Repository Structure
As the repository grows, optimizing its structure lets people find what they want easily. An example would be:
```
/Courses
	/10.001 Advanced Math I
		/Summer 2017
		/Projects
		...
	...
	/50.002 Computation Structures
		/Fall 2017
		/Projects
		...
	...
/Personal Projects
	/I Made A Thing
		/src
		...
	/memes
		/2018
			is_this_loss.jpg
			...
		...		
```
File naming should be consistent across the repository. In general, stuff should be organized and easy to find:
* Courses with their code and canonical name, e.g. `10.001 Advanced Math I`
* Lecture slides should have the week number and a descriptive filename, e.g. `Week 10 - James Scott - Commentary on Jacob's work.pdf`
* Subdirectories as needed, e.g. `/Additional Readings` or `/src`
