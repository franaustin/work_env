============以下内容转载自: http://topmanopensource.iteye.com/blog/2004853
pypi国内镜像目前有：

http://pypi.douban.com/  豆瓣
http://pypi.hustunique.com/  华中理工大学
http://pypi.sdutlinux.org/  山东理工大学
http://pypi.mirrors.ustc.edu.cn/  中国科学技术大学

对于pip这种在线安装的方式来说，很方便，但网络不稳定的话很要命。使用国内镜像相对好一些，

如果想手动指定源，可以在pip后面跟-i 来指定源，比如用豆瓣的源来安装web.py框架：

pip install web.py -i http://pypi.douban.com/simple

注意后面要有*/simple*目录！！！

要配制成默认的话，需要创建或修改配置文件（linux的文件在~/.pip/pip.conf，windows在%HOMEPATH%\pip\pip.ini），修改内容为：

code:
[global]
index-url = http://pypi.douban.com/simple

这样在使用pip来安装时，会默认调用该镜像。

更多配置参数见：http://www.pip-installer.org/en/latest/configuration.html

Configuration
Config file

pip allows you to set all command line option defaults in a standard ini style config file.

The names and locations of the configuration files vary slightly across platforms.

    On Unix and Mac OS X the configuration file is: $HOME/.pip/pip.conf
    On Windows, the configuration file is: %HOME%\pip\pip.ini

You can set a custom path location for the config file using the environment variable PIP_CONFIG_FILE.

The names of the settings are derived from the long command line option, e.g. if you want to use a different package index (--index-url) and set the HTTP timeout (--default-timeout) to 60 seconds your config file would look like this:

[global]
timeout = 60
index-url = http://download.zope.org/ppix

Each subcommand can be configured optionally in its own section so that every global setting with the same name will be overridden; e.g. decreasing the timeout to 10 seconds when running the freeze(Freezing Requirements) command and using 60 seconds for all other commands is possible with:

[global]
timeout = 60

[freeze]
timeout = 10

Boolean options like --ignore-installed or --no-dependencies can be set like this:

[install]
ignore-installed = true
no-dependencies = yes

Appending options like --find-links can be written on multiple lines:

[global]
find-links =
    http://download.example.com

[install]
find-links =
    http://mirror1.example.com
    http://mirror2.example.com

Environment Variables

pip’s command line options can be set with environment variables using the formatPIP_<UPPER_LONG_NAME> . Dashes (-) have to replaced with underscores (_).

For example, to set the default timeout:

export PIP_DEFAULT_TIMEOUT=60

This is the same as passing the option to pip directly:

pip --default-timeout=60 [...]

To set options that can be set multiple times on the command line, just add spaces in between values. For example:

export PIP_FIND_LINKS="http://mirror1.example.com http://mirror2.example.com"

is the same as calling:

pip install --find-links=http://mirror1.example.com --find-links=http://mirror2.example.com

Config Precedence

Command line options have precedence over environment variables, which have precedence over the config file.

Within the config file, command specific sections have precedence over the global section.

Examples:

    --host=foo overrides PIP_HOST=foo
    PIP_HOST=foo overrides a config file with [global] host = foo
    A command specific section in the config file [<command>] host = bar overrides the option with same name in the [global] config file section

Command Completion

pip comes with support for command line completion in bash and zsh.

To setup for bash:

$ pip completion --bash >> ~/.profile

To setup for zsh:

$ pip completion --zsh >> ~/.zprofile

Alternatively, you can use the result of the completion command directly with the eval function of you shell, e.g. by adding the following to your startup file:

eval "`pip completion --bash`"

Next  Previous


Window 需要修改：

%PYTHON_HOME%\Lib\site-packages\pip\cmdoptions.py
Java代码  收藏代码

    index_url = OptionMaker(  
        '-i', '--index-url', '--pypi-url',  
        dest='index_url',  
        metavar='URL',  
        #default='https://pypi.python.org/simple/',  
         default='http://mirrors.bistu.edu.cn/pypi/',  
        help='Base URL of Python Package Index (default %default).')  

 

%PYTHON_HOME%\Lib\site-packages\pip\commands\search.py

 
Java代码  收藏代码

    class SearchCommand(Command):  
        """Search for PyPI packages whose name or summary contains <query>."""  
        name = 'search'  
        usage = """  
          %prog [options] <query>"""  
        summary = 'Search PyPI for packages.'  
      
        def __init__(self, *args, **kw):  
            super(SearchCommand, self).__init__(*args, **kw)  
            self.cmd_opts.add_option(  
                '--index',  
                dest='index',  
                metavar='URL',  
                #default='https://pypi.python.org/pypi',  
                default='http://mirrors.bistu.edu.cn/pypi/',  
                help='Base URL of Python Package Index (default %default)')  
      
            self.parser.insert_option_group(0, self.cmd_opts)  

 
[Linux]修改easy_install和pip的镜像地址

使用easy_install和pip会让Pyhthon的模块安装和管理变得非常简单，但是，如果你身在国内的话，从官方的镜像下载的速度是很令人抓狂的事情，如同修改apt-get或yum的镜像地址一样，easy_install和pip也需要修改镜像地址。修改easy_install和pip的镜像地址通常可以有以下两种方法，可以分别使用命令和配置方式实现。

方法1:命令方式临时修改
easy_install:
easy_install -i http://e.pypi.python.org/simple fabric

pip:
pip -i http://e.pypi.python.org/simple install fabric

 

方法2:配置方式修改
easy_install:
1.打开pydistutils.cfg
vi ~/.pydistutils.cfg

2.写入以下内容
[easy_install]
index_url = http://e.pypi.python.org/simple

pip:
1.打开pip.conf
vi ~/.pip/pip.conf

2.写入以下内容	
[global]
index-url = http://e.pypi.python.org/simple

速度比较快的国内镜像，都来自清华大学，服务器在北京。公网的服务器为官方镜像
公网：http://e.pypi.python.org/simple
教育网：http://pypi.tuna.tsinghua.edu.cn/simple