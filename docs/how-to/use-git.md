# How to use git

## Overview

Git is a distributed revision control system. In other words, it keeps a history of your code changes that you can share with other people.

## Basics

### Clone

### Stage

### Commit

### Push

## Branching models

### Work in the same repo

### Work in forks

## Topics

### Remotes

#### Setting up remotes

#### Tracking branches

### Small fixes

#### Amend

#### Fixup/autosquash

Display recent history

    git log --oneline

count down to find the commit to fix
let's say it's the 4th item, that's HEAD~3, where HEAD is the first item.

Commit the current staged changes with the fixup! flag to merge with the target commit.

    git commit --fixup=HEAD~3
    # or
    git commit --fixup :/<unique portion of shortlog msg>

You'll see the commit shortlog is the same as that of the target commit.

Stash any unsaved changes.

    git stash

Perform an interactive rebase with autosquash. Since it's the 4th item, and we just added another commit, we need to use HEAD~5 to reach the target commit.

    git -c sequence.editor=: rebase -i HEAD~5 --autosquash

The `-c sequence.editor=:` passes a configuration option to git to disable the editor.

##### References

    https://thoughtbot.com/blog/autosquashing-git-commits

#### Squashing commits

### Merging models

#### Merge

#### Rebase

#### Squash

#### Github merge annoyances

### Aliases

### Delete files from the remote

### Ignore files

- http://gitignore.io

### Conflicts

- Note: DO NOT commit new code inside conflict resolution commits

## Git References

- http://www-cs-students.stanford.edu/~blynn/gitmagic/
