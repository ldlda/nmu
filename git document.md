# git usage

i will try to do manual as much as possible. it is harder

## current setup so far

```sh
cd nmu
git init
# add readme
git add .
git commit
git worktree add python # branch -c python but it adds a folder

git remote add origin git@localhost:lda/nmu.git 
# git.ldlda.com/lda/nmu.git but i cant get it to work
```

## as a guest

idfk what you do after clone: on github you should be doing issues and idk how pr would work, because gh is a push mirror.  
on [git.ldlda.com](https://git.ldlda.com) well it is invite only

```sh
git clone git@localhost:lda/nmu.git
cd nmu
git branch origin/python # next up is your own
```

## advice

note you should be committing literally **every time**

every time. you get this part right? you feel like some steps has been achieved? `git commit`.

spam it. i see 1608 commits i see big projects. 13 commits could get you there (if you are me) but i would be unimpressed.

dont do it like me. i would write a whole file before committing. got everything done flushed before committing. bad.

also commit messages should be descriptive. if you added function get_index add that in:  
`git commit -m "add get_index for Container"`

if you fixed get_index so it returns None on out bounds: commit.

do whatever: commit.

seasoned devs commit every changes.  
they do commit broken files. it does not pass their automated test actions.  
what do they do? they fix them then commit again, or they `git revert`. life is easy.

this will also be for your own sake working in the future. git bisect is going to hunt that bug down good.
