import os,sys,shutil
import svn.local
import re
import datetime

# 源码目录
Root_Dir = "/opt/"
# 已编译包的存放目录
Dest_Dir = "/data/packages/"
# war包目录，临时
War_Dir = "/opt/game-of-life/gameoflife-web/target/"

class Py_Maven(object):

    def __init__(self,projectName):
        self.projectName = projectName
        self.s_dir = Root_Dir + self.projectName

        # 日志文件
        self.Compile_Log = projectName + "-compile.log"
        self.Package_Log = projectName + "-package.log"
        self.Clean_Log = projectName + "-clean.log"

    # SVN 提交记录
    def svnlog(self):
        os.chdir(self.s_dir)
        r = svn.local.LocalClient('.')
        info = r.info()
        date = info['commit_date']
        commit_date = date + datetime.timedelta(hours=8)
        date = str(commit_date)
        positon = date.rfind(".")
        date = date[:positon]
        info['commit_date'] = date
        message = r.log_default(limit=1)
        for i in message:
            data = str(i)
            # pattern = re.compile(r"^.*date=(.*), msg='(.*)', revision=(\d+), author='(\w+)'.*")
            pattern = re.compile(r"^.*msg='(.*)', revision.*$")
            m = pattern.match(data)
            info['commit_msg'] = m.group(1)
        return info


    # 检验Maven编译日志
    def checklog(self,func,logfile):
        r = os.system("/bin/grep -q 'BUILD SUCCESS' " + logfile)
        if not r:
            print("Check mvn " + func + " success.")
        else:
            print("Check mvn " + func + " failed.")
            sys.exit()

    # 清理
    def clean(self):
        os.chdir(self.s_dir)
        os.system("/usr/bin/mvn clean > " + self.Clean_Log)
        self.checklog("clean",self.Clean_Log)

    # 编译
    def compile(self):
        os.chdir(self.s_dir)
        os.system("/usr/bin/mvn clean compile > " + self.Compile_Log)
        self.checklog("compile", self.Compile_Log)

    # 打包
    def package(self):
        os.chdir(self.s_dir)
        os.system("/usr/bin/mvn clean package > " + self.Package_Log)
        self.checklog("package", self.Package_Log)

    # 解压缩
    def uncompress(self,pkgname):
        file = War_Dir + pkgname
        # print(file)
        if os.path.isfile(file):
            shutil.copy(file,Dest_Dir)
            os.chdir(Dest_Dir)
            position = pkgname.rfind(".")
            sName = pkgname[:position]
            if os.path.isdir(sName):
                shutil.rmtree(sName)
            os.system("/usr/bin/unzip -q " + pkgname + " -d " + sName)
            print("uncompress finished.")
        else:
            print("[%s] is not exist or a directory."% pkgname)

    # 代码比对及覆盖
    def deploy(self,srcName,destName):
        src_File_List = []
        dest_File_List = []

        # Source Dir
        os.chdir(srcName)
        for foldername, subfolders, filenames in os.walk("."):
            for filename in filenames:
                src_File_List.append(foldername + '/' + filename)

        # Dest Dir
        os.chdir(destName)
        for foldername,subfolders,filenames in os.walk("."):
            for filename in filenames:
                dest_File_List.append(foldername + '/' + filename)

        for file in dest_File_List:
            if file not in src_File_List and os.path.isfile(file):
                os.unlink(file)

        # 覆盖代码
        destDir = re.match(r"(^/.*/)\w+[/]?$",destName).group(1)
        cmd = "\cp -r "+srcName+ " "+destDir
        os.system(cmd)
        print("Compare finish.")


def main():
    p = Py_Maven("game-of-life")
    # p.clean()
    # p.compile()
    # p.package()
    # p.uncompress("gameoflife.war")
    p.svnlog()
    # p.deploy("/data/packages/gameoflife/","/test/data/gameoflife")


if __name__ == '__main__':
    main()



