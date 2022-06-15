# Steps for basics pull and push applications

'''
bash: /z//.bash_profile: Too many levels of symbolic links

tushar@FTPC74 MINGW64 /z
$ git --version
git version 2.36.0.windows.1

tushar@FTPC74 MINGW64 /z
$ mkdir basics-repo

tushar@FTPC74 MINGW64 /z
$ cd basics-repo

tushar@FTPC74 MINGW64 /z/basics-repo
$ git init
Initialized empty Git repository in //FTSRV/Home $/tushar/basics-repo/.git/

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ touch hello.py

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ gedit hello.py
bash: gedit: command not found

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git add hello.py
hint: core.useBuiltinFSMonitor will be deprecated soon; use core.fsmonitor instead
hint: Disable this message with "git config advice.useCoreFSMonitorConfig false"

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git status
hint: core.useBuiltinFSMonitor will be deprecated soon; use core.fsmonitor instead
hint: Disable this message with "git config advice.useCoreFSMonitorConfig false"
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   hello.py


tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git commit -m "First-Commit"
hint: core.useBuiltinFSMonitor will be deprecated soon; use core.fsmonitor instead
hint: Disable this message with "git config advice.useCoreFSMonitorConfig false"
[master (root-commit) 7d24702] First-Commit
 Committer: Tushar Jangid <tushar@FTDC.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+)
 create mode 100644 hello.py

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git remote add origin "git@github.com:rish5/Git-Tutorials-Devops.git"

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git pull origin master
hint: core.useBuiltinFSMonitor will be deprecated soon; use core.fsmonitor instead
hint: Disable this message with "git config advice.useCoreFSMonitorConfig false"
ssh: connect to host github.com port 22: Connection refused
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ ls
hello.py

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git pull origin master
hint: core.useBuiltinFSMonitor will be deprecated soon; use core.fsmonitor instead
hint: Disable this message with "git config advice.useCoreFSMonitorConfig false"
ssh: connect to host github.com port 22: Connection refused
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ ssh -T git@github.com
ssh: connect to host github.com port 22: Connection refused

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git config --local -e  # change the ssh link to http link for a connection of local with remote for push and pull request

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git pull origin master
hint: core.useBuiltinFSMonitor will be deprecated soon; use core.fsmonitor instead
hint: Disable this message with "git config advice.useCoreFSMonitorConfig false"
fatal: couldn't find remote ref master

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git pull origin main
hint: core.useBuiltinFSMonitor will be deprecated soon; use core.fsmonitor instead
hint: Disable this message with "git config advice.useCoreFSMonitorConfig false"
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 602 bytes | 14.00 KiB/s, done.
From https://github.com/rish5/Git-Tutorials-Devops
 * branch            main       -> FETCH_HEAD
 * [new branch]      main       -> origin/main
fatal: refusing to merge unrelated histories  # you need to merge unrelated history with following below command

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ ls
hello.py

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git pull origin main --allow-unrelated-histories
hint: core.useBuiltinFSMonitor will be deprecated soon; use core.fsmonitor instead
hint: Disable this message with "git config advice.useCoreFSMonitorConfig false"
From https://github.com/rish5/Git-Tutorials-Devops
 * branch            main       -> FETCH_HEAD
Merge made by the 'ort' strategy.
 README.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ ls
hello.py  README.md

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git push origin master --allow-unrelated-histories
error: unknown option `allow-unrelated-histories'
usage: git push [<options>] [<repository> [<refspec>...]]

    -v, --verbose         be more verbose
    -q, --quiet           be more quiet
    --repo <repository>   repository
    --all                 push all refs
    --mirror              mirror all refs
    -d, --delete          delete refs
    --tags                push tags (can't be used with --all or --mirror)
    -n, --dry-run         dry run
    --porcelain           machine-readable output
    -f, --force           force updates
    --force-with-lease[=<refname>:<expect>]
                          require old value of ref to be at this value
    --force-if-includes   require remote updates to be integrated locally
    --recurse-submodules (check|on-demand|no)
                          control recursive pushing of submodules
    --thin                use thin pack
    --receive-pack <receive-pack>
                          receive pack program
    --exec <receive-pack>
                          receive pack program
    -u, --set-upstream    set upstream for git pull/status
    --progress            force progress reporting
    --prune               prune locally removed refs
    --no-verify           bypass pre-push hook
    --follow-tags         push missing but relevant tags
    --signed[=(yes|no|if-asked)]
                          GPG sign the push
    --atomic              request atomic transaction on remote side
    -o, --push-option <server-specific>
                          option to transmit
    -4, --ipv4            use IPv4 addresses only
    -6, --ipv6            use IPv6 addresses only


tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git push origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/rish5/Git-Tutorials-Devops.git'

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git commit -m "initial commit"
hint: core.useBuiltinFSMonitor will be deprecated soon; use core.fsmonitor instead
hint: Disable this message with "git config advice.useCoreFSMonitorConfig false"
On branch master
nothing to commit, working tree clean

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git push origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/rish5/Git-Tutorials-Devops.git'

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git add -all
error: did you mean `--all` (with two dashes)?

tushar@FTPC74 MINGW64 /z/basics-repo (master)
$ git add --all
hint: core.useBuiltinFSMonitor will be deprecated soon; use core.fsmonitor instead
hint: Disable this message with "git config advice.useCoreFSMonitorConfig false"

tushar@FTPC74 MINGW64 /z/basics-repo (master) # you need to specify the branch where you need to commit
$ git push origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/rish5/Git-Tutorials-Devops.git'

tushar@FTPC74 MINGW64 /z/basics-repo (master)   # here you need to login and give access to the remote server for access of local server files
$ git push origin HEAD:main
info: please complete authentication in your browser...
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 554 bytes | 184.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/rish5/Git-Tutorials-Devops.git
   bc33be1..3fed94c  HEAD -> main


'''


print("Hello! Git World")