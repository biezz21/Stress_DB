from django.db import models
from django.utils import timezone


# Create your models here.
class Description(models.Model):
	class Meta:
		db_table = 'Description'
	id = models.AutoField(primary_key=True)

	SRP_ID				= models.CharField(max_length=200 ,blank=True)
	SRR_ID				= models.CharField(max_length=200 ,blank=True)
	Assay_Type			= models.CharField(max_length=200 ,blank=True)
	Cultivar			= models.CharField(max_length=200 ,blank=True)
	Treatment			= models.CharField(max_length=200 ,blank=True)
	Stage				= models.CharField(max_length=200 ,blank=True)
	Tissue				= models.CharField(max_length=200 ,blank=True)
	Layout				= models.CharField(max_length=200, blank=True)
	Treat				= models.CharField(max_length=200, blank=True)



class tpm_list(models.Model):
	class Meta:
		db_table = 'tpm_list'
	id = models.AutoField(primary_key=True)

	target_id			= models.CharField(max_length=200 ,blank=True)
	Tpm 				= models.CharField(max_length=500 ,blank=True)






class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title