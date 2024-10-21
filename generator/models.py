from django.db import models

# Create your models here.

class QR(models.Model):
    title= models.CharField(max_length=20, null=True)
    text= models.TextField(max_length=250)
    created_at= models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
class QRImage(models.Model):
    connection=models.ForeignKey(QR, on_delete=models.CASCADE)
    qr_image= models.ImageField(default= "qr.png")

    def __str__(self):
        return self.title