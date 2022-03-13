## 1. 파이썬 가상환경 세팅



- ### 가상환경 생성

python 3.3 이상의 버전 부터는 venv 모듈을 내장하고 있으므로 따로 설치없이 가능하다.

터미널을 열어 자신이 개발하려는 workspace 폴더에 가서 아래 명령어를 입력하자.

```bash
python3 -m venv venv-tutorial
```

venv-tutorial은 가상환경 이름이므로 자유롭게 쓰면 된다.

해당 구문을 실행하면 venv-tutorial 이름을 가진 가상 환경 폴더가 생성된다.

- ### 가상환경 실행

생성을 했으면 해당 가상환경을 실행해야한다.

실행 소스 파일은 가상 환경 폴더 안의 bin폴더 안에 있다.

```bash
source venv-tutorial/bin/activate
```

source 명령어를 통해 activate파일을 실행시켜 가상환경에 진입한다.

terminal 앞쪽에 (venv-tutorial)같이 가상환경의 이름이 붙으면 진입에 성공한 것이다.

pip list 명령어를 통해 설치된 패키지 버전들을 확인해보면 pip와 setuptools빼고는 아무것도 설치가 안된 깨끗한 상태임을 확인할 수 있다

***python3로 가상환경을 만들고 진입했으면 pip3 대신 pip명령어를 사용해도 된다.\***

- ### 가상환경 종료

가상환경을 종료하려면 deactivate 명령어를 사용하면 된다.

```bash
deactivate
```

터미널 앞에 가상환경 이름이 사라지면 정상적으로 종료된 것이다.
![img](https://media.vlpt.us/images/kyle13/post/a4d93de4-700a-41b4-ba2f-2fcad14aea7f/1.png)

------

- ### 패키지 설치, 관리를 쉽게해보자 [pip freeze]

가상 환경은 좋긴하지만 환경을 만들때마다 매번 호환되는 패키지를 버전대로 설치하는 것은 굉장히 귀찮은 일이다.

pip에선 설치된 패키지를 정리하고 설치하는 루틴을 제공하는데 아래와 같이 사용해보자

먼저 위에 가상환경 설치 과정을 이용해서 envA와 envB 가상환경 2개를 만들어보자

envA에 설치된 패키지를 그대로 리스트업해서 envB에 옮기는 과정을 진행해보자

가상환경 생성후 envA에 진입한다.

```bash
python3 -m venv envA
python3 -m venv envB
source envA/bin/activate
```

실험을 위해 matplotlib 패키지를 하나 설치한 후 리스트를 확인해보자

```bash
pip install matlplitlib
pip list
```

![img](https://media.vlpt.us/images/kyle13/post/68ac2f73-d921-4a9a-97d8-96a040478f98/2.png)

위와 같은 패키지들이 설치되었는데 이 패키지들을 리스트업 해보자

```bash
pip freeze > requirements.txt
```

해당 명령어를 실행하면 실행한 위치에 requirements.txt가 생성된 것을 확인할 수 있다. (requirements.txt 파일명은 컨벤션이니 되도록 맞출것)

![img](https://media.vlpt.us/images/kyle13/post/2aeeee79-1fd5-4142-8a47-305fe92a1c51/3.png)

requirements.txt 안에 위와 같이 리스트업 된 것을 볼 수 있다.

이제 envB 가상환경에 진입해서 해당 파일을 install 하면 리스트의 패키지를 모두 설치한다.

```bash
pip install -r ./envA/requirements.txt
```

[설치 완료된 모습]

![img](https://media.vlpt.us/images/kyle13/post/2e118801-73f8-4af1-86f0-edc2c63c9c88/4.png)

- ### 프로젝트 가상환경 세팅

~~~python
D:\Python\workspace>pip install virtualenv
D:\Python\workspace>virtualenv myenv
D:\Python\workspace\myenv\Scripts>activate.bat
(myenv) D:\Python\workspace\myenv\Scripts>pip install django
(myenv) D:\Python\workspace\myenv\Scripts>py -m django --version
4.0.3
(myenv) D:\Python\workspace\myenv\Scripts>python
Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> print(django.get_version())
4.0.3
~~~

Django_install_guide :  <https://docs.djangoproject.com/en/4.0/intro/install/>



## 2. 프로젝트 생성, app 생성, 서버 구동, django cycle

```
(myenv) D:\Python\workspace>django-admin startproject mysite
(myenv) D:\Python\workspace\mysite>py manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
March 13, 2022 - 18:20:17
Django version 4.0.3, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

```

[tornado response request cycle in Django](https://i.stack.imgur.com/rLfSC.jpg)

![img](https://i.stack.imgur.com/rLfSC.jpg)

![scr1](readme.assets/scr1.png)



- mysite/urls.py

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

- polls/urls.py

```
rom django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

- polls/views.py

```
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

- Client(Browser)

![scr2](readme.assets/scr2.png)

Django_install_guide : https://docs.djangoproject.com/en/4.0/intro/tutorial01/



### 3. git 설치, git 사용법, github 사용법

