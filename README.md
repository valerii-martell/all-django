# All Django

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/aacdb4d99f3c4fbfb89f83e84854045f)](https://www.codacy.com/gh/valerii-martell/all-django/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=valerii-martell/all-django&amp;utm_campaign=Badge_Grade)

http://all-django-dev.us-east-1.elasticbeanstalk.com/ (currently suspended)

An index project that contains a set of examples of implementation of various functionalities of a modern web service in Django. Can be used as a cheat sheet and as a basis for building a course for teaching web backend development using Django as an example.
All considered topics are implemented within the set of separated applications. Among them:

 - Smoke - Classical smoke page
 - Routing - app-level routing, parametrised requests, different types of responses, handling subdomains in Django level.
 - Views - different types of Django views, function-based and class-based views
 - Templates - Django Templates, tags, creating custom tags, filters, etc. Working with Jinja2 alongside Django Templates.
 - Models - working with Django Models and their different fields
 - ORM - working with Django ORM, different entities relations, multiple DB (SQLite, PostgreSQL, MySQl), DB routers, migrations.
 - API - organizing API using Django REST Framework. Function-based API views, class-based API views, ViewSets, Generic API views. Token-based authentication. Swagger UI API docs.
 - Custom user - base User model customization (Proxy, Profile, AbstractUser and AbstractBaseUser)
 - Custom admin panel - customization of a built-in admin panel, it's fields and styles
 - AJAX - handling AJAX requests/responses in Django
 - Frontend - realization of simple frontend using Django Templates and Bootstrap, dealing with static files and media files
 - Emails - sending complicated email template with media files and styles. Email broadcast subscription using MailChimp. User email confirmation and account activation during registration. User's password reset via email.
 - GraphQL - organizing API using GraphQL and Graphene. All types of queries, related models, mutations, token-based authentication, dynamic user registration via GraphQL mutations.
 - Celery (with Redis or RabbitMQ) - different scheduled and repeated(beat) tasks - heavy calculations, generating big number of data, user-session clearing.
 - Channels (with Redis and Websockets) - dealing with Django channels with an example of websocket-based live chat.
 - Linting - controlling codestyle using flake8, fixing it using Black
 - Testing - Django tests based on pytest. Unittests, mocks, abstract tests, API tests, GraphQL tests via graphene
 - Security - examples of different attacks (XSS, SQL-injection, CSRF) and protection against them
 - Containerization - dockerizing Django application using Docker and docker-compose
 - Deploy - Nginx/Apache2, Let's Encrypt, Gunicorn and Uvicorn for ASGI Channels, AWS EC2/EBT (currently suspended)

