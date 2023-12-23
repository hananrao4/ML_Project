crosoft Windows [Version 10.0.22621.2861]
(c) Microsoft Corporation. All rights reserved.

D:\ML_Project>"C:/Users/Rao Hanan Akram/anaconda3/Scripts/activate"        

(base) D:\ML_Project>conda activate base

(base) D:\ML_Project>conda activate venv/

(D:\ML_Project\venv) D:\ML_Project>dvc add artifacts/raw.csv
100% Adding...|██████████████████████████████████|1/1 [00:00,  8.20file/s]

To track the changes with git, run:

        git add 'artifacts\raw.csv.dvc'

To enable auto staging, run:

        dvc config core.autostage true

(D:\ML_Project\venv) D:\ML_Project>git add artifacts/raw.csv.dvc           

(D:\ML_Project\venv) D:\ML_Project>git coommit -m "addition one record"
git: 'coommit' is not a git command. See 'git --help'.

The most similar command is
        commit

(D:\ML_Project\venv) D:\ML_Project>git commit -m "addition one record"  
[main 0a8a9e1] addition one record
 1 file changed, 2 insertions(+), 2 deletions(-)

(D:\ML_Project\venv) D:\ML_Project>git push origin main
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 423 bytes | 423.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.       
To https://github.com/hananrao4/ML_Project.git
   6480b07..0a8a9e1  main -> main

(D:\ML_Project\venv) D:\ML_Project>git checkout 6480b075f2c5989f0f7d533916dbcb56660087e6
Note: switching to '6480b075f2c5989f0f7d533916dbcb56660087e6'.

You are in 'detached HEAD' state. You can look around, make experimental   
changes and commit them, and you can discard any commits you make in this  
state without impacting any branches by switching back to a branch.        

If you want to create a new branch to retain commits you create, you may   
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 6480b07 chnages in data

(D:\ML_Project\venv) D:\ML_Project>dvc checkout
Building workspace index                        |2.00 [00:00, 48.4entry/s] 
Comparing indexes                               |3.00 [00:00,  558entry/s] 
Applying changes                                |1.00 [00:00,   114file/s] 
M       artifacts\raw.csv

(D:\ML_Project\venv) D:\ML_Project>