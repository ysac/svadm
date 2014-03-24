#comment
from django.db import models

class Service(models.Model):
    service_id   = models.CharField(max_length=256,unique=True)
    service_name = models.CharField(max_length=256,unique=True)

    def __unicode__(self):
        return self.service_id

class Role(models.Model):
    role_name = models.CharField(max_length=256,unique=True)

    def __unicode__(self):
        return self.role_name

class Status(models.Model):
    status_name   = models.CharField(max_length=256,unique=True)

    def __unicode__(self):
        return self.status_name

class OS(models.Model):
    os_name   = models.CharField(max_length=256,unique=True)

    def __unicode__(self):
        return self.os_name

class LB(models.Model):
    lb_name = models.CharField(max_length=256,unique=True)

    def __unicode__(self):
        return self.lb_name

class Server(models.Model):
    hostname      = models.CharField(max_length=256,unique=True)
    service       = models.ForeignKey(Service)
    role          = models.ForeignKey(Role)
    status        = models.ForeignKey(Status)
    os            = models.ForeignKey(OS)
    ip4           = models.IPAddressField(unique=True)
    ip6           = models.CharField(max_length=256,blank=True)
    lb            = models.ForeignKey(LB)
    opennms_id    = models.CharField(max_length=256,blank=True)
    opennms_host  = models.CharField(max_length=256,blank=True)
    opennms_mac   = models.CharField(max_length=256,blank=True)
    comment       = models.CharField(max_length=256,blank=True)

    def __unicode__(self):
        return self.hostname
