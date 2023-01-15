# Generated by Django 4.1.5 on 2023-01-15 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0010_remove_order_book_title_order_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='book',
            new_name='book_title',
        ),
        migrations.AddField(
            model_name='order',
            name='book_price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book_price', to='Bookstore.book'),
        ),
    ]
