# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from alerts.agent.stub import agent_service_pb2 as alerts_dot_agent_dot_stub_dot_agent__service__pb2

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
        + f' but the generated code in alerts/agent/stub/agent_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class RpcServiceStub(object):
    """-----------------------------------------------------------------------------

    RPC service used by the Alerts agent.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RaiseAlerts = channel.unary_unary(
                '/cohesity.alerts.agent.RpcService/RaiseAlerts',
                request_serializer=alerts_dot_agent_dot_stub_dot_agent__service__pb2.RaiseAlertsArg.SerializeToString,
                response_deserializer=alerts_dot_agent_dot_stub_dot_agent__service__pb2.RaiseAlertsResult.FromString,
                _registered_method=True)
        self.GetMasterInfo = channel.unary_unary(
                '/cohesity.alerts.agent.RpcService/GetMasterInfo',
                request_serializer=alerts_dot_agent_dot_stub_dot_agent__service__pb2.GetMasterInfoArg.SerializeToString,
                response_deserializer=alerts_dot_agent_dot_stub_dot_agent__service__pb2.GetMasterInfoResult.FromString,
                _registered_method=True)


class RpcServiceServicer(object):
    """-----------------------------------------------------------------------------

    RPC service used by the Alerts agent.
    """

    def RaiseAlerts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMasterInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RaiseAlerts': grpc.unary_unary_rpc_method_handler(
                    servicer.RaiseAlerts,
                    request_deserializer=alerts_dot_agent_dot_stub_dot_agent__service__pb2.RaiseAlertsArg.FromString,
                    response_serializer=alerts_dot_agent_dot_stub_dot_agent__service__pb2.RaiseAlertsResult.SerializeToString,
            ),
            'GetMasterInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMasterInfo,
                    request_deserializer=alerts_dot_agent_dot_stub_dot_agent__service__pb2.GetMasterInfoArg.FromString,
                    response_serializer=alerts_dot_agent_dot_stub_dot_agent__service__pb2.GetMasterInfoResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.alerts.agent.RpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.alerts.agent.RpcService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RpcService(object):
    """-----------------------------------------------------------------------------

    RPC service used by the Alerts agent.
    """

    @staticmethod
    def RaiseAlerts(request,
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
            '/cohesity.alerts.agent.RpcService/RaiseAlerts',
            alerts_dot_agent_dot_stub_dot_agent__service__pb2.RaiseAlertsArg.SerializeToString,
            alerts_dot_agent_dot_stub_dot_agent__service__pb2.RaiseAlertsResult.FromString,
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
    def GetMasterInfo(request,
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
            '/cohesity.alerts.agent.RpcService/GetMasterInfo',
            alerts_dot_agent_dot_stub_dot_agent__service__pb2.GetMasterInfoArg.SerializeToString,
            alerts_dot_agent_dot_stub_dot_agent__service__pb2.GetMasterInfoResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
