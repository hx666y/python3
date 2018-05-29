import os,requests,sys

# Base Var
tomcat_ver = '7.0.79'
jdk_ver = '8u111'
source = '10.10.1.223'

if len(sys.argv) < 2:
    print("project no input")
    sys.exit()
else:
    Project = sys.argv[1]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, 'soft')
if not os.path.isdir(DOWNLOAD_DIR):
    os.mkdir(DOWNLOAD_DIR)
else:
    os.chdir(DOWNLOAD_DIR)


def downloadfile(fileurl):
    filename = fileurl.split('/')[-1]
    s_path = os.path.join(DOWNLOAD_DIR,filename)
    if not os.path.exists(s_path):
        r = requests.get(fileurl)
        with open(s_path, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)
            #f.write(r.content)
            print('DownLoad ' + filename + ' Success.')
    else:
        print(filename + ' Already Exists. Skip...')

# 下载JDK和Tomcat安装包
print("Starting download file JDK...")
downloadfile('http://' + source + '/soft/jdk/jdk-' + jdk_ver + '-linux-x64.rpm')
print("Starting download file tomcat...")
downloadfile('http://' + source + '/soft/tomcat/apache-tomcat-' + tomcat_ver + '.tar.gz')

# 安装JDK
print("Starting Install JDK...")
#install_jdk_cmd = 'rpm -ivh jdk-' + jdk_ver + '-linux-x64.rpm'
os.system('rpm -ivh jdk-' + jdk_ver + '-linux-x64.rpm')
print("Install JDK ok...")

# 安装Tomcat
print("Starting Install Tomcat... ")
print("Step1: Add tomcat user.")
os.system('/usr/sbin/groupadd tomcat')
os.system('/usr/sbin/useradd -s /bin/bash -g tomcat tomcat')
print("Step2: Decompression Packet.")
os.system('tar -zxf apache-tomcat-' + tomcat_ver + '.tar.gz')
os.system('mv apache-tomcat-' + tomcat_ver + ' /usr/local/' + Project)
downloadfile('http://' + source + '/soft/tomcat/tomcat')
# 修改脚本路径
data = ''
with open('tomcat', 'r+') as file:
    for line in file.readlines():
        if 'CATALINA_HOME="/usr/local/tomcat"' in line:
            line = line.replace('CATALINA_HOME="/usr/local/tomcat"', 'CATALINA_HOME="/usr/local/' + Project + '"')
        elif 'Project="tomcat"' in line:
            line = line.replace('Project="tomcat"', 'Project="' + Project + '"')
        data += line
with open('tomcat', 'r+') as f:
    f.writelines(data)

os.system('\mv tomcat /etc/init.d/' + Project)
os.system('chmod 755 /etc/init.d/' + Project)
print("Finished Install Tomcat...")



