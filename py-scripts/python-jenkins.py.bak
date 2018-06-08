import jenkins
import shutil
import time
import re
import os,sys

J_Workspace = "/root/.jenkins/workspace"
Dest_Dir = "/temp"

# f = "/opt/github/game-of-life/pom.xml"
# f_re = re.compile(r"\s+<(module)>(.*)</\1>")
#
# module_name = []
# f_read = open(f,'r')
#
# while True:
#     line = f_read.readline()
#     if re.match(f_re,line):
#        file =  re.match(f_re,line)
#        module_name.append(file.group(2))
#     elif len(line)==0:
#         break
# f_read.close()
# print(module_name)

class P_jenkins(object):
    def __init__(self,project):
        self.__host = "http://10.10.1.105:8080"
        self.__username = "admin"
        self.__password = "admin"
        self.project = project

    def __str__(self):
        msg = "编译项目" + self.project + "完成。"
        return msg

    def run(self):
        # 连接Jenkins
        server = jenkins.Jenkins(self.__host,username=self.__username,password=self.__password)
        print("连接Jenkins成功，开始构建...")

        #构建
        server.build_job(self.project)
        print("正在构建中...")
        time.sleep(60)

        # 获取最后次构建号
        last_build = server.get_job_info(self.project)['lastBuild']['number']
        print("构建完成。此次版本为:" + str(last_build))

        # 获取某次构建的执行结果状态
        status = server.get_build_info(self.project, last_build)['result']
        print(status)

        return status

    def deploy(self,module):
        packageName = os.path.join(J_Workspace,self.project,module,"target/")
        packageName += "gameoflife.war"
        # print(packageName)

        if packageName:
            shutil.copy(packageName, Dest_Dir)
            print("拷贝文件成功。")
        else:
            print("没有找到包。")


        #status == "SUCCESS"

def main():
    pro = P_jenkins("game-of-life")
    run_result = pro.run()

    if run_result == "SUCCESS":
        pro.deploy("gameoflife-web")
    else:
        print("编译没有成功，退出。")
        sys.exit(0)

    print(pro)

if __name__ == '__main__':
    main()














