# import the os module
import os
import datetime

password = "root"

'''
agent_name="Manisha"
now = datetime.datetime.now()
folder_name = agent_name+now.isoformat()

path = "../Project/" + folder_name

# define the access rights
access_rights = 0o755

try:  
    os.mkdir(path, access_rights)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s" % path)

'''

'''
Downloading OSSEC and Installing Manager
'''
#os.system("wget -U ossec https://bintray.com/artifact/download/ossec/ossec-hids/ossec-hids-2.8.3.tar.gz")

#os.system("wget -U ossec https://raw.githubusercontent.com/ossec/ossec-docs/master/docs/whatsnew/checksums/2.8.3/ossec-hids-2.8.3.tar.gz.sha256")

#os.system("cat ossec-hids-2.8.3.tar.gz.sha256")

#os.system("sha256sum -c  ossec-hids-2.8.3.tar.gz.sha256 ossec-hids-2.8.3.tar.gz")

#os.system("tar -zxvf ossec-hids-*.tar.gz")


os.chdir("ossec-hids-2.8.3")
os.system("sudo ./install.sh ")

os.system('echo "root"')
