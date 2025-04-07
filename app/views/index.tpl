<!DOCTYPE html>
<html>
  <head>
<!-- ___________________________ Metatags __________________________ -->
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name=viewport content="width=device-width, initial-scale=1">
    <title>Bottle base template</title>
    <meta name="author" content="Rockdukan">
    <meta name="description" content="Базовый шаблон проекта на фреймворке Bottle">

<!-- _____________________________ CSS _____________________________ -->
    <link rel="stylesheet" href="/static/css/style.css">
    
<!-- ______________________ If Internet Explorer ___________________ -->
    <script>
        if (/Trident\/|MSIE/.test(window.navigator.userAgent)) {
            alert("Ваш браузер не поддерживается!!!");
        }
    </script>
  </head>
  <body>
<!-- ______________________________ CONTENT ________________________ -->
    <main>
      <div class="container">
        <h1>Добро пожаловать в Bottle-приложение.</h1>
        <a class="button" href="/api/ping">Test API</a>
      </div>
    </main>
<!-- ____________________________ END_CONTENT ______________________ -->

<!-- ____________________________ JavaScript _______________________ -->
    <script src="/static/js/scripts.js"></script>
  </body>
</html>
