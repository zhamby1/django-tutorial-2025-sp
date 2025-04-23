#we can import a cool feature in django
#so far we have grabbed a list of all posts...in this case no posts are really missing or not there
#ie if i want to see post 10 and there is no post 10 there will be an error, and we need to render an error page
#get_object_or_404 will render the object or a 404 error/page
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
#views is used to handle requests and provide a response
#we take t request information, and handle it in some way
#then we fetch the information (if needed) from the database to then send to a HTML page
#finally, we create a response to send back to the client

#everything in our views file takes in a request as an argument
def post_list(request):
    #return a response..the response will return a render of the request back to the user (in the form of a code)
    #tell you the template or html page to go to and any data that needs to be passed to that html page

    #when we want to query to the database, we first query it and set it to a variable
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    #get object 404 only works when grabbing a single item
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    #this is a HTTP method NOT the Post class/model/tabel
    #POST in HTTP means to add something to a database
    #GET is to grab
    #PUT - Updated Existing
    #DELETE - Delete something from DB
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})



def post_edit(request, pk):
    #grab post to edit
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        #instace=post makes sure we are changing an existing post and not making a new one
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        #pre-fill out text boxes with all the info from our database entry for this particular post
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})