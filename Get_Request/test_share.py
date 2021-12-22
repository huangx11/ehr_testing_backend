import requests
from FetchUserData import test_Delete_patient, test_download_patient, test_upload, test_download, test_Delete, test_allow_patient, test_upload_patient,test_share

### testing share
# from clinic to practice
#       before upload to clinic
# clinic		download 	– – – no
# 		        share 		– – – no
# patient	    download 	– – – no

# 	after upload to clinic
# patient	    download 	– – – no
# clinic		download 	– – – yes
# 		        share		– – – yes
	
# 	after share(overwrite)
# patient	    download 	– – – yes
# clinic		download 	– – – yes

# 	after share(cut)
# patient	    download 	– – – yes
# clinic		download 	– – – no

mode = ""
fromDir = "from_clinic"
from_app = "chartnotes"
from_patient_id = "47"
from_file_name = ""
from_subfolder = ""
toDir = "to_patient"
to_app = "tasks"
to_patient_id = "47"
to_file_name = ""
to_subfolder = ""
app = ""
patient_id = ""
file_name = "test.txt"
subfolder = ""

if from_app == "":
    from_app = app
if to_app == "":
    to_app = app

if to_file_name == "":
    to_file_name = file_name
if from_file_name == "":
    from_file_name = file_name

if from_patient_id == "":
    from_patient_id = patient_id
if to_patient_id == "":
    to_patient_id = patient_id

if from_subfolder == "":
    from_subfolder = subfolder
if to_subfolder == "":
    to_subfolder = subfolder

session = requests.Session()
def testing_share1():
    if patient_id == "" and from_patient_id == "" and to_patient_id == "":
        if not test_download("4110", to_file_name, to_subfolder, to_app, session):
            print(1)
            if not test_download("4110", from_file_name, from_subfolder, from_app, session) and not test_share(mode, fromDir, from_app, from_patient_id, from_file_name, from_subfolder, 
                    toDir, to_app, to_patient_id, to_file_name, to_subfolder, 
                    app, patient_id, file_name, subfolder, session):
                print(2)
                test_upload("OVERWRITE", "4110", from_file_name, from_subfolder, from_app, session)
                if not test_download("4110", to_file_name, to_subfolder, to_app, session):
                    print(3)
                    if test_download("4110", from_file_name, from_subfolder, from_app, session):
                        print(4)
                        test_share(mode, fromDir, from_app, from_patient_id, from_file_name, from_subfolder, 
                                    toDir, to_app, to_patient_id, to_file_name, to_subfolder, 
                                    app, patient_id, file_name, subfolder, session)
                        testing_share2()
                    else:
                        print(fromDir + " download failed after upload before share")
                else:
                    print(toDir + " download successful after upload before share")
            else:
                print(fromDir + " download successful before upload / " + fromDir + " share successful before upload")
        else:
            print(toDir + " download successful before upload")
    else:
        # test_download_patient("4110", "test.txt", 47, "", "doctor", "tasks", session)
        if not test_download_patient("4110", to_file_name, to_patient_id, to_subfolder, "doctor", to_app, session):
            print(1.1)
            if not test_download_patient("4110", from_file_name, from_patient_id,from_subfolder, "doctor",from_app, session) and not test_share(mode, fromDir, from_app, from_patient_id, from_file_name, from_subfolder, 
                    toDir, to_app, to_patient_id, to_file_name, to_subfolder, 
                    app, patient_id, file_name, subfolder, session):
                print(2.1)
                test_upload_patient("OVERWRITE", "4110", from_file_name, from_subfolder, from_patient_id, from_app, session)
                if not test_download_patient("4110", to_file_name, to_patient_id,to_subfolder, "doctor",to_app, session):
                    print(3.1)
                    if test_download_patient("4110", from_file_name, from_patient_id, from_subfolder, "doctor",from_app, session):
                        print(4.1)
                        test_share(mode, fromDir, from_app, from_patient_id, from_file_name, from_subfolder, 
                                    toDir, to_app, to_patient_id, to_file_name, to_subfolder, 
                                    app, patient_id, file_name, subfolder, session)
                        testing_share2()
                    else:
                        print(fromDir + " download failed after upload before share")
                else:
                    print(toDir + " download successful after upload before share")
            else:
                print(fromDir + " download successful before upload / " + fromDir + " share successful before upload")
        else:
            print(toDir + " download successful before upload")

def testing_share2():
    if patient_id == "" and from_patient_id == "" and to_patient_id == "":
        if mode == "CUT":
            print(mode)
            if not test_download("4110", from_file_name, from_subfolder, from_app, session):
                print(6)
                if test_download("4110", to_file_name, to_subfolder, to_app, session):
                    print("test successful")
                else:
                    print(toDir + " download failed after share cut")
            else:
                print(fromDir + " download successful after share cut")
        else:
            print(mode)
            if test_download("4110", from_file_name, from_subfolder, from_app, session):
                print(6)
                if test_download("4110", to_file_name, to_subfolder, to_app, session):
                    print("test successful")
                else:
                    print(toDir + " download failed after share overwrite")
            else:
                print(fromDir + " download failed after share overwrite")
    else:
        if mode == "CUT":
            print(mode)
            if not test_download("4110", from_file_name, from_subfolder, from_app, session):
                print(6.1)
                if test_download("4110", to_file_name, to_subfolder, to_app, session):
                    print("test successful")
                else:
                    print(toDir + " download failed after share cut")
            else:
                print(fromDir + " download successful after share cut")
        else:
            print(mode)
            if test_download_patient("4110", from_file_name, from_patient_id,from_subfolder, "doctor",from_app, session):
                print(6.1)
                if test_download_patient("4110", to_file_name, to_patient_id, to_subfolder, "doctor", to_app, session):
                    print("test successful")
                else:
                    print(toDir + " download failed after share overwrite")
            else:
                print(fromDir + " download failed after share overwrite")



testing_share1()







