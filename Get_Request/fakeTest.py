# from FetchUserData import test_Delete, test_upload, test_download, test_upload_rename, test_download_patient,
import requests
from FetchUserData import test_Delete, test_download_patient, test_share, test_upload, test_download, test_Delete_patient
from requests.structures import CaseInsensitiveDict

fileName = "test.txt"
session =requests.Session()

### upload files
# safe
# test_upload("SAFE", "4110", fileName, "", "app1")

# overwrite
# test_upload("OVERWRITE", "4110", fileName, "", "chartnotes")


# download
# test_download("4110", fileName, "", "chartnotes")


# delete
test_Delete("4100", fileName, "", "app1",session)
# test_Delete_patient("4110", fileName, 47, "", "doctor", "chartnotes")
# test_download_patient("4110", "test.txt", 47, "", "doctor", "chartnotes", session)

### upload subfolder
# upload private
#test_upload("OVERWRITE", "4000", fileName, "a/b/c", "app1")

# upload to patient
# test_upload_patient("OVERWRITE", "4110", fileName, "chart-note-123/2021-10-22", "47")
# download patient
# test_download_patient("4110", "Dockerfile", "47", "chart-note-123/2021-10-22", "doctor", "app1")

# download private
# test_download("4000", fileName, "a/b/c", "app1")



### doctor test
# upload to practice
# test_upload("OVERWRITE", "4100", fileName, "", "app1")
# test_download("4100", fileName, "", "app1")

# upload to clinic
# test_upload("OVERWRITE", "4110", fileName, "", "app1")
# test_download("4110", fileName, "", "app1")

# upload to patient
# test_upload_patient("OVERWRITE", "4110", fileName, "", "47")
# test_download_patient("4110", fileName, "47", "", "doctor", "app1")

# other doctor in same clinic access patient file
# test_upload_patient("OVERWRITE", "4110", fileName, "", "47")
# test_download_patient("4110", fileName, "47", "", "doctor", "app1")

## over write other doctor's shared file
## forbidden as original file has permission 4110
# test_upload_rename("RENAME", "4000", fileName, "47", "try_rename_test.txt")

## forbidden as original file has permission 4110
# test_upload_patient("OVERWRITE", "4110", fileName, "", "47")
# test_download_patient("4110", fileName, "47", "", "doctor", "app1")


# upload to practice
# test_upload("OVERWRITE", "4100", fileName, "", "app1")
# test_download("4100", fileName, "", "app1")

# upload to clinic
# test_upload("OVERWRITE", "4110", fileName, "", "app1")
# test_download("4110", fileName, "", "app1")

# upload to patient
# test_upload("OVERWRITE", "4110", fileName, "", "app1")
# test_download("4110", fileName, "", "app1")





### share
# from clinic to patient
# test_share(mode, fromDir, from_app, from_patient_id, from_file_name, from_subfolder, 
                # toDir, to_app, to_patient_id, to_file_name, to_subfolder, 
                # app, patient_id, file_name, subfolder, session = None):
# test_share("", "from_clinic", "chartnotes", "47", "", "", "to_patient", "tasks", "47", "", "", "", "", "test.txt", "", session)
# test_share("CUT", "from_clinic", "chartnotes", "47", "test.txt", "a/b/c", "to_patient", "tasks", "47", "test.txt", "a/b/c", "app1", "47", "test.txt", "a/b/c", session)


# delete private
# test_Delete('4000', fileName, "")


### allow patient test




# test_download_patient("4100", fileName, "47", "chart-note-123/2021-10-22", "doctor", "app1" )
# test_Delete("4100", fileName, "chart-note-123/2021-10-22")




