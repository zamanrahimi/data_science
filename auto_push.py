import subprocess as sb 
sb.run("git add .", shell=True)
sb.run("git commit -m 'test'", shell=True)
sb.run("git push", shell=True)


