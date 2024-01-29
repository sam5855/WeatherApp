from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=F85CCA0F-8B73-4B5F-AB45-EDCDBC2844E0")
        
        #Error when searching zip 43788. Has to do with If statements. Anything past "good" results in an error. 
        #43788 is hardcoded in api call below to test. 
        #api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=43788&distance=25&API_KEY=F85CCA0F-8B73-4B5F-AB45-EDCDBC2844E0")

        try:
            api = json.loads(api_requests.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little to no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Air quality is acceptable. However, for some pullutants there may be a moderate health concern."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101 - 150) People with lung disease, older adults, and children are at increasesed risk."
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Everyone may begin experiencing health effects."
            category_color =  "unhealthy"    
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Everyone may experience serious health effects."
            category_color = "very-unhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301 - 500) You are dead."
            category_color = "hazardous"
        


        return render(request, 'home.html', {
            'api': api,
            'category_description': category_description, 
            'category_color': category_color
            } )
    else:
        api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=32724&distance=25&API_KEY=F85CCA0F-8B73-4B5F-AB45-EDCDBC2844E0")

        try:
            api = json.loads(api_requests.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little to no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Air quality is acceptable. However, for some pullutants there may be a moderate health concern."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101 - 150) People with lung disease, older adults, and children are at increasesed risk."
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Everyone may begin experiencing health effects."
            category_color =  "unhealthy"    
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Everyone may experience serious health effects."
            category_color = "very-unhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301 - 500) You are dead."
            category_color = "hazardous"
        


        return render(request, 'home.html', {
            'api': api,
            'category_description': category_description, 
            'category_color': category_color
            } )

def about(request):
    return render(request, 'about.html', {})

