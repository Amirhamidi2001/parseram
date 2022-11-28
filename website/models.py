from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    parent = models.ForeignKey(
        'self',
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='child'
    )

    def __str__(self):                           
        full_path = [self.title]            
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent

        return ' -> '.join(full_path[::-1])


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='website/',default='website/default.jpg')
    content = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    description = models.TextField(null=True)
