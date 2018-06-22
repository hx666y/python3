#!/bin/bash
#/usr/bin/curl -u 账户:密码  -XGET   "http://172.16.30.9:9200/_snapshot/my_backup/syslog-$(date -d '-1days' +'%Y.%m.%d')"
/usr/bin/curl -H "Content-Type: application/json"  -u 账户:密码  -XPUT  'http://172.16.30.9:9200/_snapshot/my_backup/'huilc-$(date -d '-1days' +'%Y.%m.%d')'' -d '{"indices": "huilc-*-'$(date -d '-1days' +'%Y.%m.%d')'"}'
/usr/bin/curl -H "Content-Type: application/json"  -u 账户:密码  -XPUT  'http://172.16.30.9:9200/_snapshot/my_backup/'syslog-$(date -d '-1days' +'%Y.%m.%d')'' -d '{"indices": "syslog-*-'$(date -d '-1days' +'%Y.%m.%d')'"}'
/usr/bin/curl -H "Content-Type: application/json"  -u 账户:密码  -XPUT  'http://172.16.30.9:9200/_snapshot/my_backup/'toback-$(date -d '-1days' +'%Y.%m.%d')'' -d '{"indices": "toback-*-'$(date -d '-1days' +'%Y.%m.%d')'"}'
/usr/bin/curl -H "Content-Type: application/json"  -u 账户:密码  -XPUT  'http://172.16.30.9:9200/_snapshot/my_backup/'nginx-$(date -d '-1days' +'%Y.%m.%d')'' -d '{"indices": "nginx-*-'$(date -d '-1days' +'%Y.%m.%d')'"}'
/usr/bin/curl -H "Content-Type: application/json"  -u 账户:密码  -XPUT  'http://172.16.30.9:9200/_snapshot/my_backup/'hlej-$(date -d '-1days' +'%Y.%m.%d')'' -d '{"indices": "hlej-*-'$(date -d '-1days' +'%Y.%m.%d')'"}'
/usr/bin/curl -H "Content-Type: application/json"  -u 账户:密码  -XPUT  'http://172.16.30.9:9200/_snapshot/my_backup/'user-$(date -d '-1days' +'%Y.%m.%d')'' -d '{"indices": "user-*-'$(date -d '-1days' +'%Y.%m.%d')'"}'
/usr/bin/curl -u 账户:密码  -XPOST  "http://172.16.30.9:9200/*-$(date -d '-5days' +'%Y.%m.%d')/_close"
/usr/bin/curl -u 账户:密码   -XDELETE "http://172.16.30.9:9200/*-$(date -d '-15days' +'%Y.%m.%d')/"
/usr/bin/curl -u 账户:密码  -XDELETE   "http://172.16.30.9:9200/_snapshot/my_backup/hlej-$(date -d '-180days' +'%Y.%m.%d')"
/usr/bin/curl -u 账户:密码  -XDELETE   "http://172.16.30.9:9200/_snapshot/my_backup/huilc-$(date -d '-720days' +'%Y.%m.%d')"
/usr/bin/curl -u 账户:密码  -XDELETE   "http://172.16.30.9:9200/_snapshot/my_backup/syslog-$(date -d '-720days' +'%Y.%m.%d')"
/usr/bin/curl -u 账户:密码  -XDELETE   "http://172.16.30.9:9200/_snapshot/my_backup/toback-$(date -d '-720days' +'%Y.%m.%d')"
/usr/bin/curl -u 账户:密码  -XDELETE   "http://172.16.30.9:9200/_snapshot/my_backup/nginx-$(date -d '-180days' +'%Y.%m.%d')"

