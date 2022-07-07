# Generated by Django 4.0.6 on 2022-07-06 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionlist', models.CharField(choices=[('1', 'พัฒนายุทธศาสตร์สาธารณสุข'), ('2', 'บริหารทั่วไป'), ('3', 'ทันตสาธารณสุข'), ('4', 'ควบคุมโรคติดต่อ'), ('5', 'คุ้มครองผู้บริโภคและเภสัชสาธารณสุข'), ('6', 'บริหารทรัพยากรบุคคล'), ('7', 'นิติกร'), ('8', 'พัฒนาคุณภาพและสรุปแบบบริการ'), ('9', 'ส่งเสริมสุขภาพ'), ('10', 'อนามัยสิ่งแวดล้อมและอาชีวอนามัย'), ('11', 'ประกันสุขภาพ'), ('12', 'ควบคุมโรคไม่ติดต่อ สุขภาพจิตและยาเสพติด'), ('13', 'แพทย์แผนไทยและการแพทย์ทางเลือก'), ('14', 'สุขศึกษาประชาสัมพันธ์'), ('15', 'None')], default=1, max_length=100)),
                ('user_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
