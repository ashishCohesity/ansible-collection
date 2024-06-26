# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from bifrost.stub import proxy_service_pb2 as bifrost_dot_stub_dot_proxy__service__pb2

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
        + f' but the generated code in bifrost/stub/proxy_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class BifrostProxyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BifrostCall = channel.unary_unary(
                '/cohesity.bifrost.stub.BifrostProxyService/BifrostCall',
                request_serializer=bifrost_dot_stub_dot_proxy__service__pb2.BifrostCallArg.SerializeToString,
                response_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.BifrostCallResult.FromString,
                _registered_method=True)
        self.GetProxyEndUserInfo = channel.unary_unary(
                '/cohesity.bifrost.stub.BifrostProxyService/GetProxyEndUserInfo',
                request_serializer=bifrost_dot_stub_dot_proxy__service__pb2.GetProxyEndUserInfoArg.SerializeToString,
                response_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.GetProxyEndUserInfoResult.FromString,
                _registered_method=True)
        self.BrokerListenForSocks = channel.unary_unary(
                '/cohesity.bifrost.stub.BifrostProxyService/BrokerListenForSocks',
                request_serializer=bifrost_dot_stub_dot_proxy__service__pb2.BrokerListenForSocksArg.SerializeToString,
                response_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.BrokerListenForSocksResult.FromString,
                _registered_method=True)
        self.CreateNetworkRealm = channel.unary_unary(
                '/cohesity.bifrost.stub.BifrostProxyService/CreateNetworkRealm',
                request_serializer=bifrost_dot_stub_dot_proxy__service__pb2.CreateNetworkRealmArg.SerializeToString,
                response_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.CreateNetworkRealmResult.FromString,
                _registered_method=True)
        self.UpdateNetworkRealm = channel.unary_unary(
                '/cohesity.bifrost.stub.BifrostProxyService/UpdateNetworkRealm',
                request_serializer=bifrost_dot_stub_dot_proxy__service__pb2.UpdateNetworkRealmArg.SerializeToString,
                response_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.UpdateNetworkRealmResult.FromString,
                _registered_method=True)
        self.GetNetworkRealms = channel.unary_unary(
                '/cohesity.bifrost.stub.BifrostProxyService/GetNetworkRealms',
                request_serializer=bifrost_dot_stub_dot_proxy__service__pb2.GetNetworkRealmsArg.SerializeToString,
                response_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.GetNetworkRealmsResult.FromString,
                _registered_method=True)
        self.DeleteNetworkRealm = channel.unary_unary(
                '/cohesity.bifrost.stub.BifrostProxyService/DeleteNetworkRealm',
                request_serializer=bifrost_dot_stub_dot_proxy__service__pb2.DeleteNetworkRealmArg.SerializeToString,
                response_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.DeleteNetworkRealmResult.FromString,
                _registered_method=True)
        self.CreateHyxConnector = channel.unary_unary(
                '/cohesity.bifrost.stub.BifrostProxyService/CreateHyxConnector',
                request_serializer=bifrost_dot_stub_dot_proxy__service__pb2.CreateHyxConnectorArg.SerializeToString,
                response_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.CreateHyxConnectorResult.FromString,
                _registered_method=True)
        self.UpdateHyxConnector = channel.unary_unary(
                '/cohesity.bifrost.stub.BifrostProxyService/UpdateHyxConnector',
                request_serializer=bifrost_dot_stub_dot_proxy__service__pb2.UpdateHyxConnectorArg.SerializeToString,
                response_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.UpdateHyxConnectorResult.FromString,
                _registered_method=True)
        self.GetHyxConnectors = channel.unary_unary(
                '/cohesity.bifrost.stub.BifrostProxyService/GetHyxConnectors',
                request_serializer=bifrost_dot_stub_dot_proxy__service__pb2.GetHyxConnectorsArg.SerializeToString,
                response_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.GetHyxConnectorsResult.FromString,
                _registered_method=True)
        self.DeleteHyxConnector = channel.unary_unary(
                '/cohesity.bifrost.stub.BifrostProxyService/DeleteHyxConnector',
                request_serializer=bifrost_dot_stub_dot_proxy__service__pb2.DeleteHyxConnectorArg.SerializeToString,
                response_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.DeleteHyxConnectorResult.FromString,
                _registered_method=True)
        self.BringUpConnector = channel.unary_unary(
                '/cohesity.bifrost.stub.BifrostProxyService/BringUpConnector',
                request_serializer=bifrost_dot_stub_dot_proxy__service__pb2.BringUpConnectorArg.SerializeToString,
                response_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.BringUpConnectorResult.FromString,
                _registered_method=True)
        self.UpdateBifrostReverseTunnel = channel.unary_unary(
                '/cohesity.bifrost.stub.BifrostProxyService/UpdateBifrostReverseTunnel',
                request_serializer=bifrost_dot_stub_dot_proxy__service__pb2.UpdateBifrostReverseTunnelArg.SerializeToString,
                response_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.UpdateBifrostReverseTunnelResult.FromString,
                _registered_method=True)


class BifrostProxyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BifrostCall(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProxyEndUserInfo(self, request, context):
        """RPC used by a component which is using bifrost's portal proxy to talk
        to a proxy client. Proxy client is talking to the listener (TcpListener)
        running on the bifrost. There exists a stream (TcpStream) between the
        proxy client and the proxy. The component and the bifrost broker have
        established another stream between them, which would allow broker to
        forward whatever data it receives to the component.
        ( proxy_client ->proxy -> bifrost_broker-> component )
        This RPC would allow the component to get the session info for the
        stream between proxy client and the listener (TcpListener).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BrokerListenForSocks(self, request, context):
        """RPC to request broker to start listening for socks clients. Broker will
        start listening on TCP. Refer to the state machine diagram in
        ENG-132238 for reference.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateNetworkRealm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateNetworkRealm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNetworkRealms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNetworkRealm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateHyxConnector(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateHyxConnector(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHyxConnectors(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteHyxConnector(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BringUpConnector(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBifrostReverseTunnel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BifrostProxyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BifrostCall': grpc.unary_unary_rpc_method_handler(
                    servicer.BifrostCall,
                    request_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.BifrostCallArg.FromString,
                    response_serializer=bifrost_dot_stub_dot_proxy__service__pb2.BifrostCallResult.SerializeToString,
            ),
            'GetProxyEndUserInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProxyEndUserInfo,
                    request_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.GetProxyEndUserInfoArg.FromString,
                    response_serializer=bifrost_dot_stub_dot_proxy__service__pb2.GetProxyEndUserInfoResult.SerializeToString,
            ),
            'BrokerListenForSocks': grpc.unary_unary_rpc_method_handler(
                    servicer.BrokerListenForSocks,
                    request_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.BrokerListenForSocksArg.FromString,
                    response_serializer=bifrost_dot_stub_dot_proxy__service__pb2.BrokerListenForSocksResult.SerializeToString,
            ),
            'CreateNetworkRealm': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNetworkRealm,
                    request_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.CreateNetworkRealmArg.FromString,
                    response_serializer=bifrost_dot_stub_dot_proxy__service__pb2.CreateNetworkRealmResult.SerializeToString,
            ),
            'UpdateNetworkRealm': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateNetworkRealm,
                    request_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.UpdateNetworkRealmArg.FromString,
                    response_serializer=bifrost_dot_stub_dot_proxy__service__pb2.UpdateNetworkRealmResult.SerializeToString,
            ),
            'GetNetworkRealms': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNetworkRealms,
                    request_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.GetNetworkRealmsArg.FromString,
                    response_serializer=bifrost_dot_stub_dot_proxy__service__pb2.GetNetworkRealmsResult.SerializeToString,
            ),
            'DeleteNetworkRealm': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNetworkRealm,
                    request_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.DeleteNetworkRealmArg.FromString,
                    response_serializer=bifrost_dot_stub_dot_proxy__service__pb2.DeleteNetworkRealmResult.SerializeToString,
            ),
            'CreateHyxConnector': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateHyxConnector,
                    request_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.CreateHyxConnectorArg.FromString,
                    response_serializer=bifrost_dot_stub_dot_proxy__service__pb2.CreateHyxConnectorResult.SerializeToString,
            ),
            'UpdateHyxConnector': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateHyxConnector,
                    request_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.UpdateHyxConnectorArg.FromString,
                    response_serializer=bifrost_dot_stub_dot_proxy__service__pb2.UpdateHyxConnectorResult.SerializeToString,
            ),
            'GetHyxConnectors': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHyxConnectors,
                    request_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.GetHyxConnectorsArg.FromString,
                    response_serializer=bifrost_dot_stub_dot_proxy__service__pb2.GetHyxConnectorsResult.SerializeToString,
            ),
            'DeleteHyxConnector': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteHyxConnector,
                    request_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.DeleteHyxConnectorArg.FromString,
                    response_serializer=bifrost_dot_stub_dot_proxy__service__pb2.DeleteHyxConnectorResult.SerializeToString,
            ),
            'BringUpConnector': grpc.unary_unary_rpc_method_handler(
                    servicer.BringUpConnector,
                    request_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.BringUpConnectorArg.FromString,
                    response_serializer=bifrost_dot_stub_dot_proxy__service__pb2.BringUpConnectorResult.SerializeToString,
            ),
            'UpdateBifrostReverseTunnel': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBifrostReverseTunnel,
                    request_deserializer=bifrost_dot_stub_dot_proxy__service__pb2.UpdateBifrostReverseTunnelArg.FromString,
                    response_serializer=bifrost_dot_stub_dot_proxy__service__pb2.UpdateBifrostReverseTunnelResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.bifrost.stub.BifrostProxyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.bifrost.stub.BifrostProxyService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class BifrostProxyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BifrostCall(request,
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
            '/cohesity.bifrost.stub.BifrostProxyService/BifrostCall',
            bifrost_dot_stub_dot_proxy__service__pb2.BifrostCallArg.SerializeToString,
            bifrost_dot_stub_dot_proxy__service__pb2.BifrostCallResult.FromString,
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
    def GetProxyEndUserInfo(request,
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
            '/cohesity.bifrost.stub.BifrostProxyService/GetProxyEndUserInfo',
            bifrost_dot_stub_dot_proxy__service__pb2.GetProxyEndUserInfoArg.SerializeToString,
            bifrost_dot_stub_dot_proxy__service__pb2.GetProxyEndUserInfoResult.FromString,
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
    def BrokerListenForSocks(request,
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
            '/cohesity.bifrost.stub.BifrostProxyService/BrokerListenForSocks',
            bifrost_dot_stub_dot_proxy__service__pb2.BrokerListenForSocksArg.SerializeToString,
            bifrost_dot_stub_dot_proxy__service__pb2.BrokerListenForSocksResult.FromString,
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
    def CreateNetworkRealm(request,
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
            '/cohesity.bifrost.stub.BifrostProxyService/CreateNetworkRealm',
            bifrost_dot_stub_dot_proxy__service__pb2.CreateNetworkRealmArg.SerializeToString,
            bifrost_dot_stub_dot_proxy__service__pb2.CreateNetworkRealmResult.FromString,
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
    def UpdateNetworkRealm(request,
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
            '/cohesity.bifrost.stub.BifrostProxyService/UpdateNetworkRealm',
            bifrost_dot_stub_dot_proxy__service__pb2.UpdateNetworkRealmArg.SerializeToString,
            bifrost_dot_stub_dot_proxy__service__pb2.UpdateNetworkRealmResult.FromString,
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
    def GetNetworkRealms(request,
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
            '/cohesity.bifrost.stub.BifrostProxyService/GetNetworkRealms',
            bifrost_dot_stub_dot_proxy__service__pb2.GetNetworkRealmsArg.SerializeToString,
            bifrost_dot_stub_dot_proxy__service__pb2.GetNetworkRealmsResult.FromString,
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
    def DeleteNetworkRealm(request,
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
            '/cohesity.bifrost.stub.BifrostProxyService/DeleteNetworkRealm',
            bifrost_dot_stub_dot_proxy__service__pb2.DeleteNetworkRealmArg.SerializeToString,
            bifrost_dot_stub_dot_proxy__service__pb2.DeleteNetworkRealmResult.FromString,
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
    def CreateHyxConnector(request,
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
            '/cohesity.bifrost.stub.BifrostProxyService/CreateHyxConnector',
            bifrost_dot_stub_dot_proxy__service__pb2.CreateHyxConnectorArg.SerializeToString,
            bifrost_dot_stub_dot_proxy__service__pb2.CreateHyxConnectorResult.FromString,
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
    def UpdateHyxConnector(request,
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
            '/cohesity.bifrost.stub.BifrostProxyService/UpdateHyxConnector',
            bifrost_dot_stub_dot_proxy__service__pb2.UpdateHyxConnectorArg.SerializeToString,
            bifrost_dot_stub_dot_proxy__service__pb2.UpdateHyxConnectorResult.FromString,
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
    def GetHyxConnectors(request,
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
            '/cohesity.bifrost.stub.BifrostProxyService/GetHyxConnectors',
            bifrost_dot_stub_dot_proxy__service__pb2.GetHyxConnectorsArg.SerializeToString,
            bifrost_dot_stub_dot_proxy__service__pb2.GetHyxConnectorsResult.FromString,
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
    def DeleteHyxConnector(request,
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
            '/cohesity.bifrost.stub.BifrostProxyService/DeleteHyxConnector',
            bifrost_dot_stub_dot_proxy__service__pb2.DeleteHyxConnectorArg.SerializeToString,
            bifrost_dot_stub_dot_proxy__service__pb2.DeleteHyxConnectorResult.FromString,
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
    def BringUpConnector(request,
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
            '/cohesity.bifrost.stub.BifrostProxyService/BringUpConnector',
            bifrost_dot_stub_dot_proxy__service__pb2.BringUpConnectorArg.SerializeToString,
            bifrost_dot_stub_dot_proxy__service__pb2.BringUpConnectorResult.FromString,
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
    def UpdateBifrostReverseTunnel(request,
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
            '/cohesity.bifrost.stub.BifrostProxyService/UpdateBifrostReverseTunnel',
            bifrost_dot_stub_dot_proxy__service__pb2.UpdateBifrostReverseTunnelArg.SerializeToString,
            bifrost_dot_stub_dot_proxy__service__pb2.UpdateBifrostReverseTunnelResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
