import logging
from datetime import datetime
from django.http import HttpResponse

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='log.log', filemode='a', format='%(levelname)s %(message)s')


def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <style>
        * {
            margin: 0;
            padding: 0;
        }
        
        
        
        .header {
            height: 100px;
            background-color: #9dff00;
            margin-bottom: 150px;
        
        }
        
        .content{
            display: flex;
        }
        
        .item {
            width: 352px;
            height: 500px;
            
        }
        
        .footer {
            height: 100px;
            background-color: #989eae;
            margin-top: 150px;
        }
        
        .container {
            width: 1200px;
            margin: 0 auto;
        }
        
        .item-flex {
            display: flex;
            justify-content:space-around;
            height: 500px;
            align-items: center;
        }

        .nav-item Enter {
            color: red;
        }
    </style>
</head>
    <body>
<div class="wrapper">
    <nav class="navbar navbar-expand-lg navbar-light bg-light navbar-dark bg-dark">
        <a class="navbar-brand" href="/">Мой первый сайт на Django</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item active">
              <a class="nav-link" href="/">Главная</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/about">О себе</a>
            </li>
          </ul>
        </div>
      </nav>
</div>
    <div class="container">  
   <br>
       </div>   
    <div class="container">
            <h1 style="text-align: center;"><span style="font-size: 36pt;">Главная</span></h1>
            <br>
           <center> <img src="https://www.techlifediary.com/wp-content/uploads/2017/08/django.jpg"/></center>    
    </div>
</div> 
    <div class="footer">
      <div class="container">
          All rights reserved (c)
      </div>
    </div>
    </div>
    </div>
    </body>
    </html>
    """
    logger.info(f'Index page accessed: {datetime.now()}')
    return HttpResponse(html)


def about(request):
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <style>
        * {
            margin: 0;
            padding: 0;
        }
        
        
        
        .header {
            height: 100px;
            background-color: #9dff00;
            margin-bottom: 150px;
        
        }
        
        .content{
            display: flex;
        }
        
        .item {
            width: 352px;
            height: 500px;
            
        }
        
        .footer {
            height: 100px;
            background-color: #989eae;
            margin-top: 150px;
        }
        
        .container {
            width: 1200px;
            margin: 0 auto;
        }
        
        .item-flex {
            display: flex;
            justify-content:space-around;
            height: 500px;
            align-items: center;
        }

        .nav-item Enter {
            color: red;
        }
    </style>
</head>
    <body>
<div class="wrapper">
    <nav class="navbar navbar-expand-lg navbar-light bg-light navbar-dark bg-dark">
        <a class="navbar-brand" href="/">Мой первый сайт на Django</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item active">
              <a class="nav-link" href="/">Главная</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/about">О себе</a>
            </li>
          </ul>
        </div>
      </nav>
</div>
    <div class="container">  
   <br>
       </div>   
    <div class="container">
            <h1 style="text-align: center;"><span style="font-size: 36pt;">О себя</span></h1>
            <br>
           <center> <img src="https://safebooru.org//images/1890/1e6d3595f92e3d739fbd5d3a4164786441ad91b7.gif?1972247"/></center>    
    </div>
</div> 
    <div class="footer">
      <div class="container">
          All rights reserved (c)
      </div>
    </div>
    </div>
    </div>
    </body>
    </html>
    """
    logger.info(f'{request} request received')
    return HttpResponse(html)