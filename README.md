## Very Important NOTE before starting:
The paths for many files in the views.py file have been given as absolute paths.
In order to make it work in your PC, you have to modify the destinations.


### How to create credentials for accessing the Google Drive API

#### You can easily create the client configuration by the following steps:

1. Go to this URL:
   https://developers.google.com/drive/api/v3/quickstart/python
2. Click on the "Enable the Drive API" button given in the Step 1 section.
3. This will prompt a dialogue box.
   Enter your Project name and click next.
   Then choose the Desktop App option and click create.
4. Now click on "Download Client Configuration" to download your configurations as a .json file
5. Name this file as "credentials" and save it with a .json format to the destination "...\FormSite\form\files"
6. Now your credentials files is ready.
7. You can start running the project now by starting the server.




While running for the first time, you will taken to an authorization page, for granting access to your application.
A pickle file will be created automatically.
So, you won't hav to grant access every time.


### In case it doesn't work when you start the server for the first time:
1. There is a file "Test.py", in the destination "...\FormSite\form\files"
2. Run this file once. This will create the pickle file.
3. Now you should not be having any problems with running your application.
