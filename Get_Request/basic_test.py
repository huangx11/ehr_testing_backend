import requests
from FetchUserData import test_Delete_patient, test_download_patient, test_upload, test_download, test_Delete, test_allow_patient, test_upload_patient
import time

fileName = "test.txt"

# upload
# overwrite 
# 	download	– – – no  404
# 	delete 		– – – no  503

# 	after upload
# 	upload again  	– – – yes

# 	download	– – – yes  
# 	delete 		– – – yes 
def testing_upload_overwrite():
    session = requests.Session()
    if not test_download("4000", fileName, "", "app1", session):
        print(1)
        if not test_Delete("4000", fileName, "", "app1", session):
            print(2)
            test_upload("OVERWRITE", "4000", fileName, "", "app1", session)
            print(3)
            time.sleep(3)
            if test_download("4000", fileName, "", "app1", session):
                print(4)
                if test_upload("OVERWRITE", "4000", fileName, "", "app1", session):
                    print(5)
                    if test_Delete("4000", fileName, "", "app1", session):
                        print("test successful")
                    else:
                        print("Delete failed")
                else:
                    print("Second upload failed")
            else:
                print("Download after upload failed")
        else:
            print("Delete before upload successfully")
    else:
        print("Delete before upload successfully")

# save 
# 	download	– – – no  404
# 	delete 		– – – no  503

# 	after upload
# 	upload again  	– – – no

# 	download	– – – yes  
# 	delete 		– – – yes  
# def testing_upload_safe():
#     session = requests.Session()
#     if not test_download("4000", fileName, "", "app1", session):
#         print(1)
#         if not test_Delete("4000", fileName, "", session):
#             print(2)
#             test_upload("SAFE", "4000", fileName, "", "app1", session)
#             print(3)
#             time.sleep(3)
#             if test_download("4000", fileName, "", "app1", session):
#                 print(4)
#                 if not test_upload("SAFE", "4000", fileName, "", "app1", session):
#                     print(5)
#                     if test_Delete("4000", fileName, "", session):
#                         print("test successful")
#                     else:
#                         print("Delete failed")
#                 else:
#                     print("Second upload successfully")
#             else:
#                 print("Download after upload failed")
#         else:
#             print("Delete before upload successfully")
#     else:
#         print("Download before upload successfully")

###########################################################################

# download
# before upload	
# 	delete		– – – no
# 	download 	– – – no
	
# 	after upload 
# 	download 	– – – yes
# 	delete	 	– – – yes
	
# 	after delete
# 	download	– – – no

# def testing_download():
#     session = requests.Session()
#     if not test_Delete("4000", fileName, "", session):
#         print(1)
#         if not test_download("4000", fileName, "", "app1", session):
#             print(2)
#             test_upload("OVERWRITE", "4000", fileName, "", "app1", session)
#             if test_download("4000", fileName, "", "app1", session):
#                 print(3)
#                 if test_Delete("4000", fileName, "", session):
#                     if not test_download("4000", fileName, "", "app1", session):
#                         print("test successful")
#                     else:
#                         print("Download successful after delete")
#                 else:
#                     print("Delete failed")
#             else:
#                 print("Download failed")
#         else:
#             print("Download successfully")
#     else:
#         print("Delete before upload successfully")

############################################################

# delete
	# before upload 	
	# download	– – – no
	# delete		– – – no

	# after upload
	# delete		– – – yes
	# download	– – – no
# def testing_delete():
#     session = requests.Session()
#     if not test_download("4000", fileName, "", "app1", session):
#         print(1)
#         if not test_Delete("4000", fileName, "", session):
#             print(2)
#             test_upload("OVERWRITE", "4000", fileName, "", "app1", session)
#             if test_Delete("4000", fileName, "", session):
#                 print(3)
#                 if not test_download("4000", fileName, "", "app1", session):
#                     print("test successful")
#                 else:
#                     print("Download after delete successfully")
#             else:
#                 print("Delete failed")
#         else:
#             print("Delete before upload successfully")
#     else:
#         print("Download before upload successfully")

### testing allow patient
# def testing_allow_patient_1():
#     session = requests.Session()
#     if not test_download_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "patient", session) and not test_download_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "doctor", session):
#         print(1)
#         if not test_Delete_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "patient", session) and not test_Delete_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "doctor", session):
#             print(2)
#             test_upload_patient("OVERWRITE", "4100", fileName, "chart-note-123/2021-10-22", "47", session)
#             if test_download_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "doctor", session):
#                 print(3)
#                 if not test_download_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "patient", session):
#                     print(4)
#                     if not test_Delete_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "patient", session):
#                         print(5)
#                         if test_Delete_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "doctor", session):
#                             print(6)

#                         else:
#                             print("Doctor delete failed after upload")
#                     else:
#                         print("Patient delete successfully after upload")
#                 else:
#                     print("Patient download successfully after upload")
#             else:
#                 print("Doctor download failed after upload")
#         else:
#             print("Patient/Doctor delete before upload successfully")
#     else:
#         print("Patient/Doctor download before upload successfully")



testing_upload_overwrite()
# testing_upload_safe()
# testing_download()
# testing_delete()