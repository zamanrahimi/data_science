import subprocess as sb 
import coding 

sb.run("git add .", shell=True)
sb.run('git commit -m "{}"'.format(coding.commit_msg), shell=True)
sb.run("git push", shell=True)
