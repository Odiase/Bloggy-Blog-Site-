from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    category_choices = (
       ("anime","anime"),
       ("beauty","beauty"),
       ("business & finance", "business & finance"),
       ("education","education"),
       ("entertainment","entertainment"),
       ("fashion","fashion"),
       ("food","food"),
       ("government & Politics","government & politics"),
       ("lifestyle","lifestyle"),
       ("movies","movies"),   
       ("music","music"),
       ("others","others"),
       ("relationships","relationships"),
       ("religion","religion"),
       ("sports","sports"),
       ("technology","technology"),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "blogs")
    title = models.CharField(max_length=300)
    category = models.CharField(choices = category_choices, max_length =50)
    featured_image = ResizedImageField(size = [320,280],upload_to = "blog_images", force_format = "jpeg", quality = 100, blank = True,  null = True)
    created = models.DateTimeField(auto_now_add = True, editable=False)
    updated = models.DateTimeField(auto_now = True, editable=False)
    body = RichTextField()
    slug = models.SlugField(unique = True, max_length = 200)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
    
    @property
    def blog_comments(self):
        return self.comments.all()
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Blog, self).save(*args, **kwargs) # calling the main save method on this instance


class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete = models.CASCADE,related_name = "comments")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "my_comments")
    message = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add = True,blank = True, null = True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.blog.title + " comment"