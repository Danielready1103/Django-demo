[1] 安裝django
pip install django==5.0

[2] 建立專案
- django-admin startproject todolist .

[3] 啟動Server
- python manage.py runserver

[4] 資料庫同步
- python manage.py makemigrations
- python manage.py migrate

[5] 建立超級使用者
- python manage.py createsuperuser

[6] 新增功能
- python manage.py startapp user
	- settings.py
		- install apps
		- "user.apps.UserConfig",

[7] 新增獨立的templates　
- user/templates/user
