from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('animals', '0001_initial'),
    ]
    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('animals', models.ManyToManyField(related_name='features', to='animals.animal')),
            ],
        ),
    ]
