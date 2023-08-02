from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging

from .models import Author, Article, Commentary

logger = logging.getLogger(__name__)


# def index_old(request):
#     logger.info(f'Index accessed')
#     html = """<html>
#     <head><title>Index page</title></head>
#     <body>
#     <div><h2>Site Start Page</h2></div>
#         <div>
#             <ul>Simple Games
#                 <li><a href="games">Games Page</a></li>
#             </ul>
#         </div>
#         <footer>
#         <a href="">Main</a>&nbsp;&nbsp;&nbsp;
#         <a href="about/">About</a>
#         </footer>
#     </body>
#     </html>
#     """
#     return HttpResponse(html)
#
#
# def about_old(request):
#     logger.info(f'About accessed')
#     html = """<html>
#     <head><title>About page</title></head>
#     <body>
#     <div><h2>Site About Page</h2></div>
#          <div>
#           <p><strong>Lorem ipsum</strong> dolor sit amet, consectetur adipisicing elit.
#           Ab amet blanditiis dolores laudantium maiores, nulla quas
#           repudiandae saepe. A aspernatur consectetur dolore est illo nam
#           necessitatibus nostrum nulla numquam tempora! Culpa delectus dolorem,
#           dolorum ea eos eveniet facilis fugiat illo illum in ipsum minima
#           neque odit perferendis porro quaerat quia quibusdam quo quod
#           reiciendis repudiandae saepe similique, temporibus vel
#           voluptate. Aut beatae doloremque fugiat laboriosam magni,
#           optio qui quia recusandae ut veritatis. Commodi, culpa dignissimos
#           doloribus est et illo, ipsa laboriosam laborum molestias natus nemo
#           odit officiis placeat sequi sunt veniam, voluptas!
#           At ea ex odit placeat sunt? Assumenda, tenetur!</p>
#         </div>
#         <footer>
#         <a href="/">Main</a>&nbsp;&nbsp;&nbsp;
#         <a href="">About</a>
#         </footer>
#     </body>
#     </html>
#     """
#     return HttpResponse(html)


def index(request):
    logger.info(f'Index accessed')
    context = {"title": "Index page"}
    return render(request, "app001/index.html", context=context)


def about(request):
    logger.info(f'About accessed')
    context = {"title": "About page"}
    return render(request, "app001/about.html", context=context)


def get_articles(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {
        "author": f'{author.name} {author.surname}',
        "articles": Article.objects.filter(author=author),
    }
    return render(request, 'app001/authors_records.html', context=context)


def get_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    author = get_object_or_404(Author, pk=article.author.pk)
    article.views += 1
    article.save()
    commentaries = Commentary.objects.filter(article=article).all()
    context = {
        'article': article,
        'author': author,
        'commentaries': commentaries,
        }
    return render(request, 'app001/article.html', context=context)

