import jenkins

# 连接Jenkins
server = jenkins.Jenkins('http://10.10.1.105:8080', username='admin', password='admin')
# user = server.get_whoami()
# version = server.get_version()
# print("Hello %s from Jenkins %s" % (user['fullName'], version))

# 创建Jenkins


# 删除job
#server.delete_job('gameoflife')

# 构建job（不带参数）
#server.build_job('game-of-life')

# 获取job的相关信息
info = server.get_job_info('game-of-life')

# 获取最后次构建号
last_build = server.get_job_info('game-of-life')['lastBuild']['number']

# 获取某次构建的执行结果状态
status = server.get_build_info('game-of-life',last_build)['result']
print(status)

# 判断job的某次构建是否还在构建中
result = server.get_build_info('game-of-life',last_build)['building']
print(result)


#build_info = server.get_build_info('game-of-life', last_build_number)
#print(build_info)