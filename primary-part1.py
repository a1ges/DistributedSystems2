# -- Imports -- #

import ops_pb2
import ops_pb2_grpc
import grpc

# -- Imports -- #
"""
NOTE: 
PRIMARY -> reads file and sends request to secondaries/backups.

BACKUPS RECIEVE A "PUT" OR "GET" MESSAGE AND EXECUTES ON THEIR END, AND RETURNS A MESSAGE (ACKNOWLEDGEMENT) TO THE HOST

"""
class primary:
   
   # constructor , init datastore (dictionary)
    def __init__(self):
        self.datastore = {}
    
    
    def getrequest(self, request, context):
        request
        return "Not Found"
    
    def putRequest(self, request, context):

        return "Unsuccessful"
    
    def loadRequests(self):
        requests = open("location")

        # Header = Row 0. REMOVE [1:] IF FILE DOES NOT CONTAIN HEADER.

        lines = requests.readlines()[1:]

        for line in lines:
            

            # Parse line to words.
            line = line.replace("\n","")
            words = line.split(" ")
            #print(words)

            key = words[1]
            value = words[2]
            # Check if keyword found in words[0]
            # Assumption , can have similar value but must have different key.
            if ((words[0] == "put" or words[0] == "get")) and (key not in self.datastore):
                #self.datastore[key] = value
                #print("Key pair added "+ key + ":" + value)
            
            
            # Operation Key Value
        requests.close()


p = primary()
p.loadRequests()