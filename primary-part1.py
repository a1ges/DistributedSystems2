# -- Imports -- #

import ops_pb2
import ops_pb2_grpc
import grpc
from concurrent import futures
import random
import argparse
import sys


# -- Imports -- #
"""
NOTE: 
PRIMARY -> reads file and sends request to secondaries/backups.

BACKUPS RECIEVE A "PUT" OR "GET" MESSAGE AND EXECUTES ON THEIR END, AND RETURNS A MESSAGE (ACKNOWLEDGEMENT) TO THE HOST

"""
class primary(ops_pb2_grpc.PrimaryBackupServiceServicer):
   
   # constructor , init datastore (dictionary)
    def __init__(self):
        self.datastore = {}
        # These are auxillary dictionaries to take in the requests from the file
        self.portNumber = -100
        self.backupPorts = []
    
    def getDatastore(self):
        return self.datastore
    def getOtherPorts(self):
        return self.backupPorts
    def getPort(self):
        return str(self.portNumber)
    
    # note method signature here. not typical of grpc method. What is being listened to in the client?
    
    def sendRequests(self):
        putCounter = 0
        # need to change self.getport to all backup servers
        channel = grpc.insecure_channel('localhost:'+self.backupPorts[0])

        stub = ops_pb2_grpc.PrimaryBackupServiceStub(channel)
        
        print("Sending Requests to Back-up servers")
        
        for i in range(len(self.datastore)):
            """
            GET REQUEST FORMAT:
                string key = 1;
            """
            if(self.datastore[i][0] == "GET"):
                # Generating Message
                getRequestMessage = ops_pb2.getRequest(key = self.datastore[i][1])
                getResponse = stub.getRequestOperation(getRequestMessage)

                # Checking response = {value | "not found"}

            elif(self.datastore[i][0] == "PUT"):
                """
                PUT REQUEST FORMAT:
                    string key = 1;
                    string value = 2;
                    int32 sequenceNumber = 3;
                """
                # Generating Message
                putRequestMessage = ops_pb2.putRequest(key=self.datastore[i][1], value=self.datastore[i][2], sequenceNumber = putCounter)
                stub.putRequestOperation(putRequestMessage)
                putCounter+=1



                # Checking Response = {Successful | Unsuccessful}
            else:
                print("Invalid Request, will not send.")

    
    def loadRequests(self):
        sequence = 0
        print("Adding Requests")

        requests = open("operations")

        lines = requests.readlines()

        for line in lines:
            

            # Parse line to words.
            line = line.replace("\n","")
            words = line.split(" ")
            #print(words)
           # print(words)
            key = words[1]
            value = words[2]
            # Check if keyword found in words[0]
            # Assumption , can have similar value but must have different key.
            if (words[0] == "put") and (key not in self.datastore):
                self.datastore[sequence] =  ("PUT",key,value)
                sequence+=1

                #self.datastore[key] = value
               # print("Key pair added (PUT) "+ key + ":" + value)
            elif ((words[0] == "get") and (value not in self.datastore.values())):
                #print("Key pair added (GET) "+ key + ":" + value)

                self.datastore[sequence] =  ("GET",key,value)
                sequence+=1
            
            # Operation Key Value
        requests.close()

    def loadLocations(self):
        print("Adding locations")
        PORTS = open("location")
        self.portNumber = int(PORTS.readline())
        lines = PORTS.readlines()
        for x in lines:
            self.backupPorts.append(x.replace("\n", ""))
       # print(self.backupPorts)
        PORTS.close()
        
        



   


def server():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=int(1)))
        primary_instance = primary()
        primary_instance.loadLocations()
        primary_instance.loadRequests()
        portNumber = primary_instance.getPort()

        ops_pb2_grpc.add_PrimaryBackupServiceServicer_to_server(primary_instance, server)
        server.add_insecure_port("[::]:"+portNumber)
        print("gRPC starting")
        server.start()
        primary_instance.sendRequests()
        #primary_instance.sendRequests()
        server.wait_for_termination()

server()