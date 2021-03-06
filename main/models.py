from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Sectionlist(models.Model):
    
    section_name = models.CharField(max_length=255)

    def __str__(self):
        return self.section_name

class Document(models.Model):

    title = models.CharField(max_length=150)
    section = models.ForeignKey(Sectionlist,default=1 ,on_delete=models.CASCADE)
    shortnote = models.CharField(max_length=150)
    content = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(default='document.png', upload_to='document_image')
    uploadfile = models.FileField('Document',upload_to='document_file')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Document, self).save(*args, **kwargs)

    def __str__(self):
        return self.title +' - '+ str(self.user.first_name) +' - '+ str(self.user.last_name)

    def get_absolute_url(self):  
        return reverse('home')

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Sectionlist,default=1 ,on_delete=models.CASCADE)
    phone = models.CharField(max_length=20,default='0810000000')
    picture = models.ImageField(default='default.png',upload_to='profile_pictures')

    def __str__(self):
        return self.user.username+' - '+self.user.first_name+' - '+self.user.last_name
    


