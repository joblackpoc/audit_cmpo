from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Sectionlist(models.Model):
    
    section_name = models.CharField(max_length=255)

class Document(models.Model):

    title = models.CharField(max_length=150)
    content = RichTextField(blank=True, null=True)
    media = RichTextUploadingField(blank=True, null=True)
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

    def __str__(self):
        return self.title

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Sectionlist,default=1 ,on_delete=models.CASCADE)
    phone = models.CharField(max_length=100,default='0812345678')
    picture = models.ImageField(default='default.jpg',upload_to='profile_pictures')

    def __str__(self):
        return self.user.username


