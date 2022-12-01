# AQI_WebApp
Trying to pull information from an api json file then displaying the correct result to the user.


Lab Instructions
Lab #4 - Air Quality Index (AQI), Part 2

The goal of this activity is to develop a web application to inform the users about the weather conditions and air quality of the nearest city where the user is currently at. You will work on top of Lab #3. In that lab, you were asked to play with the Air Quality API provided by IQAir AirVisual. Please visit this website in case you need to get an API key to make requests for data. All you had to do in that lab was to request data from the AQI API. Now, you will develop a web application so the user can select what data they want to check.

We will use Flask framework to handle the backend of our application. Do remember that the HyperText Transfer Protocol (HTTP) is the protocol that we use for websites. The Internet uses it to make the interaction and communication among computers and servers possible.

In the previous lecture, we developed a web application that asks the user to select one of Curiosity's camera and displays pictures from Mars taken by this selected camera. You can definitely refer to the web app we develop in the previous lecture to do this activity.

I started most of the work for you, but only the parts that are repetitive and can serve as a template. I still need you to develop the most interesting components. Go ahead and download the template of the project in Python:

Project Template Download Project Template

Unzip the file and move folder AQI_WebApp to your PycharmProjects folder

Open PyCharm IDE and instead of creating a new project, simply open AQI_WebApp as a project

You will see the following structure:

here it had a picture with the folder structure viewed within pycharm

The main directory AQI_WebApp contains:

AQI_WebApp_Flask directory

venv directory

run.py script

The AQI_WebApp_Flask directory contains:

JSON_Files directory

static directory

templates directory

__init__.py script

forms.py script

main_functions.py script

routes.py script

JSON_Files directory contains:

aqi_key.json file

aqi_results.json file (AFTER MAKING THE API REQUEST)

static directory should contain optional CSS and JS files for styles purposes

templates directory contains:

parameter_result.html

parameter_search.html

Remember that the run.py script will execute the app created inside the __init__.py script. Then it will call the only function in routes.py, which in turn will make the interaction between client and server possible

Display an image file in parameter_result.html which is a screenshot of the city where the data was collected from

OPTIONAL: Dynamically display the city where the data was collected from using a Google Maps plugin

Once you are familiar with the structure of this project, add your API key from the AQI API inside the file aqi_key.json

Visit forms.py and complete the function named aqi_parameter. This function should return a dictionary as follows:

parameters = {'coordinates': coordinates,

              'temperatureC': str(temperatureC),

              'pressure': str(pressure),

              'humidity': str(humidity),

              'aqius': str(aqius)}

Your goal is to make the api request, save the requested data as a json file, and read from this json file only the values above

Next, still in forms.py script, complete the class AQIParameters with the right choices for the dropdown menu

The following step is to go back to routes.py and complete the search function to render the correct templates

Now, play with both html files to make the interface a little bit better, giving instructions to the user and providing a better response with the requested data.
