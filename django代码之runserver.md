django代码之runserver.py 
 接下来，就步入正题了， 从 manage.py runserver开始吧。

接前一章的分析，进入 django.core.management.commands.runserver

还好了，这个runserver.py里的Command类是继承自BaseCommand的，还是比较简单的。

那直接从handle方法开始吧。

可以看到方法是这样的

def handle(self, addrport='', *args, **options):

self.run(*args, **options)

而

def run(self, *args, **options):呢，会调用两种，一种是autoreload, 一种是self.inner_run,

实际上呢，autoreload只是在文件发生变化的时候，直接再load一下，都会调用到 inner_run。

那么，就接着看inner_run吧。

首先还是常见的，

from django.conf import settings 《－导入settings

from django.utils import translation ＃这个有新意，是用于控制显示语言的。

下面这两句，才是真正的决定，用什么来处理http_request.


handler = self.get_handler(*args, **options)

run(self.addr, int(self.port), handler,

ipv6=self.use_ipv6, threading=threading)


handler是从get_internal_wsgi_application()来的，

不过这个在django.core.servers.basehttp.py中得到的处理，

我觉得是直接调用django.core.wsgi.py中的 get_wsgi_application()去了，而这个真正返回了

django.core.handlers.wsgi.WSGIHandler

先看一下整体的逻辑吧。 


 接下来的， 关于WSGIHandler的处理，涉及到了 PEP－0333，也就是python wsgi的规范。

可以简单的说一下，关于server/gateway方面的定义，主要是 mod_wsgi来实现的，

关于 application/framework的，就是django实现的。

这部分呢，主要要求一个可调用的对象，

对于python来讲，可以是一个function, 一个class 或者说一个有__call__方法的instance.

那么WSGIHandler，很明显，就是一个有__call__方法的东东了。

处理肯定是掉入这里了。

参数嘛，就是我们能看到的。

class WSGIHandler(base.BaseHandler):


def __call__(self, environ, start_response):

environ:用于传递环境参数，是一个python内置的dictionary.

start_response：是一个可调用的对象。

runserver.py --> basehttp.py --> wsgi.py  
				    └──-> handlers.wsgi.py(WSGIHandler)  
						└─-> handlers.base.py(BaseHandler) 

再接下来分析一下关于BaseHandler吧，实际上这里有django 最核心的处理middleware的调用逻辑。
![django-middleware](https://docs.djangoproject.com/en/1.5/_images/middleware.png)

https://docs.djangoproject.com/en/1.5/topics/http/middleware/ 这里有一个很详细的说明。


process_request → process_view ->process_template_response ->process_response

中间，如果有process_request或者process_view产生了response, 那么后边的方法就不会接着调用了。

而process_template_response与process_response 是必须要生成一个response的。


这个处理一直是由 WSGIHandler与BaseHandler两个类一起完成的。

首先是在 __call__中进行middleware的初始化的调用。

self.load_middleware()

在BaseHandler中def load_middleware(self)则是真正的按下面的分类，初始化了五类middleware, 上面的四类外，再加了一个exception_middleware.

self._view_middleware = []

self._template_response_middleware = []

self._response_middleware = []

self._exception_middleware = []


request_middleware = [] #这个最终被赋值给了 self._request_middleware


然后接下来，就是生成一个request, 这个是用WSGIRequest生成的，

再调用BaseHandler里的get_response方法，进行request的处理，也就是上面图中的处理。

这里可以很明显地的看到，先调用 self._request_middleware里的方法，

然后再调用 self._view_middleware， 这个前面，对url进行了分析， 然后把url 里定义参数，得出来准备在后边的view方法里，调用了。

如果都没有response，就调用callback， 也就是我们写的view 方法了。

随后开始中调用self._template_response_middleware

再整个方法的最后调用self._response_middleware 