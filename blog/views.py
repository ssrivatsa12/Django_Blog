from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
from django.template.loader import render_to_string
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.views.generic import ListView
from django.views.generic import View
from api.serializers import PostSerializer 
from . import models
from api.views import PostViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@method_decorator(login_required, name='dispatch')
class PostList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blog/post_list.html'
    permission_classes = (IsAuthenticated,) 

    def get(self, request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return Response({'posts': posts})


@method_decorator(login_required, name='dispatch')
class PostDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blog/post_detail.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response({'serializer': serializer, 'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'post': post})
        serializer.save()
        return redirect('post_list')


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def post_new(request):
	if request.method == "POST":
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(author=request.user, published_date=timezone.now())
			return JsonResponse(serializer.data)

		return Response(serializer.errors, status=400)

@login_required
@api_view(["GET,POST"])
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_delete(request,pk):
	if request.method == "POST":
		Post.objects.filter(pk=pk).delete()
	messages.success(request, "Post Successfully Deleted")
	return redirect('post_list')

@login_required
def post_dropdown(request):
	if request.method == "POST":
		vn = request.POST.get('sel')
		if vn == 'old':
			posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
			return render(request, 'blog/post_list.html', {'posts': posts})	
		elif vn == 'new':
			posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
			return render(request, 'blog/post_list.html', {'posts': posts})
		else:
			pass
	return redirect('post_list')

@login_required
def post_search(request):
	query = request.GET.get('q')
	submitbutton= request.GET.get('submit')
	if query is not None:
		results= Post.objects.filter(Q(title__icontains=query)|Q(text__icontains=query)|Q(published_date__icontains=query)).distinct()
		context={'results': results, 'submitbutton': submitbutton}
		return render(request, 'blog/post_list.html', context)
	else:
		return redirect('post_list')







		
