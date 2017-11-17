from github import Github
import getpass

#g = Github("user", "password")
username = raw_input("Github Username:")
pw = getpass.getpass()
g = Github(username,pw)

for repo in g.get_user().get_repos():
    print repo.name
    #for commit in repo.get_commits():
        #print commit
    for collaborators in repo.get_collaborators():
        print collaborators
    for languages in repo.get_languages():
       print languages

email = raw_input("Email:")
print g.legacy_search_user_by_email(email)

print g.get_last_api_status_message()
