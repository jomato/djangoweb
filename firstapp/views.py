from django.shortcuts import render, HttpResponse, get_object_or_404
from firstapp.models import People, Artical, Category
from django.template import Context, Template
from comments.forms import CommentForm
import markdown

# Create your views here.


def first_try(request):
    person = People(name='Spock', job='officer')
    html_string = '''
            <html>
                <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.6/semantic.css" media="screen" title="no title">
                    <title>firstapp</title>
                </head>
                <body>
                    <h1 class="ui center aligned icon header">
                        <i class="hand spock icon"></i>
                        Hello, {{ person.name }}
                    </h1>
                </body>
            </html>

        '''
    t = Template(html_string)
    c = Context({'person': person})
    web_page = t.render(c)
    return HttpResponse(web_page)


def index(request):
    context = {}
    artical_list = Artical.objects.all().order_by('-modified_time')
    context['artical_list'] = artical_list
    return render(request, 'first_web_2.html', context)


def detail(request, pk):
    post = get_object_or_404(Artical, pk=pk)
    post.content = markdown.markdown(post.content, extensions=['markdown.extensions.extra',
                                                               'markdown.extensions.codehilite',
                                                               'markdown.extensions.toc',
                                                               ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }
    return render(request, 'detail.html', context)


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    artical_list = Artical.objects.filter(category=cate).order_by('-modified_time')
    return render(request, 'categories.html', context={'artical_list': artical_list})


def archives(request, year, month):
    artical_list = Artical.objects.filter(created_time__year=year, created_time__month=month).order_by('-modified_time')
    return render(request, 'first_web_2.html', context={'artical_list': artical_list})

























