# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from experimental.sachin.scribe.proxy.stub import rpc_service_pb2 as experimental_dot_sachin_dot_scribe_dot_proxy_dot_stub_dot_rpc__service__pb2

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
        + f' but the generated code in experimental/sachin/scribe/proxy/stub/rpc_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class RpcServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetNext = channel.unary_unary(
                '/cohesity.experimental.sachin.scribe.proxy.stub.RpcService/GetNext',
                request_serializer=experimental_dot_sachin_dot_scribe_dot_proxy_dot_stub_dot_rpc__service__pb2.GetNextArg.SerializeToString,
                response_deserializer=experimental_dot_sachin_dot_scribe_dot_proxy_dot_stub_dot_rpc__service__pb2.GetNextResult.FromString,
                _registered_method=True)


class RpcServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetNext(self, request, context):
        """Call to get (read) next batch of rows from scribe table.
        It returns a batch of rows.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetNext': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNext,
                    request_deserializer=experimental_dot_sachin_dot_scribe_dot_proxy_dot_stub_dot_rpc__service__pb2.GetNextArg.FromString,
                    response_serializer=experimental_dot_sachin_dot_scribe_dot_proxy_dot_stub_dot_rpc__service__pb2.GetNextResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.experimental.sachin.scribe.proxy.stub.RpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.experimental.sachin.scribe.proxy.stub.RpcService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RpcService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetNext(request,
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
            '/cohesity.experimental.sachin.scribe.proxy.stub.RpcService/GetNext',
            experimental_dot_sachin_dot_scribe_dot_proxy_dot_stub_dot_rpc__service__pb2.GetNextArg.SerializeToString,
            experimental_dot_sachin_dot_scribe_dot_proxy_dot_stub_dot_rpc__service__pb2.GetNextResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)