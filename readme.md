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



## 2. Django Cycle, 프로젝트 생성, app 생성, 서버 구동

- ### Django Cycle

   [tornado response request cycle in Django](https://i.stack.imgur.com/rLfSC.jpg)

![img](https://i.stack.imgur.com/rLfSC.jpg)

## 

- ### 프로젝트 생성, app 생성, 서버 구동

```
(myenv) D:\Python\workspace>django-admin startproject mysite
(myenv) D:\Python\workspace>py manage.py startapp polls
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



![scr1](readme.assets/scr1.png)

file:mysite/ 디렉토리 밖은 프로젝트를 담는 공간입니다. 그 이름은 Django 와 아무 상관이 없으니, 원하는 이름으로 변경해도 됩니다.

`manage.py`: Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인의 유틸리티 입니다. `manage.py` 에 대한 자세한 정보는 [django-admin and manage.py](https://docs.djangoproject.com/ko/4.0/ref/django-admin/) 에서 확인할 수 있습니다.

`mysite/` 디렉토리 내부에는 프로젝트를 위한 실제 Python 패키지들이 저장됩니다. 이 디렉토리 내의 이름을 이용하여, (`mysite.urls` 와 같은 식으로) 프로젝트의 어디서나 Python 패키지들을 임포트할 수 있습니다.

`mysite/__init__.py`: Python으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일입니다. Python 초심자라면, Python 공식 홈페이지의 [패키지](https://docs.python.org/3/tutorial/modules.html#tut-packages)를 읽어보세요.

`mysite/settings.py`: 현재 Django 프로젝트의 환경 및 구성을 저장합니다. [Django settings](https://docs.djangoproject.com/ko/4.0/topics/settings/)에서 환경 설정이 어떻게 동작하는지 확인할 수 있습니다.

`mysite/urls.py`: 현재 Django project 의 URL 선언을 저장합니다. Django 로 작성된 사이트의 《목차》 라고 할 수 있습니다. [URL dispatcher](https://docs.djangoproject.com/ko/4.0/topics/http/urls/) 에서 URL 에 대한 자세한 내용을 읽어보세요.

`mysite/asgi.py`: 현재 프로젝트를 서비스하기 위한 ASGI-호환 웹 서버의 진입점입니다. 자세한 내용은 [ASGI를 사용하여 배포하는 방법](https://docs.djangoproject.com/ko/4.0/howto/deployment/asgi/) 를 참조하십시오.

`mysite/wsgi.py`: 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점입니다. [WSGI를 사용하여 배포하는 방법](https://docs.djangoproject.com/ko/4.0/howto/deployment/wsgi/)를 읽어보세요.

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



### 3. git 설치, git bash, github 사용법

- ### git bash & github  사용법 

git 설치, git 사용법, github 사용법
git bash = > 윈도우/리눅스 명령어 사용가능, 자동완성 사용가능(tab키), 상대경로 이동mkdir => 공백 / 한글 / .(온점) 사용하지 말것, 공백 파일 지정 시 ''(따옴표)로 묶음, 또는 _(언더바)로 띄어쓰기 표기

> git init

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMjA1/MDAxNjQ2OTYyNjkyMDM4.6Ru2RK7OOtzev8uHW_d13jFnBCjvbiUAsnrID0N85Z4g.Z_qs5j2O9SVsr2fc0vgMxsPTV4fNYTQxD2XkEDiO7lQg.PNG.xana_/image.png?type=w580)

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMjUw/MDAxNjQ2OTYyNzQ1NDk3.8N7VPQw-zN4_aKiXet2tYWCDkM4PozsX9GuDDMdhj2Ig.hEz4GJkjmGl51ZpVKaeN6RnaSrQvpOwQHczwrkyV3Bcg.PNG.xana_/image.png?type=w580)

숨김파일 생성, 

 ls -a 로 숨김파일 확인가능

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfODQg/MDAxNjQ2OTYyNzgwNTk1.ke1aVuhk8LEWXmewyZDNFWOyenEcgJfxycpcMuAYIAsg.660IdXlQQCiyuQTSvInXDd63tFriNtqF6FaSH8SjhJAg.PNG.xana_/image.png?type=w580)

상위,하위 디렉터리 동시 생성 => -p 옵션

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMjEx/MDAxNjQ2OTYyOTM2NzYz.GnE2s2ZGmKJiUHQw6AH1KbDLyQShDqp4GljiHOHR3Oog.jDWW5gGVGmf1P4WrycJSWdPQzW6VrVY0QDFVRMpd_X0g.PNG.xana_/image.png?type=w580)

하위 폴더/디렉터리 같이 삭제 => -r 옵션

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMTIg/MDAxNjQ2OTYzMTI1OTEy.eEw62GPBqfLYYNNpCILUvkUMEX8dVKGEitc3qHUovkEg.vz6gS9wRmpGL0DSI4Ie2PSvWP3lkbN5iZkeP3X5AJiEg.PNG.xana_/image.png?type=w580)

=> -f 옵션과 같이 사용가능, rmf -rf => 강제 삭제



> vim

vi 같은 문서 편집기

vi 명령어 사용 가능

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMjky/MDAxNjQ2OTY0ODAwMTQx.3nXtgQ-QBKDLM3Ls9ERiHHP7xuHXGLPEs129beb5wOog.NCJxIYbWIXamIzWVQEq6iFXXqYSO-7APg36XBVTIkqcg.PNG.xana_/image.png?type=w580)

> git 명령어

init => 초기화

$ git init

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfNjUg/MDAxNjQ2OTcyMTA1ODcy.aXjZL_GSOYbj3jcjnM8scI5fKeA8D04oiRHzY_VkKUcg._cpP8UQickcXQd9G4yXLEEEou9sl2tnVgoCxeEosjjYg.PNG.xana_/image.png?type=w580)

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfODgg/MDAxNjQ2OTcyMTM0Mjk0.MbhQvMB5_znCAAiIKGYgC9l_X55-Q9HfGrNuXwsIclUg.DLlfTiaWlJdnGevt7vG1q1m5b76Seyv7NIehWGNH2-Mg.PNG.xana_/image.png?type=w580)

관리하고자 하는 디렉터리에만 사용할것

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMTI2/MDAxNjQ2OTc1Njk1NDQ4.KllHr7hUxA4aL65rZtAYnWA0TyJ5mPj-EzBzcxfoSxQg.hHhjAvcOZlOs89SVWwffEjz4KRkwwySe84OO86R_BfAg.PNG.xana_/image.png?type=w580)

.git 생성 => 관리대상

$ git  => 명령어 확인

$ git status => 상태확인

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMjQ4/MDAxNjQ2OTcyNDA4NTM2.08ntrlICbokmYEf8cxTLxYF4nqcWfx1Ajd3i8zCOgEYg.8PmuRt-5DIlqd2QgZ_p2L1Sux3OiKrNlMP6orEhBzVMg.PNG.xana_/image.png?type=w580)

$ git add <file>, . 은 모든 화일 => staging 영역에 올라감

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMTYx/MDAxNjQ2OTcyNTExOTMx.I6qETgXLk3KtQUD8FScXPhBkjn_ZCHAFEP1HYZqpZOkg.Nnzs-5QaE2llQqkc7jcwVXKevEiBUE2nXaXCqeWCrDog.PNG.xana_/image.png?type=w580)

$ git rm --cached <file>, . 은 모든화일 => staging 영역에서 제거

$ git commit, $ git commit -m "<메시지>" =>staging 영역의 working 디렉터리의 내용물을 git으로 관리

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfNzAg/MDAxNjQ2OTcyOTYwOTYx.wxLrqG5HCmM75ECXJ6F8kBIG5eIUILndnRi6Ctou-ywg.4YT9KRaewG5qrLRckGrkVKSR25Nc0ie1nkYxmKraEdYg.PNG.xana_/image.png?type=w580)

=> 이메일 / 이름 등록이 안돼서 오류

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMTY2/MDAxNjQ2OTczNTUwMDI1.zVs5mdO2XDWyq57spyojcs-XHuBE3T2eKKsUYV_pWr0g.EPWXM-2fGYSebBr01C3tH-nIt_jDEBp8f3oH57Q397gg.PNG.xana_/image.png?type=w580)

=> git 관리 사용자 확인을 위해 등록

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMjc5/MDAxNjQ2OTczNTgxNjQy.8Lf7f5im3wKeHmNDeIJs1YoswReOLr8UBpXKAQUzwk0g.A2RNrAZk48CPRQuIam4rrUpWc4JLmueFayNwZ8z0e_Mg.PNG.xana_/image.png?type=w580)

$ git log, $ git log --oneline => git 시점 확인(사용자, 날짜, 커밋 메시지 확인가능)

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMTYy/MDAxNjQ2OTc1OTg2NTc3.u8zGiwHKlLic1twnBloo_qKbcZRJGTMlQ4b1dN3smHsg.jkDY3aSbtvg1ubXh3bitJbwRkSfINuZdnxPsU7uU5_Ug.PNG.xana_/image.png?type=w580)

$ git remote add <원격이름> => 원격이름은 github 주소 별칭같이 사용함, 깃허브 연동 보통 원격 이름은 origin 으로 사용

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMTgz/MDAxNjQ2OTc2NzY5NjQ5.iNv3XLuDbqpgHbPTGPXyTcKAbKil_k4fwh_PgkQEf2Ug.IN46j4oJ7hD2oHtRJ5kgWgf09vv-p_egQpH0j0lWedsg.PNG.xana_/image.png?type=w580)

> github

로그인

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMjgx/MDAxNjQ2OTc2NDU5NzA4.dlRsvju4o44fgtc7YWyack9Tj39FCp1c554ptbC9Qkkg.51NFqCGgPkQuRRSpVRCZxTnGwJ5Ntxanw51rOXZZSMAg.PNG.xana_/111.png?type=w580)



git bash 창

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMzcg/MDAxNjQ2OTc2NjEyOTQ4.kEL26fLmXPnr5iBplsgh3obhiK7WYKYJgY8TFebbm5Qg.jxlmslrP9uHeskCkjQL373CNjVmu7tExM015WaHDKJMg.PNG.xana_/image.png?type=w580)

원격 연동 주소입력

$ git remote add origin https://github.com/donechoi/test.git

$ git remote rm origin => 원격 삭제 명령어 rm

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMjcy/MDAxNjQ2OTc2ODIwNDU2.ZaS9ZsPszlXnWWU_RRD9cntL-gMcsa4112w-aJRNf84g.mBWphBxlqHdJnl0RLcrulrQi61Vc2G2HEzetAfnDv28g.PNG.xana_/image.png?type=w580)

깃허브는 commit 후에 올라간다

$ git push -u <원격지> <브런치> => -u : 업데이트

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMTUy/MDAxNjQ2OTkwNzg1NTk0.KYXOqUlQ4xT7BkbAPKtoXfB79_hpDAfomMVp6TPZpWwg.z4qdqWIZ0THfIQIkaMcqsheW8haI4CLBITInsqRX_a0g.PNG.xana_/image.png?type=w580)



![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMjY5/MDAxNjQ2OTc3MTExNTUz.oBGPdjB4Pcs4tVduO_hSEF-jDu0BJH324TVUuQ_t354g.7noVg5WX2HMks175jAtNgbVyWes8vo316-2N1liTLhMg.PNG.xana_/image.png?type=w580)

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMTM4/MDAxNjQ2OTc3MTY0NzA0.ann7-HWvz07El-XkVxM-Yz0Cn_g7CC8z1YL9vDHb6vAg.jVYNwrtoP7_QZXGvu2Y6Wx-mA5f6TWNcKyleDbMdoMcg.PNG.xana_/image.png?type=w580)

처음 push 하면 인증메시지 뜸 => 인증하면됨

![img](https://postfiles.pstatic.net/MjAyMjAzMTFfOTcg/MDAxNjQ2OTc3Mzk2Mjg2.tL8xh0YL2A3RggVoyHEGnKIo-U0U9u1Wvi83OadIXgog.wN-51geYJXsJkKFHHeRrHQqZ57dEGyl1s5IsdbrPIC4g.PNG.xana_/image.png?type=w580)

새로고침하면 확인 가능



![img](https://postfiles.pstatic.net/MjAyMjAzMTFfMTM3/MDAxNjQ2OTc4Njg2MTI3.lWni9jGFKYNRkriY-2RorwnvEsxmpEkR4wTA18-B_w4g.pwXLlsvQI3MvHwhDn6hf-ZqzGvLTwI6f1pBEI08PnQMg.PNG.xana_/123123.png?type=w580)

컴퓨터에 연결된  깃허브 계정 확인가능



- ### 프로젝트 git 등록 

```objc
Administrator@DESKTOP-L5USBSK MINGW64 /d/Python/workspace/mysite
$ git init
Initialized empty Git repository in D:/Python/workspace/mysite/.git/

Administrator@DESKTOP-L5USBSK MINGW64 /d/Python/workspace/mysite (master)
$ ls
db.sqlite3  mysite/  readme.assets/  scr1.png
manage.py*  polls/   readme.md       scr2.png

Administrator@DESKTOP-L5USBSK MINGW64 /d/Python/workspace/mysite (master)
$ git add .

Administrator@DESKTOP-L5USBSK MINGW64 /d/Python/workspace/mysite (master)
$ git commit
[master (root-commit) 4f4cc38] first commit
 28 files changed, 415 insertions(+)
 create mode 100644 db.sqlite3
 create mode 100644 manage.py
 create mode 100644 mysite/__init__.py
 create mode 100644 mysite/__pycache__/__init__.cpython-39.pyc
 create mode 100644 mysite/__pycache__/settings.cpython-39.pyc
 create mode 100644 mysite/__pycache__/urls.cpython-39.pyc
 create mode 100644 mysite/__pycache__/wsgi.cpython-39.pyc
 create mode 100644 mysite/asgi.py
 create mode 100644 mysite/settings.py
 create mode 100644 mysite/urls.py
 create mode 100644 mysite/wsgi.py
 create mode 100644 polls/__init__.py
 create mode 100644 polls/__pycache__/__init__.cpython-39.pyc
 create mode 100644 polls/__pycache__/urls.cpython-39.pyc
 create mode 100644 polls/__pycache__/views.cpython-39.pyc
 create mode 100644 polls/admin.py
 create mode 100644 polls/apps.py
 create mode 100644 polls/migrations/__init__.py
 create mode 100644 polls/models.py
 create mode 100644 polls/tests.py
 create mode 100644 polls/urls.py
 create mode 100644 polls/views.py
 create mode 100644 readme.assets/image-20220313191518852.png
 create mode 100644 readme.assets/scr1.png
 create mode 100644 readme.assets/scr2.png
 create mode 100644 readme.md
 create mode 100644 scr1.png
 create mode 100644 scr2.png

Administrator@DESKTOP-L5USBSK MINGW64 /d/Python/workspace/mysite (master)
$ git log
commit (HEAD -> master)
Author: LEEYOUNGJIN1 <*************@naver.com>
Date:   Sun Mar 13 22:37:06 2022 +0900
first commit
Administrator@DESKTOP-L5USBSK MINGW64 /d/Python/workspace/mysite (master)

Administrator@DESKTOP-L5USBSK MINGW64 /d/Python/workspace/mysite (master)
$ git remote add origin https://github.com/LEEYOUNGJIN1/mysite.git

Administrator@DESKTOP-L5USBSK MINGW64 /d/Python/workspace/mysite (master)
$ git push -u origin master
Enumerating objects: 31, done.
Counting objects: 100% (31/31), done.
Delta compression using up to 8 threads
Compressing objects: 100% (29/29), done.
Writing objects: 100% (31/31), 129.50 KiB | 12.95 MiB/s, done.
Total 31 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/LEEYOUNGJIN1/mysite.git

 * [new branch]      master -> master
   Branch 'master' set up to track remote branch 'master' from 'origin'.

Administrator@DESKTOP-L5USBSK MINGW64 /d/Python/workspace/mysite (master)
```

