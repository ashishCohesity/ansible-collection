# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from bifrost.portal_proxy import portal_proxy_pb2 as bifrost_dot_portal__proxy_dot_portal__proxy__pb2
from bifrost.stub import bifrost_broker_service_pb2 as bifrost_dot_stub_dot_bifrost__broker__service__pb2

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
        + f' but the generated code in bifrost/stub/bifrost_broker_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class BifrostBrokerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BidiCall = channel.stream_stream(
                '/cohesity.bifrost.stub.BifrostBrokerService/BidiCall',
                request_serializer=bifrost_dot_stub_dot_bifrost__broker__service__pb2.StreamMessage.SerializeToString,
                response_deserializer=bifrost_dot_stub_dot_bifrost__broker__service__pb2.StreamMessage.FromString,
                _registered_method=True)
        self.BrokerCall = channel.unary_unary(
                '/cohesity.bifrost.stub.BifrostBrokerService/BrokerCall',
                request_serializer=bifrost_dot_stub_dot_bifrost__broker__service__pb2.BifrostRequest.SerializeToString,
                response_deserializer=bifrost_dot_stub_dot_bifrost__broker__service__pb2.BrokerResponse.FromString,
                _registered_method=True)
        self.BidiStream = channel.stream_stream(
                '/cohesity.bifrost.stub.BifrostBrokerService/BidiStream',
                request_serializer=bifrost_dot_portal__proxy_dot_portal__proxy__pb2.BifrostPortalProxyStreamData.SerializeToString,
                response_deserializer=bifrost_dot_portal__proxy_dot_portal__proxy__pb2.BifrostPortalProxyStreamData.FromString,
                _registered_method=True)
        self.TunnelProxyStream = channel.stream_stream(
                '/cohesity.bifrost.stub.BifrostBrokerService/TunnelProxyStream',
                request_serializer=bifrost_dot_portal__proxy_dot_portal__proxy__pb2.BifrostPortalProxyStreamData.SerializeToString,
                response_deserializer=bifrost_dot_portal__proxy_dot_portal__proxy__pb2.BifrostPortalProxyStreamData.FromString,
                _registered_method=True)


class BifrostBrokerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BidiCall(self, request_iterator, context):
        """Method used to setup a reverse server i.e. from bifrost-broker
        to bifrost-server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BrokerCall(self, request, context):
        """Method used by bifrost-server to send a request to bifrost-broker
        using gRPC's unary rpc mechanism.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BidiStream(self, request_iterator, context):
        """Method used to proxy tcp-connection from bifrost-server(tenant-side)
        to bifrost-broker(cluster-side) via bidi-gRPC streams.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TunnelProxyStream(self, request_iterator, context):
        """RPC used for tunnel proxy (outgoing TCP connections from cohesity to
        outside world). These streams can be hooked up to a socks proxy or a
        pure TCP proxy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BifrostBrokerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BidiCall': grpc.stream_stream_rpc_method_handler(
                    servicer.BidiCall,
                    request_deserializer=bifrost_dot_stub_dot_bifrost__broker__service__pb2.StreamMessage.FromString,
                    response_serializer=bifrost_dot_stub_dot_bifrost__broker__service__pb2.StreamMessage.SerializeToString,
            ),
            'BrokerCall': grpc.unary_unary_rpc_method_handler(
                    servicer.BrokerCall,
                    request_deserializer=bifrost_dot_stub_dot_bifrost__broker__service__pb2.BifrostRequest.FromString,
                    response_serializer=bifrost_dot_stub_dot_bifrost__broker__service__pb2.BrokerResponse.SerializeToString,
            ),
            'BidiStream': grpc.stream_stream_rpc_method_handler(
                    servicer.BidiStream,
                    request_deserializer=bifrost_dot_portal__proxy_dot_portal__proxy__pb2.BifrostPortalProxyStreamData.FromString,
                    response_serializer=bifrost_dot_portal__proxy_dot_portal__proxy__pb2.BifrostPortalProxyStreamData.SerializeToString,
            ),
            'TunnelProxyStream': grpc.stream_stream_rpc_method_handler(
                    servicer.TunnelProxyStream,
                    request_deserializer=bifrost_dot_portal__proxy_dot_portal__proxy__pb2.BifrostPortalProxyStreamData.FromString,
                    response_serializer=bifrost_dot_portal__proxy_dot_portal__proxy__pb2.BifrostPortalProxyStreamData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.bifrost.stub.BifrostBrokerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.bifrost.stub.BifrostBrokerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class BifrostBrokerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BidiCall(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/cohesity.bifrost.stub.BifrostBrokerService/BidiCall',
            bifrost_dot_stub_dot_bifrost__broker__service__pb2.StreamMessage.SerializeToString,
            bifrost_dot_stub_dot_bifrost__broker__service__pb2.StreamMessage.FromString,
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
    def BrokerCall(request,
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
            '/cohesity.bifrost.stub.BifrostBrokerService/BrokerCall',
            bifrost_dot_stub_dot_bifrost__broker__service__pb2.BifrostRequest.SerializeToString,
            bifrost_dot_stub_dot_bifrost__broker__service__pb2.BrokerResponse.FromString,
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
    def BidiStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/cohesity.bifrost.stub.BifrostBrokerService/BidiStream',
            bifrost_dot_portal__proxy_dot_portal__proxy__pb2.BifrostPortalProxyStreamData.SerializeToString,
            bifrost_dot_portal__proxy_dot_portal__proxy__pb2.BifrostPortalProxyStreamData.FromString,
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
    def TunnelProxyStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/cohesity.bifrost.stub.BifrostBrokerService/TunnelProxyStream',
            bifrost_dot_portal__proxy_dot_portal__proxy__pb2.BifrostPortalProxyStreamData.SerializeToString,
            bifrost_dot_portal__proxy_dot_portal__proxy__pb2.BifrostPortalProxyStreamData.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
