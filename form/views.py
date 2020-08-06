from __future__ import print_function
from django.shortcuts import render
from .models import media
from django.utils import timezone
from django.http import HttpResponse
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
import csv

# Create your views here.


def form(request):
    if request.method == 'POST':
        username = request.POST["username"]
        textfield1 = request.POST["textfield1"]
        textfield2 = request.POST["textfield2"]
        textfield3 = request.POST["textfield3"]
        textfield4 = request.POST["textfield4"]
        textfield5 = request.POST["textfield5"]
        image1 = request.FILES["image1"]
        image2 = request.FILES["image2"]
        image3 = request.FILES["image3"]
        image4 = request.FILES["image4"]
        image5 = request.FILES["image5"]
        latitude = request.POST["latitude"]
        longitude = request.POST["longitude"]
        name1 = image1.name
        name2 = image2.name
        name3 = image3.name
        name4 = image4.name
        name5 = image5.name
        name1 = "_".join(name1.split())
        name2 = "_".join(name2.split())
        name3 = "_".join(name3.split())
        name4 = "_".join(name4.split())
        name5 = "_".join(name5.split())
        file_name1 = 'D:\\Projects\\Django\\FormSite2\\FormSite\\media\\images\\'+name1
        file_name2 = 'D:\\Projects\\Django\\FormSite2\\FormSite\\media\\images\\'+name2
        file_name3 = 'D:\\Projects\\Django\\FormSite2\\FormSite\\media\\images\\'+name3
        file_name4 = 'D:\\Projects\\Django\\FormSite2\\FormSite\\media\\images\\'+name4
        file_name5 = 'D:\\Projects\\Django\\FormSite2\\FormSite\\media\\images\\'+name5
        add_data = media(img1 = image1,img2 = image2,img3 = image3,img4 = image4,img5 = image5,
                        text1 = textfield1,text2 = textfield2,text3 = textfield3,text4 = textfield4,text5 = textfield5,
                        lattitude = latitude, longitude = longitude, username = username)
        add_data.save()
        
        
        SCOPES = ['https://www.googleapis.com/auth/drive']
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('D:\\Projects\\Django\\FormSite2\\FormSite\\form\\files\\token.pickle'):
            with open('D:\\Projects\\Django\\FormSite2\\FormSite\\form\\files\\token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'D:\\Projects\\Django\\FormSite2\\FormSite\\form\\files\\credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('D:\\Projects\\Django\\FormSite2\\FormSite\\form\\files\\token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('drive', 'v3', credentials=creds)
            
        ### FOLDER CREATION IN GOOGLE DRIVE ###
        folder_metadata = {
            'name': username,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = service.files().create(body=folder_metadata,
                                    fields='id, webViewLink').execute()
        folder_id = file.get('id')
        folder_link = file.get('webViewLink')
            
        ####################
            
        ### FILES BEING UPLOADED TO THE ABOVE CREATED FOLDER ###
            
        file_metadata = {
            'name': name1,
            'parents': [folder_id]
        }
        media1 = MediaFileUpload(file_name1, mimetype='image/jpeg')
        file = service.files().create(body=file_metadata,
                                                media_body=media1,
                                                fields='id').execute()
        file_metadata = {
            'name': name2,
            'parents': [folder_id]
        }
        media1 = MediaFileUpload(file_name2, mimetype='image/jpeg')
        file = service.files().create(body=file_metadata,
                                            media_body=media1,
                                            fields='id').execute()
        file_metadata = {
            'name': name3,
            'parents': [folder_id]
        }
        media1 = MediaFileUpload(file_name3, mimetype='image/jpeg')
        file = service.files().create(body=file_metadata,
                                            media_body=media1,
                                            fields='id').execute()
        file_metadata = {
            'name': name4,
            'parents': [folder_id]
        }
        media1 = MediaFileUpload(file_name4, mimetype='image/jpeg')
        file = service.files().create(body=file_metadata,
                                            media_body=media1,
                                            fields='id').execute()
        file_metadata = {
            'name': name5,
            'parents': [folder_id]
        }
        media1 = MediaFileUpload(file_name5, mimetype='image/jpeg')
        file = service.files().create(body=file_metadata,
                                            media_body=media1,
                                            fields='id').execute()
            
            
        #############################################################
        
        
        with open('all_datas.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, textfield1,textfield2,textfield3,textfield4,textfield5, latitude, longitude, folder_link])
        
        return HttpResponse("Your submission has been recorded successfully!")
    
    return render(request,'forms/Form.html',{})