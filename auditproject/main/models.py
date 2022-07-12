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


