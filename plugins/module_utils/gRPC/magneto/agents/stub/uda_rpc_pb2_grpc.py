# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from magneto.agents.stub import agent_base_pb2 as magneto_dot_agents_dot_stub_dot_agent__base__pb2
from magneto.agents.stub import uda_param_pb2 as magneto_dot_agents_dot_stub_dot_uda__param__pb2

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
        + f' but the generated code in magneto/agents/stub/uda_rpc_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class UdaRpcServiceStub(object):
    """-----------------------------------------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DiscoverUdaSource = channel.unary_unary(
                '/cohesity.magneto.agents.uda.stub.UdaRpcService/DiscoverUdaSource',
                request_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.DiscoverUdaSourceArg.SerializeToString,
                response_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.DiscoverUdaSourceResult.FromString,
                _registered_method=True)
        self.VerifyUdaSource = channel.unary_unary(
                '/cohesity.magneto.agents.uda.stub.UdaRpcService/VerifyUdaSource',
                request_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.VerifyUdaSourceArg.SerializeToString,
                response_deserializer=magneto_dot_agents_dot_stub_dot_agent__base__pb2.Result.FromString,
                _registered_method=True)
        self.GetUdaObjects = channel.unary_unary(
                '/cohesity.magneto.agents.uda.stub.UdaRpcService/GetUdaObjects',
                request_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaObjectsArg.SerializeToString,
                response_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaObjectsResult.FromString,
                _registered_method=True)
        self.UdaRequestResourceUsage = channel.unary_unary(
                '/cohesity.magneto.agents.uda.stub.UdaRpcService/UdaRequestResourceUsage',
                request_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.UdaRequestResourceUsageArg.SerializeToString,
                response_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.UdaRequestResourceUsageResult.FromString,
                _registered_method=True)
        self.SendUdaEntities = channel.unary_unary(
                '/cohesity.magneto.agents.uda.stub.UdaRpcService/SendUdaEntities',
                request_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.SendUdaEntitiesArg.SerializeToString,
                response_deserializer=magneto_dot_agents_dot_stub_dot_agent__base__pb2.Result.FromString,
                _registered_method=True)
        self.UdaPreJobRunTasks = channel.unary_unary(
                '/cohesity.magneto.agents.uda.stub.UdaRpcService/UdaPreJobRunTasks',
                request_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.UdaPreJobRunTasksArg.SerializeToString,
                response_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.UdaPreJobRunTasksResult.FromString,
                _registered_method=True)
        self.StartUdaBackup = channel.unary_unary(
                '/cohesity.magneto.agents.uda.stub.UdaRpcService/StartUdaBackup',
                request_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.StartUdaBackupArg.SerializeToString,
                response_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.StartUdaBackupResult.FromString,
                _registered_method=True)
        self.GetUdaJobStatus = channel.unary_unary(
                '/cohesity.magneto.agents.uda.stub.UdaRpcService/GetUdaJobStatus',
                request_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaJobStatusArg.SerializeToString,
                response_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaJobStatusResult.FromString,
                _registered_method=True)
        self.GetUdaBackupDetails = channel.unary_unary(
                '/cohesity.magneto.agents.uda.stub.UdaRpcService/GetUdaBackupDetails',
                request_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaBackupDetailsArg.SerializeToString,
                response_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaBackupDetailsResult.FromString,
                _registered_method=True)
        self.CancelUdaJob = channel.unary_unary(
                '/cohesity.magneto.agents.uda.stub.UdaRpcService/CancelUdaJob',
                request_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.CancelUdaJobArg.SerializeToString,
                response_deserializer=magneto_dot_agents_dot_stub_dot_agent__base__pb2.Result.FromString,
                _registered_method=True)
        self.StartUdaRestore = channel.unary_unary(
                '/cohesity.magneto.agents.uda.stub.UdaRpcService/StartUdaRestore',
                request_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.StartUdaRestoreArg.SerializeToString,
                response_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.StartUdaRestoreResult.FromString,
                _registered_method=True)
        self.GetUdaRestoreDetails = channel.unary_unary(
                '/cohesity.magneto.agents.uda.stub.UdaRpcService/GetUdaRestoreDetails',
                request_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaRestoreDetailsArg.SerializeToString,
                response_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaRestoreDetailsResult.FromString,
                _registered_method=True)
        self.MountUdaView = channel.unary_unary(
                '/cohesity.magneto.agents.uda.stub.UdaRpcService/MountUdaView',
                request_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.MountUdaViewArg.SerializeToString,
                response_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.MountUdaViewResult.FromString,
                _registered_method=True)
        self.UnmountUdaView = channel.unary_unary(
                '/cohesity.magneto.agents.uda.stub.UdaRpcService/UnmountUdaView',
                request_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.UnmountUdaViewArg.SerializeToString,
                response_deserializer=magneto_dot_agents_dot_stub_dot_agent__base__pb2.Result.FromString,
                _registered_method=True)
        self.CleanupUdaJob = channel.unary_unary(
                '/cohesity.magneto.agents.uda.stub.UdaRpcService/CleanupUdaJob',
                request_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.CleanupUdaJobArg.SerializeToString,
                response_deserializer=magneto_dot_agents_dot_stub_dot_agent__base__pb2.Result.FromString,
                _registered_method=True)


class UdaRpcServiceServicer(object):
    """-----------------------------------------------------------------------------

    """

    def DiscoverUdaSource(self, request, context):
        """Discover the source.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyUdaSource(self, request, context):
        """Verify the source.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUdaObjects(self, request, context):
        """Get the source objects.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UdaRequestResourceUsage(self, request, context):
        """Get resource usage.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendUdaEntities(self, request, context):
        """Send the entities to source for backup/restore.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UdaPreJobRunTasks(self, request, context):
        """Start pre job run script.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartUdaBackup(self, request, context):
        """Start backup of the source objects.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUdaJobStatus(self, request, context):
        """Get the status of a Uda job.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUdaBackupDetails(self, request, context):
        """Get the details of a completed backup job.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelUdaJob(self, request, context):
        """Cancel a running UDA job.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartUdaRestore(self, request, context):
        """Start the restore of source objects.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUdaRestoreDetails(self, request, context):
        """Get the details of a completed restore job.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MountUdaView(self, request, context):
        """Mount a view. Can be used to mount multiple vips
        of a single view.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnmountUdaView(self, request, context):
        """Unmount the paths in UnmountUdaViewArg.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CleanupUdaJob(self, request, context):
        """Do cleanup after UDA job deletion.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UdaRpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DiscoverUdaSource': grpc.unary_unary_rpc_method_handler(
                    servicer.DiscoverUdaSource,
                    request_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.DiscoverUdaSourceArg.FromString,
                    response_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.DiscoverUdaSourceResult.SerializeToString,
            ),
            'VerifyUdaSource': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyUdaSource,
                    request_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.VerifyUdaSourceArg.FromString,
                    response_serializer=magneto_dot_agents_dot_stub_dot_agent__base__pb2.Result.SerializeToString,
            ),
            'GetUdaObjects': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUdaObjects,
                    request_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaObjectsArg.FromString,
                    response_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaObjectsResult.SerializeToString,
            ),
            'UdaRequestResourceUsage': grpc.unary_unary_rpc_method_handler(
                    servicer.UdaRequestResourceUsage,
                    request_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.UdaRequestResourceUsageArg.FromString,
                    response_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.UdaRequestResourceUsageResult.SerializeToString,
            ),
            'SendUdaEntities': grpc.unary_unary_rpc_method_handler(
                    servicer.SendUdaEntities,
                    request_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.SendUdaEntitiesArg.FromString,
                    response_serializer=magneto_dot_agents_dot_stub_dot_agent__base__pb2.Result.SerializeToString,
            ),
            'UdaPreJobRunTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.UdaPreJobRunTasks,
                    request_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.UdaPreJobRunTasksArg.FromString,
                    response_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.UdaPreJobRunTasksResult.SerializeToString,
            ),
            'StartUdaBackup': grpc.unary_unary_rpc_method_handler(
                    servicer.StartUdaBackup,
                    request_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.StartUdaBackupArg.FromString,
                    response_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.StartUdaBackupResult.SerializeToString,
            ),
            'GetUdaJobStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUdaJobStatus,
                    request_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaJobStatusArg.FromString,
                    response_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaJobStatusResult.SerializeToString,
            ),
            'GetUdaBackupDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUdaBackupDetails,
                    request_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaBackupDetailsArg.FromString,
                    response_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaBackupDetailsResult.SerializeToString,
            ),
            'CancelUdaJob': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelUdaJob,
                    request_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.CancelUdaJobArg.FromString,
                    response_serializer=magneto_dot_agents_dot_stub_dot_agent__base__pb2.Result.SerializeToString,
            ),
            'StartUdaRestore': grpc.unary_unary_rpc_method_handler(
                    servicer.StartUdaRestore,
                    request_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.StartUdaRestoreArg.FromString,
                    response_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.StartUdaRestoreResult.SerializeToString,
            ),
            'GetUdaRestoreDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUdaRestoreDetails,
                    request_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaRestoreDetailsArg.FromString,
                    response_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaRestoreDetailsResult.SerializeToString,
            ),
            'MountUdaView': grpc.unary_unary_rpc_method_handler(
                    servicer.MountUdaView,
                    request_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.MountUdaViewArg.FromString,
                    response_serializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.MountUdaViewResult.SerializeToString,
            ),
            'UnmountUdaView': grpc.unary_unary_rpc_method_handler(
                    servicer.UnmountUdaView,
                    request_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.UnmountUdaViewArg.FromString,
                    response_serializer=magneto_dot_agents_dot_stub_dot_agent__base__pb2.Result.SerializeToString,
            ),
            'CleanupUdaJob': grpc.unary_unary_rpc_method_handler(
                    servicer.CleanupUdaJob,
                    request_deserializer=magneto_dot_agents_dot_stub_dot_uda__param__pb2.CleanupUdaJobArg.FromString,
                    response_serializer=magneto_dot_agents_dot_stub_dot_agent__base__pb2.Result.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.magneto.agents.uda.stub.UdaRpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.magneto.agents.uda.stub.UdaRpcService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class UdaRpcService(object):
    """-----------------------------------------------------------------------------

    """

    @staticmethod
    def DiscoverUdaSource(request,
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
            '/cohesity.magneto.agents.uda.stub.UdaRpcService/DiscoverUdaSource',
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.DiscoverUdaSourceArg.SerializeToString,
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.DiscoverUdaSourceResult.FromString,
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
    def VerifyUdaSource(request,
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
            '/cohesity.magneto.agents.uda.stub.UdaRpcService/VerifyUdaSource',
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.VerifyUdaSourceArg.SerializeToString,
            magneto_dot_agents_dot_stub_dot_agent__base__pb2.Result.FromString,
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
    def GetUdaObjects(request,
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
            '/cohesity.magneto.agents.uda.stub.UdaRpcService/GetUdaObjects',
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaObjectsArg.SerializeToString,
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaObjectsResult.FromString,
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
    def UdaRequestResourceUsage(request,
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
            '/cohesity.magneto.agents.uda.stub.UdaRpcService/UdaRequestResourceUsage',
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.UdaRequestResourceUsageArg.SerializeToString,
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.UdaRequestResourceUsageResult.FromString,
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
    def SendUdaEntities(request,
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
            '/cohesity.magneto.agents.uda.stub.UdaRpcService/SendUdaEntities',
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.SendUdaEntitiesArg.SerializeToString,
            magneto_dot_agents_dot_stub_dot_agent__base__pb2.Result.FromString,
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
    def UdaPreJobRunTasks(request,
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
            '/cohesity.magneto.agents.uda.stub.UdaRpcService/UdaPreJobRunTasks',
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.UdaPreJobRunTasksArg.SerializeToString,
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.UdaPreJobRunTasksResult.FromString,
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
    def StartUdaBackup(request,
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
            '/cohesity.magneto.agents.uda.stub.UdaRpcService/StartUdaBackup',
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.StartUdaBackupArg.SerializeToString,
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.StartUdaBackupResult.FromString,
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
    def GetUdaJobStatus(request,
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
            '/cohesity.magneto.agents.uda.stub.UdaRpcService/GetUdaJobStatus',
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaJobStatusArg.SerializeToString,
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaJobStatusResult.FromString,
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
    def GetUdaBackupDetails(request,
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
            '/cohesity.magneto.agents.uda.stub.UdaRpcService/GetUdaBackupDetails',
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaBackupDetailsArg.SerializeToString,
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaBackupDetailsResult.FromString,
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
    def CancelUdaJob(request,
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
            '/cohesity.magneto.agents.uda.stub.UdaRpcService/CancelUdaJob',
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.CancelUdaJobArg.SerializeToString,
            magneto_dot_agents_dot_stub_dot_agent__base__pb2.Result.FromString,
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
    def StartUdaRestore(request,
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
            '/cohesity.magneto.agents.uda.stub.UdaRpcService/StartUdaRestore',
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.StartUdaRestoreArg.SerializeToString,
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.StartUdaRestoreResult.FromString,
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
    def GetUdaRestoreDetails(request,
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
            '/cohesity.magneto.agents.uda.stub.UdaRpcService/GetUdaRestoreDetails',
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaRestoreDetailsArg.SerializeToString,
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.GetUdaRestoreDetailsResult.FromString,
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
    def MountUdaView(request,
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
            '/cohesity.magneto.agents.uda.stub.UdaRpcService/MountUdaView',
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.MountUdaViewArg.SerializeToString,
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.MountUdaViewResult.FromString,
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
    def UnmountUdaView(request,
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
            '/cohesity.magneto.agents.uda.stub.UdaRpcService/UnmountUdaView',
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.UnmountUdaViewArg.SerializeToString,
            magneto_dot_agents_dot_stub_dot_agent__base__pb2.Result.FromString,
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
    def CleanupUdaJob(request,
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
            '/cohesity.magneto.agents.uda.stub.UdaRpcService/CleanupUdaJob',
            magneto_dot_agents_dot_stub_dot_uda__param__pb2.CleanupUdaJobArg.SerializeToString,
            magneto_dot_agents_dot_stub_dot_agent__base__pb2.Result.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)