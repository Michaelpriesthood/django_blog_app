from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from . forms import CommentForm

# Create your views here.
def home(request):
	post = Post.objects.all().order_by('-publish')
	paginator = Paginator(post, 5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	if page is None:
		start_index = 0
		end_index = 7
	else:
		(start_index, end_index) = proper_pagination(posts, index=4)

	page_range = list(paginator.page_range)[start_index:end_index]
	context = {
		'posts': posts,
		'page_range': page_range,
	}
	return render(request, 'blog/home.html', context)


def proper_pagination(posts, index):
    start_index = 0
    end_index = 7
    if posts.number > index:
        start_index = posts.number - index
        end_index = start_index + end_index
    return (start_index, end_index)


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



