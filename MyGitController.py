import os
import sys
import time

com3 = os.listdir()
python_files = []
project_names = []

for i in com3:
    if "." in i:
        python_files.append(i)
    else:
        project_names.append(i)

print(com3)

def track_status(project_path):
    print('Git status information: ', os.system('''CD {0} && git status'''.format(project_path)))

initGit = ''
workFile = ''
trackFile = ''
commitGit = ''

for pro in project_names:
    com4 = os.listdir(pro)
    if '{}.txt'.format(pro) not in com4:
        os.system('''CD {0} && git init'''.format(pro))
        initGit = ('IMPORTANT: Initializing git repository: ' + str(pro))
        with open('{0}\\{1}.txt'.format(pro, pro), 'w') as cr:
            cr.close()

    os.system('''CD {0} && git add .'''.format(pro))
    trackFile = 'Tracked files: ' + str(com4)
    commit_time = str(time.strftime('%Y.%m.%d_%H:%M'))
    my_commit = '''git commit -m "Commit {} "'''.format(commit_time)
    os.system('''CD {0} && {1}'''.format(pro, my_commit))
    commitGit = 'Commitment: {}'.format(my_commit)
    track_status(pro)
    with open('{0}\\{1}.txt'.format(pro, pro), 'a') as mf:
        mf.writelines(initGit + '\n' + workFile + '\n' + trackFile + '\n' + commitGit + '\n')
    print(os.system('CD {} && git diff'.format(pro)))
    os.system('CD {0} && git remote add origin https://github.com/azikoDron/{1}.git && git push -u origin master'.format(pro, pro))
    print('\n') # Fix me


