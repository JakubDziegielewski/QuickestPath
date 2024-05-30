# QuickestPath
Project for SPDB course at WUT

## How to test the app

0. Requirements:
    -Python >=3.10
    -networkx >=3.10 
    -pyrosm
    -geopandas
    -django 4.1
    -numpy

1. git clone https://github.com/JakubDziegielewski/QuickestPath.git

2. cd QickestPath/application

3. python manage.py makemigrations

4. python manage.py migrate

5. python manage.py runserver

6. Wait until the application starts

7. Go to 127.0.0.1:8000 in your browser

8. Enter your starting address (Remember that all your addresses should be in Warsaw agglomeration)

9. Add more addresses for path searching

10. Click on the 'find route' button and wait for the application to draw the path on the map
