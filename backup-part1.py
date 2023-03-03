import ops_pb2
import ops_pb2_grpc
import grpc
from concurrent import futures
import random
import argparse
import sys


class backup(ops_pb2_grpc.PrimaryBackupServiceServicer):
    def __init__(self):
        datastore = {}
        port =  -999
    
    
    # Checking Response = {Successful | Unsuccessful}

    def putRequestOperation(self, request, context):
        # Request = key, value
        if(request.key in self.datastore) or (request.value in self.datastore.values()):
            return ops_pb2.replyPutRequest(response="unsuccessful")
        else:
            self.datastore[request.key] = request.value
            return ops_pb2.replyPutRequest(response="successful")
        

    

    def getRequestOperation(self,request,context):
        if(request.key not in self.datastore):
            return ops_pb2.replyGetRequest(response="successful")
        else:
            return ops_pb2.replyGetRequest(response=self.datastore[request.key])


def server():
        parse = argparse.ArgumentParser(prog="backup-part1.py", description="Backup Server")
        parse.add_argument("Port Number", type=int)
        args = parse.parse_args()
        port = sys.argv[1]
        if(port!=-999):
            server = grpc.server(futures.ThreadPoolExecutor())
            ops_pb2_grpc.add_PrimaryBackupServiceServicer_to_server(backup, server)
            server.add_insecure_port('[::]:'+port)

            print("gRPC starting")
            server.start()
            server.wait_for_termination()
        else:
            print("Invalid port")


server()