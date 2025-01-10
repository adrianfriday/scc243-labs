# Part 1: Setting up your version controlled repo!

This is an *absolute essential*.  Submission of all work, and evidence of your achievement, will be through a 'portfolio submission' via `github.com` (*the link to which must be submitted via the course moodle page*).

To set this up, go to `github.com` and *create an account if you don't already have one*.

* Read about [the basics of version control](https://about.gitlab.com/topics/version-control/)

Essentially, the idea is that you 'check out' (normally) the latest version of a project.  Work on the content (mainly markdown text files ending in '`.md`' in this case).  Commit your changes (with a helpful message explaining what you've done is the key thing).  Then push a copy onto the server with `git push`.

The great thing is, there's a backed up version of not just your work, but each important step leading up to where you are now.

It'll take a while to 'get comfy' with how this works in practice.

Repos can be public or private.  You can invite collaborators to either.  **We'd ask that all your coursework remains private to avoid unwanted code sharing.**

> Your repo in this case **should be private**.

## A word on security

**  You must use either HTTPS or SSH based URLs for securely pushing/pulling your code.  HTTPS is easier, since SSH would require that you [generate a public/private key pair](https://docs.gitlab.com/ee/user/ssh.html) then upload your public key to github as part of your profile.  It's easier to [generate a 'personal access token'](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).  You will need your token to have both `read_repository` and `write_repository` access rights.

You can use a personal access token instead of a password.  *You'll want to keep this somewhere safe for future use.  **Don't share it with anyone!***

The good news is VS Code will remember your credentials for you.  Or enable the git password cache so you don't have to enter your password or token every time you push/pull from the remote repo (`git config --global credential.helper cache`) from the shell.


## More version control
1. [generate a public/private key pair](https://docs.gitlab.com/ee/user/ssh.html) then upload your public key to github as part of your profile
2. Ensure you understand how to use the `SSH` URIs (that start with `git@` instead of `HTTPS`) with your key pair for cloning and pushing your repos from/to your github repo.