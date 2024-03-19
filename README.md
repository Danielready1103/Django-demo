[1] pip install pipenv

[2] pipenv shell

[3] pip install django

[4] django-admin createproject todolist .

[5] todolist /settings.py
		        /urls.py

[6] 開啟專案
python manage.py runserver
- db.sqlite3

[7] python manage.py createsuperuser

[8] python manage.py migrate

[9] python startapp app 

[10] 基本語法
def index(request):
    text = "<h1>Hello Django!</h1>"
    return HttpResponse(text)

def get_stocks(request):
    data = json.dumps(stocks, ensure_ascii=False)
    return HttpResponse(data)

[11] 放入網頁url
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("stocks/", views.get_stocks),
]

[12]templates
	- settings.py 設定

def get_stocks(request):
    return render(request, "index.html", {"stocks": stocks})

只能用stock.分類

<body>
  <h1>股市行情</h1>
  {% for stock in stocks %}
  <li>
    {{stock.分類}}-{{stock.指數}}
  </li>
  {% endfor %}
</body>

[13]
python manage.py startapp user
- settings 
	- todolist.user

[14]樣板套用
{% block naming %}
{% endblock%}

[15] 使用POST，要記得帶上TOKEN
{% csrf_token %}
