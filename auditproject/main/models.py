from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    sectionlist = (
        ('1','พัฒนายุทธศาสตร์สาธารณสุข'),
        ('2','บริหารทั่วไป'),
        ('3','ทันตสาธารณสุข'),
        ('4','ควบคุมโรคติดต่อ'),
        ('5','คุ้มครองผู้บริโภคและเภสัชสาธารณสุข'),
        ('6','บริหารทรัพยากรบุคคล'),
        ('7','นิติกร'),
        ('8','พัฒนาคุณภาพและสรุปแบบบริการ'),
        ('9','ส่งเสริมสุขภาพ'),
        ('10','อนามัยสิ่งแวดล้อมและอาชีวอนามัย'),
        ('11','ประกันสุขภาพ'),
        ('12','ควบคุมโรคไม่ติดต่อ สุขภาพจิตและยาเสพติด'),
        ('13','แพทย์แผนไทยและการแพทย์ทางเลือก'),
        ('14','สุขศึกษาประชาสัมพันธ์'),
        ('15','None'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sectionlist = models.CharField(max_length=100, choices=sectionlist, default=1)
    user_phone = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
