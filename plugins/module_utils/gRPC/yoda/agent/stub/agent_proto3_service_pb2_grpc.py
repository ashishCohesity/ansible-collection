# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yoda.agent.stub import agent_proto3_service_pb2 as yoda_dot_agent_dot_stub_dot_agent__proto3__service__pb2

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
        + f' but the generated code in yoda/agent/stub/agent_proto3_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class AgentProto3ServiceStub(object):
    """-----------------------------------------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AsyncVolumeMount = channel.unary_unary(
                '/cohesity.yoda.agent.stub.AgentProto3Service/AsyncVolumeMount',
                request_serializer=yoda_dot_agent_dot_stub_dot_agent__proto3__service__pb2.AsyncVolumeMountArg.SerializeToString,
                response_deserializer=yoda_dot_agent_dot_stub_dot_agent__proto3__service__pb2.AsyncVolumeMountResult.FromString,
                _registered_method=True)
        self.VolumeUnmount = channel.unary_unary(
                '/cohesity.yoda.agent.stub.AgentProto3Service/VolumeUnmount',
                request_serializer=yoda_dot_agent_dot_stub_dot_agent__proto3__service__pb2.VolumeUnmountArg.SerializeToString,
                response_deserializer=yoda_dot_agent_dot_stub_dot_agent__proto3__service__pb2.VolumeUnmountResult.FromString,
                _registered_method=True)


class AgentProto3ServiceServicer(object):
    """-----------------------------------------------------------------------------

    """

    def AsyncVolumeMount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VolumeUnmount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentProto3ServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AsyncVolumeMount': grpc.unary_unary_rpc_method_handler(
                    servicer.AsyncVolumeMount,
                    request_deserializer=yoda_dot_agent_dot_stub_dot_agent__proto3__service__pb2.AsyncVolumeMountArg.FromString,
                    response_serializer=yoda_dot_agent_dot_stub_dot_agent__proto3__service__pb2.AsyncVolumeMountResult.SerializeToString,
            ),
            'VolumeUnmount': grpc.unary_unary_rpc_method_handler(
                    servicer.VolumeUnmount,
                    request_deserializer=yoda_dot_agent_dot_stub_dot_agent__proto3__service__pb2.VolumeUnmountArg.FromString,
                    response_serializer=yoda_dot_agent_dot_stub_dot_agent__proto3__service__pb2.VolumeUnmountResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.yoda.agent.stub.AgentProto3Service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.yoda.agent.stub.AgentProto3Service', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AgentProto3Service(object):
    """-----------------------------------------------------------------------------

    """

    @staticmethod
    def AsyncVolumeMount(request,
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
            '/cohesity.yoda.agent.stub.AgentProto3Service/AsyncVolumeMount',
            yoda_dot_agent_dot_stub_dot_agent__proto3__service__pb2.AsyncVolumeMountArg.SerializeToString,
            yoda_dot_agent_dot_stub_dot_agent__proto3__service__pb2.AsyncVolumeMountResult.FromString,
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
    def VolumeUnmount(request,
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
            '/cohesity.yoda.agent.stub.AgentProto3Service/VolumeUnmount',
            yoda_dot_agent_dot_stub_dot_agent__proto3__service__pb2.VolumeUnmountArg.SerializeToString,
            yoda_dot_agent_dot_stub_dot_agent__proto3__service__pb2.VolumeUnmountResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)