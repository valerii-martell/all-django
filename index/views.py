from django.http import HttpResponse


def index(request):
    _html = """
    <html>
        <head>
            <title>
                All Django
            </title>
        </head>
        <body>
            <h1>Index:</h1>
            <p><a href="/smoke">001. Smoke</a></p>
            <p><a href="/routing">002. Routing</a></p>
            <p><a href="/views">003. Views</a></p>
            <p><a href="/templates">004. Templates</a></p>
            <p><a href="/models">005. Models</a></p>
            <p><a href="/forms">006. Forms</a></p>
            <p><a href="/orm">007. Django ORM</a></p>
            <p><a href="/authentication">008. Authentication</a></p>
            <p><a href="/ajax">009. AJAX</a></p>
            <p><a href="/api">010. API via Django REST Framework</a></p>
            <p><a href="/security">011. Security</a></p>
            <p><a href="/custom-user">012. Custom user models</a></p>
            <p><a href="/custom-admin">013. Custom Admin panel</a></p>
            <p><a href="/frontend">014. Frontend</a></p>
            <p><a href="/emails">015. Emails</a></p>
            <p><a href="/graphql">016. GraphQL</a></p>
        </body>
    </html>
    """
    return HttpResponse(_html)
