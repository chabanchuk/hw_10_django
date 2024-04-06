from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import QuoteForm, AuthorForm
from .models import Quote, Author
from django.db.models import Count
from django.contrib.auth.decorators import login_required


# Create your views here.
def main(request):
    quote_list = Quote.objects.all()
    paginator = Paginator(quote_list, 4) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    top_tags = Quote.objects.exclude(tags__exact=[]).values('tags').annotate(tag_count=Count('id')).order_by('-tag_count')[:10]

    formatted_top_tags = list(set(tag for sublist in top_tags for tag in sublist['tags'] if tag))

    return render(request, 'toscrape_app/index.html', {'page_obj': page_obj, 'top_tags': formatted_top_tags})

@login_required
def quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('toscrape_app:main')
    else:
        form = QuoteForm()
    return render(request, 'toscrape_app/quotes.html', {'form': form})

@login_required
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('toscrape_app:main')
    else:
        form = AuthorForm()
    return render(request, 'toscrape_app/authors.html', {'form': form})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'toscrape_app/author_detail.html', {'author': author})

def tag_quotes(request, tag):
    quotes = Quote.objects.filter(tags__contains=[tag])
    paginator = Paginator(quotes, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'toscrape_app/index.html', {'page_obj': page_obj, 'tag': tag})