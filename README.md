WEBCACHE REFACTOR PROJECT
=========================

2 hours is very short time for such a big task.
I guess it's because You want to see on which topics, I will focus
For me most important is:
- good dev (and production deploy setup) - that's why i move to docker
- good architecture - that's why I refactor all names and dirs
- clean architecture - classes doing one thing and one thing only.
  Creating separate Service for handling ulrs, db, proxies etc.
  Having separation between logic, services, and views. View should
  only validate request, call specific service and parser answer,
  sometimes raise error :)
- having tests -> integration tests over unit tests

WHAT I MANAGE IN 2 HOURS
------------------------

0. Write this README
1. Creating docker deploy
2. Creating new architecture
3. Moving from flask to lightweight async framework
3. Refactor basic function - see common, helpers
4. Creating RequestService which will ask for responses (see up
   one class doing one thing). RequestService use corutines.
   On top of RequestService should be WebCacheUrlHandler which
   will ask for response (using RequestService) and handle all
   logic (higher abstract class handle logic, lower class
   just do stuff -> separate logic = good architecture).
5. Run deploy and basic test it - return hello world :D
6. No time for writing tests - now I have RequestService so I'm
   able to write unit tests, and after creating one endpoint
   integration tests.
7. Sometimes is better to demolish a ruined building than to
   renovate it, in some cases it's faster option (paradox :D)
  
HOW TO SEE SOMETHING WORKING
---------------------------

Run service:

    $ docker-compose build
    $ docker-compose up
    
    $ curl 0.0.0.0:8080/hello_world

Check RequestService:

    - uncomment code on bottom 
    (its just to test, use it for simple fast verification,
    only 2 hours)
