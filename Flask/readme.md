激活虚拟环境：

```powershell
 venv\Scripts\activate
```

启动服务器，如果主脚本为app.py，则直接进行第二步。

```powershell
set FLASK_APP=iron-notes_flask
flask run
```

服务器记录：

查询：Get请求。

与数据库有交互：Post请求。

安装库：

```powershel
pip install mysql-connector-python
```