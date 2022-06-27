# Generated by Django 4.0.3 on 2022-04-22 00:05

import cfipage.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_facebook_event_twitter'),
    ]

    operations = [
        migrations.AddField(
            model_name='attend',
            name='age',
            field=models.CharField(choices=[('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60'), ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('66', '66'), ('67', '67'), ('68', '68'), ('69', '69'), ('70', '70'), ('71', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('75', '75'), ('76', '76'), ('77', '77'), ('78', '78'), ('79', '79'), ('80', '80'), ('81', '81'), ('82', '82'), ('83', '83'), ('84', '84'), ('85', '85'), ('86', '86'), ('87', '87'), ('88', '88'), ('89', '89')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='attend',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='attend',
            name='governorates',
            field=models.CharField(choices=[('AN', 'الانبار'), ('BB', 'بابل'), ('BG', 'بغداد'), ('BA', 'البصرة'), ('DQ', 'ذي قار'), ('QA', 'القادسية'), ('DI', 'ديالى'), ('DA', 'دهوك'), ('AR', 'اربيل'), ('KA', 'كربلاء'), ('KI', 'كركوك'), ('MA', 'ميسان'), ('MU', 'مثنى'), ('NA', 'النجف'), ('NI', 'نينوى'), ('SD', 'صلاح الدين'), ('SU', 'السليمانية'), ('WA', 'واسط')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='attend',
            name='phoneNo',
            field=models.CharField(blank=True, help_text='077 or 078 or 075', max_length=11, null=True, validators=[cfipage.utils.validate_phone]),
        ),
        migrations.AlterField(
            model_name='attend',
            name='specialty',
            field=models.CharField(choices=[('MD', 'طبية'), ('ENG', 'هندسية'), ('SCI', 'العلوم'), ('FE', 'كلية التربية'), ('IN', 'معهد'), ('S', 'طالب اعدادية')], max_length=3, null=True),
        ),
    ]