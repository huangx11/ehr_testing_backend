import requests
from FetchUserData import test_Delete_patient, test_download_patient, test_upload, test_download, test_Delete, test_allow_patient, test_upload_patient
import time

fileName = "test.txt"

### testing allow patient
# 			check file upload
# doctor/ patient	download	– – – no  404
# 	                delete 		– – – no  503

# 	        after upload
# doctor	download	– – – yes  
# 		    delete 		– – – yes 
# patient 	download	– – – no  
# 		    delete 		– – – no 

# 	        after allow patient
# doctor	download	– – – yes  
# 		    delete 		– – – yes 
# patient 	download	– – – yes  
# 		    delete 		– – – no 

session = requests.Session()
def testing_allow_patient_1():
    if not test_download_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "patient", "chartnotes", session) and not test_download_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "doctor", "chartnotes",session):
        print(1)
        if not test_Delete_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "patient", "chartnotes", session) and not test_Delete_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "doctor", "chartnotes", session):
            print(2)
            test_upload_patient("OVERWRITE", "4100", fileName, "chart-note-123/2021-10-22", "47", "chartnotes", session)
            if test_download_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "doctor", "chartnotes", session):
                print(3)
                if not test_download_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "patient", "chartnotes", session):
                    print(4)
                    if not test_Delete_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "patient", "chartnotes", session):
                        print(5)
                        if test_Delete_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "doctor", "chartnotes", session):
                            print(6)
                            print("testing before allow patient")
                            testing_allow_patient_2()
                        else:
                            print("Doctor delete failed after upload")
                    else:
                        print("Patient delete successfully after upload")
                else:
                    print("Patient download successfully after upload")
            else:
                print("Doctor download failed after upload")
        else:
            print("Patient/Doctor delete before upload successfully")
    else:
        print("Patient/Doctor download before upload successfully")

def testing_allow_patient_2():
    test_upload_patient("OVERWRITE", "4100", fileName, "chart-note-123/2021-10-22", "47", "chartnotes", session)
    if test_allow_patient("4100", fileName, "47", "chart-note-123/2021-10-22", session):
        print(7)
        if test_download_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "patient", "chartnotes", session):
            print(8)
            if not test_Delete_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "patient", "chartnotes", session):
                print(9)
                if test_download_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "doctor", "chartnotes", session):
                    print(10)
                    if test_Delete_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "doctor", "chartnotes", session):
                        print("test successful")
                    else:
                        print("Doctor delete failed after 'allow patient'")
                else:
                    print("Doctor download failed after 'allow patient'")
            else:
                print("Patient delete successfully after 'allow patient'")
        else:
            print("Patient download failed after 'allow patient'")
    else:
        print("allow patient failed")
















