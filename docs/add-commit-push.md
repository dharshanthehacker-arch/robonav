# Git: Add, Commit and Push

This document explains the three commands used to get work from my laptop into the RoboNav repository on GitHub, and how they differ. I used all three throughout this project.

## git add: select what goes into the next snapshot

`git add` moves changes from the working directory into the **staging area**. It does not save anything permanently. It only marks which changes I want in the next commit.

Example from this project:

    git add src/robot.py

Before this, `git status` showed `src/robot.py` as untracked (red). After it, the file appeared under "Changes to be committed" (green). The staging area lets me commit related changes together and leave unfinished work out.

## git commit: save a snapshot to local history

`git commit` takes everything in the staging area and records it as a permanent snapshot in my **local** repository, with a message and a unique hash.

Example:

    git commit -m "Add Robot class with basic movement"

This created commit `0a95ea9`. The snapshot exists only on my computer. If I lost my laptop at this point, the work would be lost, and nobody else could see it.

## git push: send local commits to GitHub

`git push` uploads my local commits to the **remote** repository on GitHub, so the history is backed up and visible to others, including my lecturer.

Example:

    git push

The first push of a new branch needed `-u` to link it to the remote:

    git push -u origin feature/diagonal-moves

## The differences

| Command | What it affects | Where the change lives |
|---|---|---|
| `git add` | Selects changes for the next commit | Staging area (local) |
| `git commit` | Records the staged changes as a snapshot | Local repository |
| `git push` | Uploads local commits | Remote repository (GitHub) |

The three steps always go in this order: add, then commit, then push. Splitting them gives me control. I choose exactly what each commit contains (add), I save checkpoints with a clear message while working offline (commit), and I share them only when ready (push).

## Related commands I used

- `git status` shows what is untracked, staged or committed.
- `git diff` shows the exact line changes before I add them.
- `git log --oneline` shows the commit history.
- `git checkout -b feature/diagonal-moves` created a branch so I could build a feature without touching `main`.
- `git merge` brought the finished feature back into `main`.
- `git clone` copied the whole repository from GitHub into a fresh folder.

## Evidence from this project

The history of the RoboNav repository shows the workflow in practice: nine commits, each made with add, commit and push, plus one feature branch that was merged into `main`.
