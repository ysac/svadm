from django.db import models

class Service(models.Model):
    service_id   = models.CharField(max_length=256,unique=True)
    service_name = models.CharField(max_length=256,unique=True)

    def __unicode__(self):
        return self.service_id

class Os(models.Model):
    os_name   = models.CharField(max_length=256,unique=True)

    def __unicode__(self):
        return self.os_name

class Status(models.Model):
    status_name   = models.CharField(max_length=256,unique=True)

    def __unicode__(self):
        return self.status_name

class Server(models.Model):
    hostname      = models.CharField(u'hostname',max_length=256,unique=True)
    status        = models.ForeignKey(Status)
    os            = models.ForeignKey(Os)
    service       = models.ForeignKey(Service)
#    service_id    = models.CharField(max_length=20)
#    service_name  = models.CharField(max_length=20)
#    ip4_addr      = models.CharField(max_length=20)
#    ip6_addr      = models.CharField(max_length=20)
#    load_balancer = models.CharField(max_length=20)
#    machine_group = models.CharField(max_length=20)
#    opennms_host  = models.CharField(max_length=20)
#    opennms_id    = models.CharField(max_length=20)

    def __unicode__(self):
        return self.hostname

#
#Class Opennms(models.Model):
#    id   = models.CharField(max_length=20)
#    host = models.CharField(max_length=20)
#
#    del __unicode__(self):
#        return self.id
#
