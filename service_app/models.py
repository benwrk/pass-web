from django.db import models
from service_app.messaging.message_dispatcher import MessageDispatcher

class Floor(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=50)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='groups')

    def __str__(self):
        return self.name

class Ward(models.Model):
    name = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='wards')

    def __str__(self):
        return  self.name

class Box(models.Model):
    mac_address = models.CharField(primary_key=True, max_length=12, unique=True)
    name = models.CharField(max_length=50)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='boxes')

    def __str__(self):
        return self.name + ' @ ' + self.mac_address

class Message(models.Model):
    MESSAGE_TYPE_CHOICES = (
        ('TOAST', 'Toast'),
        ('POPUP', 'Pop-up'),
        ('WELCM', 'Welcome')
    )

    created = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField()
    message = models.CharField(max_length=200)
    send_to = models.ManyToManyField(Box, related_name='messages')
    sender = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=5, choices=MESSAGE_TYPE_CHOICES)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)

        while len(Message.objects.all()) > 10000:
            message[0].delete()
