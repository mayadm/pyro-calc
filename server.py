#!/usr/bin/python

import Pyro.core
import os

class Buah(Pyro.core.ObjBase):
        def __init__(self):
                Pyro.core.ObjBase.__init__(self)
        def jus(self,nilai1,nilai2,opt):
            if opt == "+":
               hasil = int(nilai1) + int(nilai2)
            if opt == "-":
               hasil = int(nilai1) - int(nilai2)
            if opt == "*":
               hasil = int(nilai1) * int(nilai2)
            if opt == "/":
               hasil = int(nilai1) / int(nilai2)
            return hasil              

def main():
    Pyro.core.initServer()
    daemon=Pyro.core.Daemon()
    uri=daemon.connect(Buah(),"jambu")

    print "server ok",daemon.port
    print "The object's uri is:",uri

    daemon.requestLoop()
    
if __name__=="__main__":
    main()

