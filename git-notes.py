'''config (~/.ssh/config)

# Default account (tendercuts account)
Host github.com
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_rsa_tendercuts

# Personal account
Host github-personal
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_rsa

'''

For using personal github account do following changes

- while adding git remote origin change git@github-personal
example:
	git remote add origin git@github-personal:uttampatel007/git-ssh-notes.git 


- change username and email for that repo (as global is set for default account)
example:
	git config user.email "uttam11.velani11@gmail.com"
	git config user.username "uttampatel007"
	git config user.name "Uttam Patel"


