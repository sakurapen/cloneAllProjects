import requests
import git


class Progress(git.remote.RemoteProgress):
    @staticmethod
    def update(op_code, cur_count, max_count=None, message=''):
        print('update(%s, %s, %s, %s)' % (op_code, cur_count, max_count, message))


projects = requests.get(
    'https://gitlab.example.com/api/v4/projects',
    headers={'Authorization': 'Bearer your-user-token'}
)

for project in projects.json():
    # print(project)
    print('Start clone: ' + project["name"] + ', git url: ' + project["ssh_url_to_repo"])
    git.Repo.clone_from(
        project["ssh_url_to_repo"],
        project["name"],
        progress=Progress())
