from django.db import models
from accounts.models import User
from django.utils import timezone
from extensions.utils import jalali_converter

from django.contrib.contenttypes.fields import GenericRelation

from comment.models import Comment

class Category(models.Model):
	title = models.CharField(max_length=200,verbose_name="عنوان دسته بندی")
	slug = models.SlugField(max_length=100,unique=True,verbose_name="ادرس دسته بندی")
	status = models.BooleanField(default=True,verbose_name="آیا می خواید نمییش داداه شود؟")
	position = models.IntegerField(verbose_name="پوزیشن")
	class Meta:
		verbose_name="دسته بندی"
		verbose_name_plural = "دسته بندی ها"
		ordering = ['position']
	def __str__(self):
		return self.title



class Article(models.Model):
	post = models.CharField(max_length = 200,unique=False,verbose_name='عنوان')
	description = models.TextField(max_length = 1000,unique=False,verbose_name='مقاله ی پست',null=True,blank=True)
	pictures = models.ImageField(upload_to="images/",unique=False,verbose_name='عکس برای پست',null=True,blank=True)
	category = models.ManyToManyField(Category,verbose_name='دسته بندی',related_name='articles',null=True,blank=True,)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	private = models.BooleanField(default=False,verbose_name="...خصوصی")
	video = models.FileField(upload_to='video/',verbose_name="ویدیو",null=True,blank=True)
	video_not_music = models.FileField(upload_to='video/',verbose_name="استیکر",null=True,blank=True)
	comments = GenericRelation(Comment)
	





	def __str__(self):
		return self.post
	class Meta:
		verbose_name="پست"
		verbose_name_plural = "پست ها"
		ordering =['-publish']
	def category_published(self):
		return self.category.filter(status=True)
	
	def jpublish(self):
		return jalali_converter(self.publish)
	jpublish.short_description = "زمان انتشار پست"

	def category_to_str(self):
		return " ".join([category.title for category in self.category.all()])
	category_to_str.short_description = 'دسته بندی'
	

