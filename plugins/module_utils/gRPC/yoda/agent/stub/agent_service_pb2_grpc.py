# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yoda.agent.stub import agent_service_pb2 as yoda_dot_agent_dot_stub_dot_agent__service__pb2

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
        + f' but the generated code in yoda/agent/stub/agent_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class AgentServiceStub(object):
    """-----------------------------------------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HealthCheck = channel.unary_unary(
                '/cohesity.yoda.agent.stub.AgentService/HealthCheck',
                request_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.HealthCheckArg.SerializeToString,
                response_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.HealthCheckResult.FromString,
                _registered_method=True)
        self.Mount = channel.unary_unary(
                '/cohesity.yoda.agent.stub.AgentService/Mount',
                request_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.MountArg.SerializeToString,
                response_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.MountResult.FromString,
                _registered_method=True)
        self.Unmount = channel.unary_unary(
                '/cohesity.yoda.agent.stub.AgentService/Unmount',
                request_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.UnmountArg.SerializeToString,
                response_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.UnmountResult.FromString,
                _registered_method=True)
        self.ReadFileRange = channel.unary_unary(
                '/cohesity.yoda.agent.stub.AgentService/ReadFileRange',
                request_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.ReadFileRangeArg.SerializeToString,
                response_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.ReadFileRangeResult.FromString,
                _registered_method=True)
        self.RemovePath = channel.unary_unary(
                '/cohesity.yoda.agent.stub.AgentService/RemovePath',
                request_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.RemovePathArg.SerializeToString,
                response_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.RemovePathResult.FromString,
                _registered_method=True)
        self.ReadDir = channel.unary_unary(
                '/cohesity.yoda.agent.stub.AgentService/ReadDir',
                request_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.ReadDirArg.SerializeToString,
                response_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.ReadDirResult.FromString,
                _registered_method=True)
        self.PrepareVMVolumeInfo = channel.unary_unary(
                '/cohesity.yoda.agent.stub.AgentService/PrepareVMVolumeInfo',
                request_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.PrepareVMVolumeInfoArg.SerializeToString,
                response_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.PrepareResult.FromString,
                _registered_method=True)
        self.GetTaskStatus = channel.unary_unary(
                '/cohesity.yoda.agent.stub.AgentService/GetTaskStatus',
                request_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.GetTaskStatusArg.SerializeToString,
                response_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.GetTaskStatusResult.FromString,
                _registered_method=True)
        self.FileStat = channel.unary_unary(
                '/cohesity.yoda.agent.stub.AgentService/FileStat',
                request_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.FileStatArg.SerializeToString,
                response_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.FileStatResult.FromString,
                _registered_method=True)


class AgentServiceServicer(object):
    """-----------------------------------------------------------------------------

    """

    def HealthCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Mount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unmount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadFileRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemovePath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadDir(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PrepareVMVolumeInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTaskStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FileStat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HealthCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.HealthCheck,
                    request_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.HealthCheckArg.FromString,
                    response_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.HealthCheckResult.SerializeToString,
            ),
            'Mount': grpc.unary_unary_rpc_method_handler(
                    servicer.Mount,
                    request_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.MountArg.FromString,
                    response_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.MountResult.SerializeToString,
            ),
            'Unmount': grpc.unary_unary_rpc_method_handler(
                    servicer.Unmount,
                    request_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.UnmountArg.FromString,
                    response_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.UnmountResult.SerializeToString,
            ),
            'ReadFileRange': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadFileRange,
                    request_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.ReadFileRangeArg.FromString,
                    response_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.ReadFileRangeResult.SerializeToString,
            ),
            'RemovePath': grpc.unary_unary_rpc_method_handler(
                    servicer.RemovePath,
                    request_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.RemovePathArg.FromString,
                    response_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.RemovePathResult.SerializeToString,
            ),
            'ReadDir': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadDir,
                    request_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.ReadDirArg.FromString,
                    response_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.ReadDirResult.SerializeToString,
            ),
            'PrepareVMVolumeInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.PrepareVMVolumeInfo,
                    request_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.PrepareVMVolumeInfoArg.FromString,
                    response_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.PrepareResult.SerializeToString,
            ),
            'GetTaskStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTaskStatus,
                    request_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.GetTaskStatusArg.FromString,
                    response_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.GetTaskStatusResult.SerializeToString,
            ),
            'FileStat': grpc.unary_unary_rpc_method_handler(
                    servicer.FileStat,
                    request_deserializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.FileStatArg.FromString,
                    response_serializer=yoda_dot_agent_dot_stub_dot_agent__service__pb2.FileStatResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.yoda.agent.stub.AgentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.yoda.agent.stub.AgentService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AgentService(object):
    """-----------------------------------------------------------------------------

    """

    @staticmethod
    def HealthCheck(request,
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
            '/cohesity.yoda.agent.stub.AgentService/HealthCheck',
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.HealthCheckArg.SerializeToString,
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.HealthCheckResult.FromString,
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
    def Mount(request,
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
            '/cohesity.yoda.agent.stub.AgentService/Mount',
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.MountArg.SerializeToString,
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.MountResult.FromString,
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
    def Unmount(request,
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
            '/cohesity.yoda.agent.stub.AgentService/Unmount',
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.UnmountArg.SerializeToString,
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.UnmountResult.FromString,
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
            '/cohesity.yoda.agent.stub.AgentService/ReadFileRange',
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.ReadFileRangeArg.SerializeToString,
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.ReadFileRangeResult.FromString,
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
    def RemovePath(request,
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
            '/cohesity.yoda.agent.stub.AgentService/RemovePath',
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.RemovePathArg.SerializeToString,
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.RemovePathResult.FromString,
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
    def ReadDir(request,
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
            '/cohesity.yoda.agent.stub.AgentService/ReadDir',
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.ReadDirArg.SerializeToString,
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.ReadDirResult.FromString,
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
    def PrepareVMVolumeInfo(request,
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
            '/cohesity.yoda.agent.stub.AgentService/PrepareVMVolumeInfo',
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.PrepareVMVolumeInfoArg.SerializeToString,
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.PrepareResult.FromString,
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
    def GetTaskStatus(request,
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
            '/cohesity.yoda.agent.stub.AgentService/GetTaskStatus',
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.GetTaskStatusArg.SerializeToString,
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.GetTaskStatusResult.FromString,
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
    def FileStat(request,
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
            '/cohesity.yoda.agent.stub.AgentService/FileStat',
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.FileStatArg.SerializeToString,
            yoda_dot_agent_dot_stub_dot_agent__service__pb2.FileStatResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
