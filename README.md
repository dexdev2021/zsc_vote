# zsc_vote

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


# api部署

数据库文件 api/vote.sql
```
pip install flask
pip install pymysql
pip install flask-mysql
pip install requests
pip install apscheduler

cd api
nohup python app.py &
nohup python zsc_rpc.py &
```
推荐使用supervisorctl管理进程
