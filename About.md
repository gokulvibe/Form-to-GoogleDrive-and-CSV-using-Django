## The workflow of the project:
1. The front end is a HTML form decorated using Bootstrap.
2. The data collected through the form are Username, user location (using geolocation), 5 text fields, 5 image fields.
3. The data is stored to SQLlite3 data base locally.
4. Then a folder is created on Google Drive using the Google Drive API, to store the particular user's images.
5. Then the images are fetched from the local Database and are then uploaded to the Google Drive folder that has just been created.
7. Now, the username, textfields, location (latitude & longitude), link to the Google Drive folder, are written to a CSV file.
