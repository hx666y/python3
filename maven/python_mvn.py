import os,sys,shutil
import svn.local
import re
import datetime

class Py_Maven(object):

    def __init__(self,Src_Project,Dest_Project,War_Path):

        # 项目名
        self.projectName = os.path.basename(Src_Project)
        self.s_dir = Src_Project

        self.Dest_Project = Dest_Project
        self.Dest_Dir = os.path.dirname(Dest_Project)
        self.pkgDir = os.path.basename(Dest_Project)

        # war包绝对路径
        self.War_Pkg = Src_Project + "/" + War_Path
        self.pkgName = os.path.basename(self.War_Pkg)

        # 日志文件
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.Compile_Log = self.projectName + "-" + date + "-compile.log"
        self.Package_Log = self.projectName + "-" + date + "-package.log"
        self.Clean_Log = self.projectName + "-" + date + "-clean.log"


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
            #pattern = re.compile(r"^.*date=(.*), msg='(.*)', revision=(\d+), author='(\w+)'.*")
            pattern = re.compile(r"^.*msg='(.*)', revision.*$")
            m = pattern.match(data)
            info['commit_msg'] = m.group(1)
        return info


    # 检验Maven编译日志
    def checklog(self,func,logfile):
        r = os.system("tail %s | grep -q 'BUILD SUCCESS' " %logfile)
        if not r:
            print("Check mvn " + func + " success.")
        else:
            print("Check mvn " + func + " failed.")
            sys.exit()

    # 清理
    def clean(self):
        os.chdir(self.s_dir)
        os.system("/usr/bin/mvn clean >> " + self.Clean_Log)
        self.checklog("clean",self.Clean_Log)

    # 编译
    def compile(self):
        os.chdir(self.s_dir)
        os.system("/usr/bin/mvn clean compile >> " + self.Compile_Log)
        self.checklog("compile", self.Compile_Log)

    # 打包
    def package(self):
        os.chdir(self.s_dir)
        os.system("/usr/bin/mvn clean package >> " + self.Package_Log)
        self.checklog("package", self.Package_Log)

        # 检查打包之后的文件是否存在
        if os.path.isfile(self.War_Pkg):
            print("Confirm "+self.pkgName+" is exist, build finished.")
        else:
            print(self.pkgName+" not found, error.")
            sys.exit()

    # 解压缩
    def uncompress(self):
        pkgname = os.path.basename(self.War_Pkg)
        sName = self.pkgDir
        shutil.copy(self.War_Pkg,self.Dest_Dir)
        os.chdir(self.Dest_Dir)
        if os.path.isdir(sName):
            shutil.rmtree(sName)
        os.system("/usr/bin/unzip -q " + pkgname + " -d " + sName)
        print("uncompress finished.")

    # 代码比对及覆盖
    def deploy(self,destName,destSvnUrl):
        srcName = self.Dest_Project
        src_File_List = []
        dest_File_List = []

        src_Dir_List = []
        dest_Dir_List = []

        ops = "--username SvnUpdateU --password sdbqWt2711An --no-auth-cache"
        # 判断SVN目录是否存在
        if not os.path.isdir(destName):
            os.system("svn checkout %s %s %s"%(destSvnUrl,destName,ops))
        else:
            pass

        # Source Dir
        os.chdir(srcName)
        for foldername, subfolders, filenames in os.walk("."):
            if ".svn" in foldername:
                continue
            else:
                src_Dir_List.append(foldername)
                for filename in filenames:
                    src_File_List.append(foldername + '/' + filename)

        # Dest Dir
        os.chdir(destName)
        for foldername,subfolders,filenames in os.walk("."):
            if ".svn" in foldername:
                continue
            else:
                dest_Dir_List.append(foldername)
                for filename in filenames:
                    dest_File_List.append(foldername + '/' + filename)

        # 删除多余代码
        for file in dest_File_List:
            if file not in src_File_List and os.path.isfile(file):
                os.system("svn delete %s %s"%(file,ops))
        for dir in dest_Dir_List:
            if dir not in src_Dir_List and os.path.isdir(dir):
                os.system("svn delete %s %s"%(dir,ops))


        # 覆盖代码
        # destDir = re.match(r"(^/.*/)\w+[/]?$",destName).group(1)
        os.chdir(srcName)
        os.system("cp -rf * " + destName)

        info = self.svnlog()
        revision = info['commit_revision']

        # 新增代码
        os.chdir(destName)
        for dir in src_Dir_List:
            if dir not in dest_Dir_List:
                os.system("svn add --non-recursive %s %s"%(dir,ops))
        for file in src_File_List:
            if file not in dest_File_List:
                os.system("svn add %s %s"%(file,ops))
        # svn 提交
        os.system("svn commit -m '开发版本%s初始化' %s"%(str(revision),ops))
        print("Compare finish.")


def main():
    p = Py_Maven("/opt/game-of-life","/data/packages/gameoflife","gameoflife-web/target/gameoflife.war")
    p.clean()
    p.compile()
    p.package()
    p.uncompress()
    p.svnlog()
    p.deploy("/test/data/gameoflife","svn://10.10.1.105/aaa")


if __name__ == '__main__':
    main()



