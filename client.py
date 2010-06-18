#!/usr/bin/python
import Pyro.core

haus = Pyro.core.getProxyForURI("PYROLOC://localhost:7766/jambu")
print "Masukan angka pertama :"
nguk = raw_input()
print "Masukan angka kedua :"
ngik = raw_input()
print "Masukan operasi [ + - / * ]:"
opt = raw_input()
hasil = haus.jus(nguk,ngik,opt)
print "Hasilnya adalah "+int(hasil)+""
