#!/usr/bin/env python
#encoding=UTF8
class Server(object):
def _init_(self, ip, hostname):
    self.ip = ip
    self.hostname = hostname
def set_ip(self, ip):
    self.ip = ip
def set_hostname(self, hostname):
    self.hostname = hostname
def ping(self, ip_addr):
    print "Pinging %s from %s (%s)" % (ip_addr, self.ip, self.hostname)

if_name_ == '_main_':
   server = Server('192.168.1.27', 'localhost')
   server.ping('192.168.1.24')
