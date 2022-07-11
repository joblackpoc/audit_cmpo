import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django_ckeditor_5.fields import CKEditor5Field
class Sectionlist(models.Model):
    section_name = models.CharField(max_length=255)
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sectionlist = models.ForeignKey(Sectionlist, on_delete=models.CASCADE)
    user_phone = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

class Document(models.Model):

    title = models.CharField(max_length=150)
    content = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(default='document.jpg', upload_to='document_image')
    uploadfile = models.FileField('Document', upload_to='document_file')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=())
    update_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Document, self).save(*args, **kwargs)


