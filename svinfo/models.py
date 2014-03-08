from django.db import models

class Server(models.Model):
    hostname      = models.CharFileld(max_length=20)
    status        = models.CharFileld(max_length=20)
    service_id    = models.CharFileld(max_length=20)
    service_name  = models.CharFileld(max_length=20)
    os            = models.CharFileld(max_length=20)
    ip4_addr      = models.CharFileld(max_length=20)
    ip6_addr      = models.CharFileld(max_length=20)
    load_balancer = models.CharFileld(max_length=20)
    machine_group = models.CharFileld(max_length=20)
    opennms_host  = models.CharFileld(max_length=20)
    opennms_id    = models.CharFileld(max_length=20)

    def __str__(self):
        return self.hostname

Class Service(models.Model):
    id   = models.CharFileld(max_length=20)
    name = models.CharFileld(max_length=20)

    def __str__(self):
        return self.id

Class Opennms(models.Model):
    id   = models.CharFileld(max_length=20)
    host = models.CharFileld(max_length=20)

    del __str__(self):
        return self.id

