from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='Title')
    sub_title = models.CharField(max_length=200,verbose_name='Sub Title')
    content = models.TextField(verbose_name='Content')
    image = models.ImageField(upload_to='images/', default='images/imagen_default.jpg', verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Category')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']

    def __str__(self):
        return self.title