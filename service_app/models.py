from django.db import models

class Floor(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return 'Floor: ' + self.name

class Group(models.Model):
    name = models.CharField(max_length=50)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='groups')

    def __str__(self):
        return 'Group: ' + self.name

class Ward(models.Model):
    name = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='wards')

    def __str__(self):
        return 'Ward: ' + self.name

class Box(models.Model):
    name = models.CharField(max_length=50)
    mac_address = models.CharField(max_length=12, unique=True)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='boxes')

    def __str__(self):
        return 'Box: ' + self.name + ' @ ' + self.mac_address
