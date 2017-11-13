# -*- coding: utf-8 -*-
'''
# @FileName: 
# @Created : 2014-2-17 14:46:45
# @Author  : 
# @Version : Dev 1.0.0.0
'''
from soaplib.core import Application
from soaplib.core.server.wsgi import Application as WSGIApplication
from django.http import HttpResponse
from soaplib.core.model.primitive import Boolean, String
from soaplib.core.model.clazz import ClassModel
from soaplib.core.service import DefinitionBase, rpc
import StringIO
import os
import copy

NEW_DIR = os.path.join(os.getcwd(),"interface_dir/new")
OLD_DIR = os.path.join(os.getcwd(),"interface_dir/old")

class SHead(ClassModel):
    SYSTEM_ID = String
    TRAN_MODE = String
    TRAN_DATE = String
    TRAN_TIMESTAMP = String 
    SERVER_ID = String
    WS_ID = String
    USER_LANG = String
    USER_ID = String
    SEQ_NO = String
    COUNTRY = String
    PAGE_NUM = String
    PAGE_INDEX = String
    PAGE_SIZE  = String

    
class SBody(ClassModel):
    dataType = String
    timeStamp = String
    isZip = String
    filePath = String
    fileName = String
    md5 = String    


class DumbStringIo(StringIO.StringIO):
    
    def read(self, n=-1):
        return self.getvalue()

class DjangoSoapApp(WSGIApplication):
    """
    Generic Django view for creating SOAP web services (works with soaplib 2.0)
    Based on http://djangosnippets.org/snippets/2210/
    """

    csrf_exempt = True

    def __init__(self, services, tns):
        """Create Django view for given SOAP soaplib services and tns"""
        
        return super(DjangoSoapApp, self).__init__(Application(services, tns))

    def __call__(self, request):
        django_response = HttpResponse()
        remote = str(request.META.get("REMOTE_ADDR"))
        #@todo: 此处增加控制
        write_log([u"接口被访问%s"%str("("+remote+")"),request.raw_post_data])

        def start_response(status, headers):
            django_response.status_code = int(status.split(' ', 1)[0])
            for header, value in headers:
                django_response[header] = value
        
        environ = request.META.copy()
        environ['CONTENT_LENGTH'] = len(request.raw_post_data)
        environ['CONTENT_TYPE'] = 'text/html; charset=utf-8' #text/html; charset=utf-8
        environ['wsgi.input'] = DumbStringIo(request.raw_post_data)
        environ['wsgi.multithread'] = False
        response = super(DjangoSoapApp, self).__call__(environ, start_response)
        django_response.content = '\n'.join(response)

        return django_response
    
class MySOAPService(DefinitionBase):
    '''    '''
    @rpc(SHead,SBody,_returns=String)
    def BigFileService(self,SHEAD,SBODY):
        shead_dic,sbody_dic = self.setObjectDict(SHEAD, SBODY)

        #***********开一个线程取数据***********
        import threading
        import time
        
        lock = threading.RLock()       
        def my_thread(shead_dic, sbody_dic):
                  
            if lock.acquire():
                #write_logs_sql  # 用django 模型 modules.save() 将出错
                time.sleep(3)
                
                lock.release()
        #***********线程结束****************
                
        threading.Thread(target=my_thread,args =(shead_dic,sbody_dic)).start()
        return "SUCCESS" #SUCCESS  
        

    def setObjectDict(self,obj1,obj2):
        shead_dic = {}
        shead_dic['SYSTEM_ID'] = obj1.SYSTEM_ID or ""
        shead_dic['TRAN_MODE'] = obj1.TRAN_MODE
        shead_dic['TRAN_DATE'] = obj1.TRAN_DATE
        shead_dic['TRAN_TIMESTAMP'] = obj1.TRAN_TIMESTAMP
        shead_dic['SERVER_ID'] = obj1.SERVER_ID
        shead_dic['WS_ID'] = obj1.WS_ID
        shead_dic['USER_LANG'] = obj1.USER_LANG
        shead_dic['USER_ID'] = obj1.USER_ID
        shead_dic['SEQ_NO'] = obj1.SEQ_NO
        shead_dic['COUNTRY'] = obj1.COUNTRY
        shead_dic['PAGE_NUM'] = obj1.PAGE_NUM
        shead_dic['PAGE_INDEX'] = obj1.PAGE_INDEX
        shead_dic['PAGE_SIZE'] = obj1.PAGE_SIZE
                        
        sbody_dic = {}
        sbody_dic['dataType'] = obj2.dataType or ""
        sbody_dic['timeStamp'] = obj2.timeStamp 
        sbody_dic['isZip'] = obj2.isZip
        sbody_dic['filePath'] = obj2.filePath 
        sbody_dic['fileName'] = obj2.fileName  
        sbody_dic['md5'] = obj2.md5    
                                   
        return shead_dic,sbody_dic
    
    
interfaceSoap = DjangoSoapApp([MySOAPService], 'http://www.***.com/esb/service/BigFileService')

#******日志sql****************
def write_logs_sql(log_info=[]):
    '''写日志  insert into到日志表'''

  
#************写服务日志************
def write_log(log_info = []):
    u"写处理日志"
    #log = serviceLog()
    #log.message = u"; \n".join(log_info) 
    #log.save()

def resendMessage(url,message_args):
    '''    '''
    error_info = []
    
    message_temp ='''<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <ns2:esbSoapHeader xmlns:ns2="http://www.***.com/esb/service/FileResendServices" xmlns="http://www.***.com/esb/metadata">
      <From xmlns:ns3="http://www.***.com/esb/metadata">%(sendSystem)s</From>
      <To xmlns:ns3="http://www.***.com/esb/metadata">%(receiveSystem)s</To>
    </ns2:esbSoapHeader>
  </soap:Header>
  <soap:Body><ns2:FileResendService xmlns:ns2="http://www.***.com/esb/service/FileResendServices" xmlns="http://www.***.com/esb/metadata">
      <ns2:SHEAD>
        <SYSTEM_ID>%(sendSystem)s</SYSTEM_ID>
        <TRAN_MODE xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"></TRAN_MODE>
        <TRAN_DATE xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"></TRAN_DATE>
        <TRAN_TIMESTAMP xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"></TRAN_TIMESTAMP>
        <SERVER_ID xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"></SERVER_ID>
        <WS_ID xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"></WS_ID>
        <USER_LANG xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"></USER_LANG>
        <USER_ID xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"></USER_ID>
        <SEQ_NO>%(batch_sn)s</SEQ_NO>
        <COUNTRY xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"></COUNTRY>
        <PAGE_NUM xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"></PAGE_NUM>
        <PAGE_INDEX xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"></PAGE_INDEX>
        <PAGE_SIZE xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"></PAGE_SIZE>
      </ns2:SHEAD>
      <ns2:SBODY>
        <dataType>%(dataType)s</dataType>
        <timestamp xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true">%(timestamp)s</timestamp>
      </ns2:SBODY>
    </ns2:FileResendService>
  </soap:Body>
</soap:Envelope>
    '''
    message_body = message_temp%message_args
    
    content = ""
    import urllib2
    try:
        f = urllib2.urlopen(url, message_body) 
        content = f.read()
    except Exception,e:
        error_info.append(u"发送消息失败:%(url)s,%(e)s"%{"url":url,"e":e})
    message_results = {"content":content,"error_info":error_info}
    return message_results    
    
def CastAsBoolean(FlagStr):
    FlagCap = FlagStr.capitalize()
    if FlagCap==str(True):
        return True
    else:
        return False


