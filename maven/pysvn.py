import python_mvn
p = python_mvn.Py_Maven("/opt/game-of-life","/data/packages/gameoflife","gameoflife-web/target/gameoflife.war")
#info = p.svnlog()

p.clean()
p.compile()
p.package()
p.uncompress()
p.deploy("/test/data/gameoflife","svn://10.10.1.105/aaa")
#print(info['commit_revision'])
#print(info['commit_date'])
#print(info['commit_msg'])
#print(info['commit_author'])
