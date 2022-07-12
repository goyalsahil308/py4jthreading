from __future__ import division
import os
import time
from threading import Thread
from numpy import multiply
class PythonPlayer(object):

    def multiply(self,a):
        print(y.multi(a))
    def multiply2(self,a):
        print(y.multi2(a))
    def division(self,a):
        print(y.divi(a))
    def plus(self,a,b):
        return a+b
    def minus(self,a,b):
        return a-b
    def response(self,object):
        return y.resp(object)
    def response2(self):
        return "Got response from python thread2"
    def sumjava(self,object):
        return y.sum(object)
    class Java:
        implements = ["py4j.PongPlayer"]

from py4j.java_gateway import JavaGateway, CallbackServerParameters
pong_player = PythonPlayer()
gateway = JavaGateway(callback_server_parameters=CallbackServerParameters(),python_server_entry_point=pong_player)
y=gateway.entry_point
for i in range(100):
    t2=Thread(target=pong_player.division,args=(10,))
    t1=Thread(target=pong_player.multiply,args=(5,))
    t3=Thread(target=pong_player.multiply2,args=(5,))
    t4=Thread(target=pong_player.response,args=(pong_player,))
    t5=Thread(target=pong_player.sumjava,args=(pong_player,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
def timer():
    time.sleep(2)
    print("Sleeping done ")
timer()
os._exit(1)