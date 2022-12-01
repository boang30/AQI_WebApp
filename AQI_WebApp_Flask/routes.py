from AQI_WebApp_Flask import app, forms
from flask import request, render_template


@app.route('/', methods=['GET', 'POST'])
def search():
    searchForm = forms.AQIParameters(request.form)
    if request.method == "POST":

        parameters_requested = request.form['aqiparameter']
        aqi_parameter = forms.aqi_parameter()

        '''
        If the user makes a post request, please save the selected value by the user into a variable
        Also, call the function aqi_parameter (from forms.py) with all the results
        Then, render template parameter_result.html only with the parameter requested by the user
        Which means that you should assign the correct value for the variable parameter_requested below
        '''

        return render_template('parameter_result.html', result=parameters_requested, aqi_parameter=aqi_parameter)
    return render_template('parameter_search.html', form=searchForm)
