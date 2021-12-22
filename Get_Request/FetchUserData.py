import requests
from requests.models import Response
from requests.structures import CaseInsensitiveDict
from auth import JWT_TOKEN_FOR_PATIENT, base_auth, base_auth1, JWT_TOKEN_FOR_RENAME, JWT_TOKEN_FOR_ME

subfolder = ""
patient_id = ""

def test_upload(mode, permission, fileName, subfolder, targetFolder, session = None):
    headers = CaseInsensitiveDict()
    headers["Authorization"] = base_auth

    files = {'filea': open(fileName, 'rb')}

    if targetFolder == "app1":
        url = "http://192.168.10.62:6003/app1/upload_lua?"
    elif targetFolder == "tasks":
        url = "http://192.168.10.62:6003/tasks/upload_lua?"
    elif targetFolder == "chartnotes":
        url = "http://192.168.10.62:6003/chartnotes/upload_lua?"
    
    if subfolder == "":
        if not session:
            resp = requests.post(url + "permission=" + permission + 
                    "&" + 
                    "mode=" + mode, 
                    headers=headers, 
                    files = files)
        else:
            resp = session.post(url + "permission=" + permission + 
                    "&" + 
                    "mode=" + mode, 
                    headers=headers, 
                    files = files)
    else:
        if not session:
            resp = requests.post(url + "permission=" + permission + 
                    "&" + 
                    "mode=" + mode + "&"
                    "subfolder=" + subfolder, 
                    headers=headers, 
                    files = files)
        else:
            resp = session.post(url + "permission=" + permission + 
                    "&" + 
                    "mode=" + mode + "&"
                    "subfolder=" + subfolder, 
                    headers=headers, 
                    files = files)

    print('status code for upload: ' + str(resp.status_code))

    if resp.status_code == 200:
        return True
    else:
        return False

    # assert resp.status_code == 200, 'Upload failed'
    

def test_upload_rename(mode, permission, fileName, patient_id, new_name, session = None):
    headers = CaseInsensitiveDict()
    headers["Authorization"] = JWT_TOKEN_FOR_RENAME

    files = {'filea': open(fileName, 'rb')}

    url = "http://192.168.10.62:6003/app1/upload_lua?"
    #"mode=OVERWRITE"
    if not session:
        resp = requests.post(url + 
                "permission=" + permission + "&" + 
                "mode=" + mode + "&" + 
                "rename=" + new_name + "&" + 
                "patient_id=" + patient_id, 
                headers=headers, 
                files = files)
    else:
        resp = session.post(url + 
                "permission=" + permission + "&" + 
                "mode=" + mode + "&" + 
                "rename=" + new_name + "&" + 
                "patient_id=" + patient_id, 
                headers=headers, 
                files = files)

    print('status code for upload: ' + str(resp.status_code))


    assert resp.status_code == 200, 'Upload new name / file failed'
    print('Upload new name / file successfully!')


def test_upload_patient(mode, permission, fileName, subfolder, patient_id, targetFolder,session = None):
    headers = CaseInsensitiveDict()
    # headers["Authorization"] = base_auth
    headers["Authorization"] = JWT_TOKEN_FOR_RENAME

    files = {'filea': open(fileName, 'rb')}

    if targetFolder == "app1":
        url = "http://192.168.10.62:6003/app1/upload_lua?"
    elif targetFolder == "tasks":
        url = "http://192.168.10.62:6003/tasks/upload_lua?"
    elif targetFolder == "chartnotes":
        url = "http://192.168.10.62:6003/chartnotes/upload_lua?"

    if not session:
        if subfolder == "":
            resp = requests.post(url + "permission=" + permission + 
                    "&" + 
                    "mode=" + mode + "&" +
                    "patient_id=" + patient_id, 
                    headers=headers, 
                    files = files)
        else:
            resp = requests.post(url + "permission=" + permission + 
                    "&" + 
                    "mode=" + mode + "&" +
                    "patient_id=" + patient_id + "&" + 
                    "subfolder=" + subfolder, 
                    headers=headers, 
                    files = files)
    else:
        if subfolder == "":
            resp = session.post(url + "permission=" + permission + 
                    "&" + 
                    "mode=" + mode + "&" +
                    "patient_id=" + patient_id, 
                    headers=headers, 
                    files = files)
        else:
            resp = session.post(url + "permission=" + permission + 
                    "&" + 
                    "mode=" + mode + "&" +
                    "patient_id=" + patient_id + "&" + 
                    "subfolder=" + subfolder, 
                    headers=headers, 
                    files = files)

    print('status code for upload: ' + str(resp.status_code))

    assert resp.status_code == 200, 'Upload failed'
    print('Upload file successfully!')





##########################################################################

def test_download(permission, fileName, subfolder, targetFolder, session = None):
    headers = CaseInsensitiveDict()
    headers["Authorization"] = base_auth
    # headers["Authorization"] = JWT_TOKEN_FOR_RENAME

    if targetFolder == "app1":
        url = "http://192.168.10.62:6003/app1/download_lua?"
    elif targetFolder == "tasks":
        url = "http://192.168.10.62:6003/tasks/download_lua?"
    elif targetFolder == "chartnotes":
        url = "http://192.168.10.62:6003/chartnotes/download_lua?"

    if not session:
        if subfolder == "":
            resp = requests.get(url + "permission=" + permission + 
                    "&" + 
                    "file_name=" + fileName, 
                    headers=headers)
        else: 
            resp = requests.get(url + "permission=" + permission + 
                    "&" + 
                    "file_name=" + fileName + "&" + 
                    "subfolder=" + subfolder, 
                    headers=headers)
    else:
        if subfolder == "":
            resp = session.get(url + "permission=" + permission + 
                    "&" + 
                    "file_name=" + fileName, 
                    headers=headers)
        else: 
            resp = session.get(url + "permission=" + permission + 
                    "&" + 
                    "file_name=" + fileName + "&" + 
                    "subfolder=" + subfolder, 
                    headers=headers)

    print('status code for dowload: ' + str(resp.status_code))
   

    if resp.status_code == 200:
        with open('test.txt', "rb") as f:
            byte = f.read()
            if byte == resp.content:
                print("file content and download content are the same")
                return True
            else:
                print("file content and download content are different")
        
    else:
        return False

    # assert resp.status_code == 200, 'download failed'
    # print('Download successfully')
    # print('Download file content: ' + str(resp.content))
    # with open('test.txt') as f:
    #     file_contents = f.read ()
    #     print('My file content: \n' + file_contents)

def test_download_patient(permission, fileName, patient_id, subfolder, id, targetFolder, session = None):
    if targetFolder == "app1":
        url = "http://192.168.10.62:6003/app1/download_lua?"
    elif targetFolder == "tasks":
        url = "http://192.168.10.62:6003/tasks/download_lua?"
    elif targetFolder == "chartnotes":
        url = "http://192.168.10.62:6003/chartnotes/download_lua?"
        
    headers = CaseInsensitiveDict()
    if id == "doctor":
        headers["Authorization"] = base_auth
    else:
        headers["Authorization"] = JWT_TOKEN_FOR_PATIENT
    # headers["Authorization"] = JWT_TOKEN_FOR_RENAME


    if not session:
        if subfolder == "":
            resp = requests.get(url + "permission=" + permission + 
                    "&" + 
                    "file_name=" + fileName + "&" + 
                    "patient_id=" + str(patient_id), 
                    headers=headers)
        else:
            resp = requests.get(url + "permission=" + permission + 
                    "&" + 
                    "file_name=" + fileName + "&" + 
                    "patient_id=" + str(patient_id) + "&" + 
                    "subfolder=" + subfolder, 
                    headers=headers)
    else:
        if subfolder == "":
            resp = session.get(url + "permission=" + permission + 
                    "&" + 
                    "file_name=" + fileName + "&" + 
                    "patient_id=" + str(patient_id), 
                    headers=headers)
        else:
            resp = session.get(url + "permission=" + permission + 
                    "&" + 
                    "file_name=" + fileName + "&" + 
                    "patient_id=" + str(patient_id) + "&" + 
                    "subfolder=" + subfolder, 
                    headers=headers)

    # print(resp.headers)
    print('status code for dowload: ' + str(resp.status_code))
    print('Download file content: ' + str(resp.content))
    if resp.status_code == 200:
        return True
    else:
        return False
    assert resp.status_code == 200, 'download failed'
    print(resp.headers)
    print('status code for dowload: ' + str(resp.status_code))
    print('Download successfully')
    print('Download file content: ' + str(resp.content))



##############################################################################

def test_Delete(permission, fileName, subfolder, targetFolder, session = None):
    if targetFolder == "app1":
        url = "http://192.168.10.62:6003/app1/download_lua?"
    elif targetFolder == "tasks":
        url = "http://192.168.10.62:6003/tasks/download_lua?"
    elif targetFolder == "chartnotes":
        url = "http://192.168.10.62:6003/chartnotes/download_lua?"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = base_auth
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    if subfolder == "":
        # data = '{"permission":4000, "file_name":"test.txt"}'
        data = '{"permission":"' + permission + '", "file_name":"' + fileName + '"}'
        print(str(data))
    else:
        # data = '{"permission":4000, "file_name":"test.txt", "subfolder":"chart-note-123/2021-10-22"}'
        data = '{"permission":"' + permission + '", "file_name":"' + fileName + '", "subfolder":"' + subfolder + '"}'
        print(str(data))
    
    if not session:
        resp = requests.post(url, headers=headers, data=str(data))
    else:
        resp = session.post(url, headers=headers, data=str(data))

    print('status code for delete: ' + str(resp.status_code))

    if resp.status_code == 200:
        return True
    else:
        return False

    # assert resp.status_code == 200, 'Delete failed'
    # print('Delete file successfully!')
    
def test_Delete_patient(permission, fileName, patient_id, subfolder, id, targetFolder, session = None):
    if targetFolder == "app1":
        url = "http://192.168.10.62:6003/app1/delete_lua?"
    elif targetFolder == "tasks":
        url = "http://192.168.10.62:6003/tasks/delete_lua?"
    elif targetFolder == "chartnotes":
        url = "http://192.168.10.62:6003/chartnotes/delete_lua?"

    headers = CaseInsensitiveDict()
    if id == "doctor":
        headers["Authorization"] = base_auth
    else:
        headers["Authorization"] = JWT_TOKEN_FOR_PATIENT
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    if subfolder == "" and patient_id == "":
        # data = '{"permission":4000, "file_name":"test.txt"}'
        data = "'" + '{"permission":"' + permission + '", "file_name":"' + fileName + '"}' + "'"
        print(str(data))
    elif patient_id == "":
        # data = '{"permission":4000, "file_name":"test.txt", "subfolder":"chart-note-123/2021-10-22"}'
        data = "'" + '{"permission":"' + permission + '", "file_name":"' + fileName + '", "subfolder":"' + subfolder + '"}' + "'"
        print(str(data))
    elif subfolder == "":
        data = "'" + '{"permission":"' + permission + '", "file_name":"' + fileName + '", "patient_id":' + str(patient_id) + '}' + "'"
        print(str(data))
    else:
        # data = '{"permission":4000, "file_name":"test.txt", "subfolder":"chart-note-123/2021-10-22"}'
        data = "'" + '{"permission":"' + permission + '", "file_name":"' + fileName + '", "patient_id":' + str(patient_id) + ', "subfolder":"' + subfolder + '"}' + "'"
        print(str(data))
    
    if not session:
        resp = requests.post(url, headers=headers, data=str(data))
    else:
        resp = session.post(url, headers=headers, data=str(data))

    print(resp.headers)
    print('status code for delete: ' + str(resp.status_code))

    if resp.status_code == 200:
        return True
    else:
        return False

    # assert resp.status_code == 200, 'Delete failed'
    # print('Delete file successfully!')
    

#############################################################


def test_share(mode, fromDir, from_app, from_patient_id, from_file_name, from_subfolder, 
                toDir, to_app, to_patient_id, to_file_name, to_subfolder, 
                app, patient_id, file_name, subfolder, session = None):
    url = "http://192.168.10.62:6003/share_lua"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = base_auth
    # headers["Authorization"] = base_auth1
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    dataString = "'{" + '"' + fromDir + '":{'
    
    i = 0
    if not from_app == "":
        dataString += '"app":"' + from_app + '"'
        i += 1
    if not from_patient_id == "":
        if i > 0:
            dataString += ', "patient_id":' + str(from_patient_id)
        else:
            dataString += '"patient_id":' + str(from_patient_id)
        i += 1
    if not from_file_name == "":
        if i > 0:
            dataString += ', "file_name":"' + from_file_name + '"'
        else:
            dataString += '"file_name":"' + from_file_name + '"'
        i += 1
    if not from_subfolder == "":
        if i > 0:
            dataString += ', "subfolder":"' + from_subfolder + '"'
        else:
            dataString += '"subfolder":"' + from_subfolder + '"'

    i = 0
    dataString += '}, "' + toDir + '":{'
    if not to_app == "":
        dataString += '"app":"' + to_app + '"'
        i += 1
    if not to_patient_id == "":
        if i > 0:
            dataString += ', "patient_id":' + str(to_patient_id)
        else:
            dataString += '"patient_id":' + str(to_patient_id)
        i += 1
    if not to_file_name == "":
        if i > 0:
            dataString += ', "file_name":"' + to_file_name + '"'
        else:
            dataString += '"file_name":"' + to_file_name + '"'
        i += 1
    if not to_subfolder == "":
        if i > 0:
            dataString += ', "subfolder":"' + to_subfolder + '"'
        else:
            dataString += '"subfolder":"' + to_subfolder + '"'
    dataString += '}, '

    i = 0
    if not app == "":
        dataString += '"app":"' + app + '"'
        i += 1
    if not patient_id == "":
        if i > 0:
            dataString += ', "patient_id":' + str(patient_id)
        else:
            dataString += '"patient_id":' + str(patient_id)
        i += 1
    if not file_name == "":
        if i > 0:
            dataString += ', "file_name":"' + file_name + '"'
        else:
            dataString += '"file_name":"' + file_name + '"'
        i += 1
    if not subfolder == "":
        if i > 0:
            dataString += ', "subfolder":"' + subfolder + '"'
        else:
            dataString += '"subfolder":"' + subfolder + '"'
        i += 1
    if not mode == "":
        if i > 0:
            dataString += ', "mode":"' + mode + '"'
        else:
            dataString += '"mode":"' + mode + '"'
    dataString += "}'"
    print(dataString)
    
    if from_app == "" and to_app == "" and app == "":
        print("please insert a app")
    if from_file_name == "" and to_file_name == "" and file_name == "":
        print("please insert file name")

    if not session:
        resp = requests.post(url, headers=headers, data=dataString)
    else:
        resp = session.post(url, headers=headers, data=dataString)

    print(resp.status_code)
    print(resp.headers)
    
    if resp.status_code == 200:
        print('Move patient upload(share) successfully!')
        return True
    else:
        return False

    assert resp.status_code == 200, 'move patient upload(share) failed'
    print('Move patient upload(share) successfully!')
    
###################################################################

def test_allow_patient(permission, fileName, patient_id, subfolder, session = None):
    url = "http://192.168.10.62:6003/chartnotes/allow_patient/"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = base_auth
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    
    # data = '{"permission":4110, "file_name":"Dockerfile", "patient_id":47,"subfolder":"chart-note-123/2021-10-22"}'
    data = '{"permission":"' + permission + '", "file_name":"' + fileName + '", "patient_id":"' + patient_id + '", "subfolder":"' + subfolder + '"}'
    print(str(data))

    if not session:
        resp = requests.post(url, headers=headers, data=str(data))
    else:
        resp = session.post(url, headers=headers, data=str(data))

    print('status code for allow_patient: ' + str(resp.status_code))

    if resp.status_code == 200:
        return True
    else:
        return False














