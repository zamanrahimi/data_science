import subprocess as sb 
import glob 

commit_msg = "this is a test commit1" 
sb.run("git add .", shell=True)
sb.run('git commit -m "{}"'.format(commit_msg), shell=True)
sb.run("git push", shell=True)
