from django.shortcuts import render, redirect
from .models import Community, Post, Image, Comment
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
import ast
from django.contrib.auth.models import User 

# Create your views here.
def groups(request):
    context = {}
    user = request.user
    if user.is_active:
        print(user)
        # context['groups'] = user.community_set.all()
        total_groups = Community.objects.filter(user=user).count()
        group_count = []
        for group in user.community_set.all():
            group_count.append((group, group.user.count()))
        context['groups'] = group_count
        context['tot_groups'] = total_groups
    return render(request, 'groups.html', context)

def not_joined(request):
    context = {}
    user = request.user
    if user.is_active:
        total_groups = Community.objects.filter(~Q(user = user))
        group_count = []
        for group in total_groups:
            group_count.append((group, group.user.count()))
        context['groups'] = group_count
        context['tot_groups'] = total_groups
    return render(request, 'unfollowed_groups.html', context)

def join_group(request, pk):
    context = {}
    context['valid'] = True
    user = request.user
    if user.is_active:
        try:
            group = Community.objects.get(id=pk)
            group.user.add(user)
            context['group'] = group
            context['users'] = group.user.all()
        except:
            context['valid'] = False
    return redirect('share:detail_group_user', pk=pk)

def detail_group_user(request, pk):
    context = {}
    context['valid'] = True
    user = request.user
    context['group_id'] = pk
    if user.is_active:
        try:
            group = Community.objects.get(id=pk)
            context['group'] = group
            all_words = []
            user_words = []
            for user in group.user.all():
                words = user.word_set.all()
                user_words.append((user, words.count()))
                meaning = []
                for word in words:
                    meaning = []
                    temp = ''
                    for mean in word.meaning_set.all():
                        temp = mean.pos
                        meaning.append((ast.literal_eval(mean.meaning), temp))
                    all_words.append((word, meaning))
            context['users'] = user_words
            context['words'] = all_words
        except:
            context['valid'] = False
    return render(request, 'group_detail_user.html', context)

def detail_group_wordwall(request, pk):
    context = {}
    context['valid'] = True
    user = request.user
    context['group_id'] = pk
    if user.is_active:
        try:
            group = Community.objects.get(id=pk)
            context['group'] = group
            all_words = []
            user_words = []
            for user in group.user.all():
                words = user.word_set.all()
                user_words.append((user, words.count()))
                meaning = []
                for word in words:
                    meaning = []
                    temp = ''
                    for mean in word.meaning_set.all():
                        temp = mean.pos
                        meaning.append((ast.literal_eval(mean.meaning), temp))
                    all_words.append((word, meaning))
            context['users'] = user_words
            context['words'] = all_words
        except:
            context['valid'] = False
    return render(request, 'group_detail_wordwall.html', context)


def create_post(request, pk):
    user = request.user
    context = {}
    if user.is_active:
        if request.method == 'POST':
            title = request.POST['title']
            text = request.POST['text']
            context['group'] = pk
            try:
                group = Community.objects.get(id=pk)
                post = Post.objects.create(user=user, group=group, title=title, text=text)
                for i in range(1, 7):
                    try:
                        name = 'image-' + str(i)
                        image = request.FILES[name]
                        Image.objects.create(post=post, image=image)
                    except:
                        break
            except:
                pass
    return render(request, 'create_post.html', context) 


def list_posts(request, pk):
    context = {}
    user = request.user
    if user.is_active:
        url = reverse('share:list_posts', args=[str(pk)])
        if request.method == "POST":
            user = request.user
            pk = request.POST["index"]
            post = Post.objects.get(id=pk)
            if user in post.likes.all():
                post.likes.remove(user)
            else:
                post.likes.add(user)
            return HttpResponseRedirect(url)
        else:
            group = Community.objects.get(id=pk)
            print(group)
            posts = group.post_set.all()
            print(posts)
            collection = []
            for post in posts:
                image = post.image_set.all()
                content = post.text
                context_temp = ''
                likes = post.likes.all().count()
                if len(context) > 50:
                    context_temp = content[:50] + '...'
                if image:
                    collection.append((post, image[0], content[:50], likes))
            print(collection)
            context['posts'] = collection
            context['group'] = group
    return render(request, 'post-listings.html', context)


def detail_post(request, pk):
    context = {}
    context['pk'] = pk
    user = request.user
    if user.is_active:
        post = Post.objects.get(id=pk)
        if request.method == 'POST':
            comment = request.POST['comment']
            Comment.objects.create(post=post, content=comment, user=user)
        comments = Comment.objects.all().filter(post=post).order_by('-timestamp')
        likes = post.likes.count()
        images = post.image_set.all()
        context['post'] = post
        context['comments'] = comments
        context['likes'] = likes
        context['images'] = images
    return render(request, 'post-detail.html', context)

def comment_like(request, cpk, ppk):
    context = {}
    context['cpk'] = cpk
    context['ppk'] = ppk
    user = request.user
    if user.is_active:
        if request.method == "POST":
            comment = Comment.objects.get(id=cpk)
            if user in comment.likes.all():
                comment.likes.remove(user)
            else:
                comment.likes.add(user)
    return HttpResponseRedirect(reverse('share:detail_post', args=[str(ppk)]))

def user_detail(request, pk):
    user = User.objects.get(id=pk)
    context = {}
    context['words'] = []
    context['user'] = user
    if user.is_active:
        temp = []
        for word in user.word_set.all():
            temp2 = []
            for mean in word.meaning_set.all():
                temp2.append((mean.pos, ast.literal_eval(mean.meaning)))
            temp.append((word, tuple(temp2)))
        context['words'] = temp
        for c in context['words']:
            print(c)
    return render(request, 'user_detail.html', context)

        
