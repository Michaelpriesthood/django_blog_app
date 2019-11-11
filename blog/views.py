from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from . forms import CommentForm

# Create your views here.
def home(request):
	post = Post.objects.all().order_by('-publish')
	page = request.GET.get('page', 4)
	paginator = Paginator(post, 4)
	try:
		post_list = paginator.page(page)
	except PageNotAnInteger:
		post_list = paginator.page(1)
	except EmptyPage:
		post_list = paginator.page(paginator.num_pages)
	context = {
		'post_list':post_list
	}
	return render(request, 'blog/home.html', context)

def post_details(request, pk):
	posts = get_object_or_404(Post, pk=pk)
	comments = posts.comments.filter()
    # Comment posted
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = posts
			comment_form.save() # Save the comment to the database       
	comment_form = CommentForm()

	context = {
		'posts': posts,
		'comments' :comments,
		'comment_form': comment_form,	
		
	}

	return render(request, 'blog/post_details.html', context)



