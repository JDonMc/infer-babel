# Generated by Django 3.0.6 on 2020-09-20 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, unique=True)),
                ('changes', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Change')),
            ],
        ),
        migrations.CreateModel(
            name='Dosage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Herb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, unique=True)),
                ('changes', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Change')),
                ('dosages', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Dosage')),
                ('functions', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Function')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('item_name', models.CharField(default='', max_length=200, unique=True)),
                ('author', models.CharField(default='', max_length=200, unique=True)),
                ('success', models.BooleanField(default=False)),
                ('submit_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Mechanism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compound_or_herb', models.TextField(default='', max_length=1440)),
                ('associated_effect', models.TextField(default='', max_length=1440)),
                ('quote', models.TextField(default='', max_length=1440)),
                ('reference', models.URLField(blank=True, default='', max_length=2000)),
                ('authors', models.TextField(default='', max_length=1440)),
                ('copyright', models.TextField(default='', max_length=1440)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotes', models.ManyToManyField(default=None, to='Mixed.Quotation')),
            ],
        ),
        migrations.CreateModel(
            name='Side_Effect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotes', models.ManyToManyField(default=None, to='Mixed.Quotation')),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, unique=True)),
                ('changes', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Change')),
                ('dosages', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Dosage')),
                ('functions', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Function')),
                ('mechanisms', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Mechanism')),
                ('reviews', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Review')),
                ('side_effects', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Side_Effect')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, unique=True)),
                ('original', models.IntegerField(default=0)),
                ('description', models.TextField(default='', max_length=144000)),
                ('img', models.URLField(blank=True, default='', max_length=2000)),
                ('price', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('sale_qty', models.IntegerField(default=0)),
                ('latest_change_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('compounds', models.ManyToManyField(default=None, to='Mixed.Compound')),
                ('herbs', models.ManyToManyField(default=None, to='Mixed.Herb')),
                ('purchases', models.ManyToManyField(default=None, to='Mixed.Invoice')),
                ('seller', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Author')),
                ('targets', models.ManyToManyField(default=None, to='Mixed.Target')),
            ],
        ),
        migrations.AddField(
            model_name='mechanism',
            name='quotes',
            field=models.ManyToManyField(default=None, to='Mixed.Quotation'),
        ),
        migrations.AddField(
            model_name='herb',
            name='mechanisms',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Mechanism'),
        ),
        migrations.AddField(
            model_name='herb',
            name='reviews',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Review'),
        ),
        migrations.AddField(
            model_name='herb',
            name='side_effects',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Side_Effect'),
        ),
        migrations.AddField(
            model_name='function',
            name='quotes',
            field=models.ManyToManyField(default=None, to='Mixed.Quotation'),
        ),
        migrations.AddField(
            model_name='dosage',
            name='quotes',
            field=models.ManyToManyField(default=None, to='Mixed.Quotation'),
        ),
        migrations.AddField(
            model_name='compound',
            name='dosages',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Dosage'),
        ),
        migrations.AddField(
            model_name='compound',
            name='functions',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Function'),
        ),
        migrations.AddField(
            model_name='compound',
            name='mechanisms',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Mechanism'),
        ),
        migrations.AddField(
            model_name='compound',
            name='reviews',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Review'),
        ),
        migrations.AddField(
            model_name='compound',
            name='side_effects',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mixed.Side_Effect'),
        ),
        migrations.AddField(
            model_name='change',
            name='quotes',
            field=models.ManyToManyField(default=None, to='Mixed.Quotation'),
        ),
        migrations.CreateModel(
            name='Anon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_sort', models.IntegerField(choices=[(0, 'title'), (1, '-title'), (2, 'description'), (3, '-description'), (4, 'price'), (5, '-price'), (6, 'stock'), (7, '-stock'), (8, 'sale_qty'), (9, '-sale_qty')], default=0)),
                ('last_login_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cart', models.ManyToManyField(default=None, to='Mixed.Product')),
                ('purchases', models.ManyToManyField(default=None, to='Mixed.Invoice')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('whotheysent', models.ManyToManyField(default=None, to='Mixed.Author')),
            ],
        ),
    ]