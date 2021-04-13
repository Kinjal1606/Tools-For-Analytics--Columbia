This is the final project for IEOR 4501 Tools for Analytics 

Owners of this project are Kinjal Saxena (uni ks3851) and Neha Vibhu Hajela (uni nh2675) 

Description: This is a web application designed in Django Framework to track all known squirrels in Central Park. It has imported the 2018 Central Park Squirrel census data and allows to add, update and view squirrel data. 

Features: 

Management Commands: 

Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command. 
$ python manage.py import_squirrel_data /path/to/file.csv

Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command. 
$ python manage.py export_squirrel_data /path/to/file.csv

Map: 
A view to show the location of squirrel sightings on an OpenStreets map is located at \map

List: 
List of all squirrel sightings with links to view each sighting is available and located at \sightings 

Update: 
Sightings of a particular squirrel can be updated and located at /sightings/<unique-squirrel-id>

Add:
New squirrels sighted  can be added and located at /sightings/add

Stats: 
General stats about the squirrel sightings are available at /sightings/stats

Website: 
https://tfa-2021-spring-nh2675.uk.r.appspot.com/
 



# Tools-For-Analytics--Columbia
