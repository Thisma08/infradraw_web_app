from django.db import models

class Application(models.Model):
    app_id = models.AutoField(primary_key=True, default=0)
    aCode = models.CharField(max_length=10)
    nameFr = models.CharField(max_length=250)
    nameNl = models.CharField(max_length=250)
    nameEn = models.CharField(max_length=250)
    status = models.CharField(max_length=30)
    
    # app_id = models.AutoField(primary_key=True)
    # a_code = models.CharField(max_length=10)
    # name_fr = models.CharField(max_length=250)
    # name_nl = models.CharField(max_length=250)
    # name_en = models.CharField(max_length=250)
    # app_status = models.CharField(max_length=30)

    class Meta:
        # db_table = 'A1788_application'
        db_table = 'application'
        
class Environment(models.Model):
    env_id = models.AutoField(primary_key=True, default=0)
    guid = models.CharField(max_length=40)
    name = models.CharField(max_length=100)
    env_type = models.CharField(max_length=3)
    status = models.CharField(max_length=30)
    applicationId = models.ForeignKey(Application, on_delete=models.CASCADE, db_column='applicationId', default=0)
    
    # env_id = models.AutoField(primary_key=True)
    # guid = models.CharField(max_length=40)
    # env_name = models.CharField(max_length=100)
    # env_type = models.CharField(max_length=3)
    # env_status = models.CharField(max_length=30)
    # app_id = models.ForeignKey(Application, on_delete=models.CASCADE, db_column='app_id')

    
    class Meta:
        # db_table = 'A1788_environment'
        db_table = 'environment'

