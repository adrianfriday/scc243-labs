# Part 1: Setting up your version controlled repo!

This is an *absolute essential*.  Submission of all work, and evidence of your achievement, will be through a 'portfolio submission' via SCC's gitlab instance `https://scc-source.lancs.ac.uk` (*this will be private to you, so you must invite '`@friday`' as a collaborator*).

To set this up, go to `https://scc-source.lancs.ac.uk` and *login to create an account if you don't already have one*.

* Read about [the basics of version control](https://about.gitlab.com/topics/version-control/)
* You may find [this step by step tutorial also useful](https://www.zdnet.com/article/how-to-get-started-with-git-on-linux/), if you haven't used git from the Linux terminal before

Essentially, the idea is that you 'check out' (normally) the latest version of a project from the server to your local machine.  Work on the content (mainly **markdown** text files ending in '`.md`' in this case).  **Add the new files** and **Commit** your changes (with a helpful message explaining what you've done is a key thing).  Then **push** a copy of your repo to the server with '`git push`'.

The great thing is, there's a backed up version of not just your work, but each important step leading up to where you are now.  *This will be important for the overall assessment of your work.*

It'll take a while to 'get comfy' with how this works in practice.  Although I think this is important general learning (to use git from the terminal).  You might find it easier to use [the built in git client in vscode](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git).

Repos can generally be public or private.  You can invite collaborators to either.  **We'd ask that all your coursework remains private to avoid unwanted code sharing.**

**Create a repo** and **clone it** to your file system.  [Download my template](https://scc-source.lancs.ac.uk/friday/scc243-labs/-/archive/main/scc243-labs-main.zip) (ZIP), expand it, and copy the files and weekly subfolders into your folder you've 'cloned' from the server.  *You should have a structure where there is a folder for each week's lab that's committed and pushed to your scc-source account by the end of this lab.*

> i.e. Your repo in this case **should be private**.

## A word on security

* You must use either HTTPS or SSH based URLs for securely pushing/pulling your code.  HTTPS is easier, since SSH would require that you [generate a public/private key pair](https://docs.gitlab.com/ee/user/ssh.html) then upload your public key to gitlab as part of your profile.
* It's easier to [generate a 'personal access token'](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).  You will need your token to have both `read_repository` and `write_repository` access rights.

You use a personal access token instead of a password.  *You'll want to keep this somewhere safe for future use, as once created you can't see it again.  **Don't share it with anyone!***

The good news is VS Code will remember your credentials for you.  The git password cache will enable the password to be remembered from the terminal so you don't have to enter your password or token every time you push/pull from the remote repo (`git config --global credential.helper cache`) from the shell.

## More version control
1. [generate a public/private key pair](https://docs.gitlab.com/ee/user/ssh.html) then upload your public key to gitlab as part of your profile
2. Ensure you understand how to use the `SSH` URIs (that start with `git@` instead of `HTTPS`) with your key pair for cloning and pushing your repos from/to your gitlab repo.