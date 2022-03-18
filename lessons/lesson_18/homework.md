# Homework

[conversions.json](conversions.json)

Use your code from one of your homeworks with the currency conversion programs, and make a flask application that will
do the following.

1. have a route /conversions/list - GET only, that will return all conversions
2. have a route /conversions/get/<currency> - GET only, that will return conversion rates for that conversion
3. have a route /convert - POST only, that will take the following JSON format as request data
    ```json
     {"from": "MDL","to": "eur", "amount": 1000}
     ```
   And will return the converted value

Bonus points:

1. Try to save all the requested conversions in a separate files (call it history.json)

Notes:

When working with files in flask, `open('file.json')` will point to a location in a different place that you expect,
this is why either use absolute paths, ex: `C:\data\conversions.json` or use something like you can
see [here](https://github.com/mtricolici98/courseAssignmentLiveCoding/blob/master/config.py) with usages
examples [here](https://github.com/mtricolici98/courseAssignmentLiveCoding/blob/master/services/file/FileService.py#L4).

