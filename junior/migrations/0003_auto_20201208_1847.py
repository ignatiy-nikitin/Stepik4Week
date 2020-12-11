# Generated by Django 3.1.3 on 2020-12-08 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('junior', '0002_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='grade',
            field=models.CharField(choices=[('junior', 'Младший (junior)'), ('middle', 'Средний (middle)'),
                                            ('senior', 'Страший (senior)')], max_length=64),
        ),
        migrations.AlterField(
            model_name='resume',
            name='status',
            field=models.CharField(choices=[('looking_for_a_job', 'Ищу работу'),
                                            ('open_to_suggestions', 'Открыт к предложениям'),
                                            ('not_looking_for_a_job', 'Не ищу работу')], max_length=64),
        ),
    ]
