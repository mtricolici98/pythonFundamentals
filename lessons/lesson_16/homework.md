# Homework

## IMPORTANT

If you want to upload your project to GitHub, please save the credentials (example the API Keys) in a separate file, and
don't upload that file to GitHub.

## Ex1

Using The [Google translate API](https://rapidapi.com/googlecloud/api/google-translate1)

Create an application that will translate text.

Application should prompt the user for the target language from a list of options. (You decide what the options are)

Application should allow user to input any length text, or can provide a path to a file (textual file to translate)

Write the code as a library, this way you can have functions such as:

* get_all_languages
* translate(text, to_language)
* translate_file(path, to_language)

## Ex2: Optional

Use a combination of 2 WEB APIs, to create an application that will find the country and city using the
IP [Example](https://rapidapi.com/xakageminato/api/ip-geolocation-ipwhois-io/) and will show the weather
data [using this](https://rapidapi.com/community/api/open-weather-map).

The program should automatically detect the location and display the weather when started.

It should show:

* City, Country
* Temperature (celsius)
* Weather (example: Cloudy/Clear/Snowing/Raining)