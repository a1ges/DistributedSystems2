# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ops_pb2 as ops__pb2


class PrimaryBackupServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.putRequestOperation = channel.unary_unary(
                '/main.PrimaryBackupService/putRequestOperation',
                request_serializer=ops__pb2.putRequest.SerializeToString,
                response_deserializer=ops__pb2.replyPutRequest.FromString,
                )
        self.getRequestOperation = channel.unary_unary(
                '/main.PrimaryBackupService/getRequestOperation',
                request_serializer=ops__pb2.getRequest.SerializeToString,
                response_deserializer=ops__pb2.replyGetRequest.FromString,
                )


class PrimaryBackupServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def putRequestOperation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getRequestOperation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PrimaryBackupServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'putRequestOperation': grpc.unary_unary_rpc_method_handler(
                    servicer.putRequestOperation,
                    request_deserializer=ops__pb2.putRequest.FromString,
                    response_serializer=ops__pb2.replyPutRequest.SerializeToString,
            ),
            'getRequestOperation': grpc.unary_unary_rpc_method_handler(
                    servicer.getRequestOperation,
                    request_deserializer=ops__pb2.getRequest.FromString,
                    response_serializer=ops__pb2.replyGetRequest.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'main.PrimaryBackupService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PrimaryBackupService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def putRequestOperation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/main.PrimaryBackupService/putRequestOperation',
            ops__pb2.putRequest.SerializeToString,
            ops__pb2.replyPutRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getRequestOperation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/main.PrimaryBackupService/getRequestOperation',
            ops__pb2.getRequest.SerializeToString,
            ops__pb2.replyGetRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)