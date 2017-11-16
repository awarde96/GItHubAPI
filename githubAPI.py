from github import Github
import getpass

#g = Github("user", "password")
username = raw_input("Github Username:")
pw = getpass.getpass()
g = Github(username,pw)

for repo in g.get_user().get_repos():
    print repo.name

print g.get_last_api_status_message()
