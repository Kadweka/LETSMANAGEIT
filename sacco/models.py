from django.db import models

# Create your models here.
class SaccoManager(models.Model):
    Fname=models.CharField(max_length=10)
    Lname=models.CharField(max_length=10)
    Email=models.EmailField()
    Phone=models.IntegerField()
    # Id=models.FileField(max_length=10)

    def __str__(self):
        return self.Fname
    class Meta:
        ordering = ['Fname']


class MatatuDriver(models.Model):
    Fname1=models.CharField(max_length=10)
    Lname1=models.CharField(max_length=10)
    Mobile=models.IntegerField()
    Dlincence=models.IntegerField()
    Manager = models.ForeignKey(SaccoManager,on_delete=models.CASCADE)

    def __str__(self):
        return self.Fname1
    class Meta:
        ordering = ['Fname1']


class MatatuConductor(models.Model):
    Fname12=models.CharField(max_length=10)
    Lname12=models.CharField(max_length=10)
    Mobile=models.IntegerField()
    Driver = models.ForeignKey(MatatuDriver,on_delete=models.CASCADE)
    def __str__(self):
        return self.Fname12
    class Meta:
        ordering = ['Fname12']


class MatatuCollect(models.Model):
    okota=models.CharField(max_length=10)
    mwaga=models.CharField(max_length=10)
    amountperperson=models.IntegerField()
    # Driver = models.ForeignKey(MatatuDriver)
    def __str__(self):
        return self.okota
    class Meta:
        ordering = ['okota']


class SaccoMatatu(models.Model):
    Pnumber=models.CharField(max_length=15)
    Mcolour = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'))
    Snumber=models.IntegerField()
    Ntrips=models.IntegerField()

    def __str__(self):
        return self.Pnumber
    class Meta:
        ordering = ['Pnumber']