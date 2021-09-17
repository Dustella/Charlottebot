@echo on
docker build . -t registry.cn-shanghai.aliyuncs.com/qbot/cbot
docker push registry.cn-shanghai.aliyuncs.com/qbot/cbot
pause