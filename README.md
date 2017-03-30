# SentimentAnalyzer

Alexis was here.



#### How To Contribute

- First step is to clone this repo onto local machine
- git clone https://github.com/acandelaria1/SentimentAnalyzer.git

- If you type git branch on command line then you will see which branches
  you have locally and which branch you are currently on.

- To contribute, create a new branch that makes sense for the feature you are trying to add
- For this example you called type git checkout -b yourname-update-readme
- if you run git branch again you will notice that git will say that you are on this newly 
  created branch.

- Update Readme file now using any text editor you want.
- Once you have saved a change you can type git status to view all changed files

- Git requires you to add changed files to what is called a staging area, commit these staged
  changes, and then push them to a branch.

- To add your updated read me change type git add -A
  note: what this does is add ALL changed files.

- Type git status again to see the difference in what staged files look like.

- To commit, type git commit -m "Updated readme relevant message" and pass whatever message
  you want to describe the action you are taking. Making good commit descriptions will
  help you if you ever need to find the commit again.

- Type git status again to see what commited changes look like
- Now you can push them to the branch you just created with git push origin yourname-update-readme
- When this is successful you can view the repo on the github website and it will show you the newly
  pushed branch and give you the option to make a pull request off of this branch.
- When you select create pull request off this branch you can then type a description of the pull request 
  and on the side bar you will see options to add reviewers.
- Once someone eles approves the pull request you can merge the branch into master and you have successfully contributed.

- It is not over yet though: everyone else must continuously call git fetch, and git pull while on master to receive these latest updates.
