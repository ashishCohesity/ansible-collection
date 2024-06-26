# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from bridge.cloud_chunk_repository.stub import rpc_service_pb2 as bridge_dot_cloud__chunk__repository_dot_stub_dot_rpc__service__pb2

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
        + f' but the generated code in bridge/cloud_chunk_repository/stub/rpc_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class RpcServiceStub(object):
    """-----------------------------------------------------------------------------

    RPC service used by the cloud chunk repository.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReadChunks = channel.unary_unary(
                '/cohesity.bridge.cloud_chunk_repository.stub.RpcService/ReadChunks',
                request_serializer=bridge_dot_cloud__chunk__repository_dot_stub_dot_rpc__service__pb2.ReadChunksArg.SerializeToString,
                response_deserializer=bridge_dot_cloud__chunk__repository_dot_stub_dot_rpc__service__pb2.ReadChunksResult.FromString,
                _registered_method=True)


class RpcServiceServicer(object):
    """-----------------------------------------------------------------------------

    RPC service used by the cloud chunk repository.
    """

    def ReadChunks(self, request, context):
        """Read data for some chunks from a cloud chunk file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReadChunks': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadChunks,
                    request_deserializer=bridge_dot_cloud__chunk__repository_dot_stub_dot_rpc__service__pb2.ReadChunksArg.FromString,
                    response_serializer=bridge_dot_cloud__chunk__repository_dot_stub_dot_rpc__service__pb2.ReadChunksResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.bridge.cloud_chunk_repository.stub.RpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.bridge.cloud_chunk_repository.stub.RpcService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RpcService(object):
    """-----------------------------------------------------------------------------

    RPC service used by the cloud chunk repository.
    """

    @staticmethod
    def ReadChunks(request,
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
            '/cohesity.bridge.cloud_chunk_repository.stub.RpcService/ReadChunks',
            bridge_dot_cloud__chunk__repository_dot_stub_dot_rpc__service__pb2.ReadChunksArg.SerializeToString,
            bridge_dot_cloud__chunk__repository_dot_stub_dot_rpc__service__pb2.ReadChunksResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
