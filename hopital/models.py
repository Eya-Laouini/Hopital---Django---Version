from django.db import models
class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=50)
    numtel = models.IntegerField()
    dateNais = models.DateField()
    service = models.ForeignKey('Service', on_delete=models.CASCADE,)
    def __str__(self) -> str:
        return self.nom
        
class Service(models.Model):
    #idSer = models.AutoField(primary_key=True)
    nomSer = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self) -> str:
        return self.nomSer