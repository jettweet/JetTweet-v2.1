from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic import CreateView , UpdateView ,DeleteView
from django.urls import reverse , reverse_lazy
from .models import Article,Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .mixins import FieldMixin,FormValidMixin,AuthorAccessMixin
# Create your views here.
@login_required
def home(request):
	articles_list = Article.objects.all()
	paginator = Paginator(articles_list, 10)

	page = request.GET.get("page")
	articles = paginator.get_page(page)
	context = {
	'articles' :articles,
	'category':Category.objects.filter(status=True)
	}
	return render(request,'pages/index.html',context)




class PostDetail(LoginRequiredMixin,DetailView):
	model = Article
	template_name = 'pages/detail.html'
	context_object_name = 'article'




@login_required
def category(request,slug):
	context = {
	'category':get_object_or_404(Category,slug=slug,status=True),
	'categorys': Category.objects.all()
	}
	return render(request,'pages/category.html',context)

class ListArticle(LoginRequiredMixin,ListView):
	template_name = 'pages/list_article.html'
	def get_queryset(self):
		if self.request.user.is_superuser:
			return Article.objects.all()
		else:
			return Article.objects.filter(author=self.request.user)


class CreateArticle(LoginRequiredMixin,FieldMixin,FormValidMixin,CreateView):
	model = Article
	template_name = 'pages/create_article.html'
	success_url = reverse_lazy('home')

class ArticleUpdate(LoginRequiredMixin,AuthorAccessMixin,FieldMixin,FormValidMixin,UpdateView):
	model = Article
	template_name = 'pages/update_article.html'
	success_url = reverse_lazy('home')

class ArticleDeleteView(LoginRequiredMixin,AuthorAccessMixin,DeleteView):
    model = Article
    success_url = reverse_lazy("list")
    template_name = 'pages/delete_article.html'