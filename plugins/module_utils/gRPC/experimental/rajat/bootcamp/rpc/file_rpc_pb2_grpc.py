# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from experimental.rajat.bootcamp.rpc import file_rpc_pb2 as experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in experimental/rajat/bootcamp/rpc/file_rpc_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class FileRpcStub(object):
    """File Range Read/Write RPC servie.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateFile = channel.unary_unary(
                '/cohesity.experimental.rajat.bootcamp.rpc.FileRpc/CreateFile',
                request_serializer=experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.CreateFileReq.SerializeToString,
                response_deserializer=experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.CreateFileResp.FromString,
                _registered_method=True)
        self.ReadFileRange = channel.unary_unary(
                '/cohesity.experimental.rajat.bootcamp.rpc.FileRpc/ReadFileRange',
                request_serializer=experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.ReadFileRangeReq.SerializeToString,
                response_deserializer=experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.ReadFileRangeResp.FromString,
                _registered_method=True)
        self.WriteFileRange = channel.unary_unary(
                '/cohesity.experimental.rajat.bootcamp.rpc.FileRpc/WriteFileRange',
                request_serializer=experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.WriteFileRangeReq.SerializeToString,
                response_deserializer=experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.WriteFileRangeResp.FromString,
                _registered_method=True)


class FileRpcServicer(object):
    """File Range Read/Write RPC servie.
    """

    def CreateFile(self, request, context):
        """Create file RPC.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadFileRange(self, request, context):
        """Read File Range RPC.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteFileRange(self, request, context):
        """Write File Range RPC.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileRpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFile,
                    request_deserializer=experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.CreateFileReq.FromString,
                    response_serializer=experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.CreateFileResp.SerializeToString,
            ),
            'ReadFileRange': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadFileRange,
                    request_deserializer=experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.ReadFileRangeReq.FromString,
                    response_serializer=experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.ReadFileRangeResp.SerializeToString,
            ),
            'WriteFileRange': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteFileRange,
                    request_deserializer=experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.WriteFileRangeReq.FromString,
                    response_serializer=experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.WriteFileRangeResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.experimental.rajat.bootcamp.rpc.FileRpc', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.experimental.rajat.bootcamp.rpc.FileRpc', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FileRpc(object):
    """File Range Read/Write RPC servie.
    """

    @staticmethod
    def CreateFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.experimental.rajat.bootcamp.rpc.FileRpc/CreateFile',
            experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.CreateFileReq.SerializeToString,
            experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.CreateFileResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReadFileRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.experimental.rajat.bootcamp.rpc.FileRpc/ReadFileRange',
            experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.ReadFileRangeReq.SerializeToString,
            experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.ReadFileRangeResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def WriteFileRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.experimental.rajat.bootcamp.rpc.FileRpc/WriteFileRange',
            experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.WriteFileRangeReq.SerializeToString,
            experimental_dot_rajat_dot_bootcamp_dot_rpc_dot_file__rpc__pb2.WriteFileRangeResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
