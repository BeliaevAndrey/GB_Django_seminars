from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'Index accessed')
    html = """<html>
    <head><title>Index page</title></head>
    <body>
    <div><h2>Site Start Page</h2</div>
        <div>
            <ul>Simple Games
                <li><a href="games">Games Page</a></li>
            </ul>
        </div>
        <footer>
        <a href="">Main</a>&nbsp;&nbsp;&nbsp;
        <a href="about/">About</a>
        </footer>
    </body>
    </html>
    """
    return HttpResponse(html)


def about(request):
    logger.info(f'Index accessed')
    html = """<html>
    <head><title>About page</title></head>
    <body>
    <div><h2>Site About Page</h2></div>
         <div>
          <p><strong>Lorem ipsum</strong> dolor sit amet, consectetur adipisicing elit. 
          Ab amet blanditiis dolores laudantium maiores, nulla quas 
          repudiandae saepe. A aspernatur consectetur dolore est illo nam 
          necessitatibus nostrum nulla numquam tempora! Culpa delectus dolorem, 
          dolorum ea eos eveniet facilis fugiat illo illum in ipsum minima 
          neque odit perferendis porro quaerat quia quibusdam quo quod 
          reiciendis repudiandae saepe similique, temporibus vel 
          voluptate. Aut beatae doloremque fugiat laboriosam magni, 
          optio qui quia recusandae ut veritatis. Commodi, culpa dignissimos
          doloribus est et illo, ipsa laboriosam laborum molestias natus nemo 
          odit officiis placeat sequi sunt veniam, voluptas!
          At ea ex odit placeat sunt? Assumenda, tenetur!</p>
        </div>
        <footer>
        <a href="/">Main</a>&nbsp;&nbsp;&nbsp;
        <a href="">About</a>
        </footer>
    </body>
    </html>
    """
    return HttpResponse(html)
