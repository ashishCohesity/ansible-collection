# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from nexus.eagle_agent.base import pipe_data_pb2 as nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2

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
        + f' but the generated code in nexus/eagle_agent/base/helios_agent_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class HeliosAgentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProxyControlPlaneApi = channel.unary_unary(
                '/pipe.HeliosAgentService/ProxyControlPlaneApi',
                request_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.ControlPlaneApiRequest.SerializeToString,
                response_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.ControlPlaneApiResponse.FromString,
                _registered_method=True)
        self.SendHeartBeat = channel.unary_unary(
                '/pipe.HeliosAgentService/SendHeartBeat',
                request_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.HeliosServerHeartBeatRequest.SerializeToString,
                response_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.HeliosServerHeartBeatResponse.FromString,
                _registered_method=True)
        self.StartSnapshotDiff = channel.unary_unary(
                '/pipe.HeliosAgentService/StartSnapshotDiff',
                request_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SnapshotDiffRequest.SerializeToString,
                response_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SnapshotDiffResponse.FromString,
                _registered_method=True)
        self.GetSnapshotDiffStatus = channel.unary_unary(
                '/pipe.HeliosAgentService/GetSnapshotDiffStatus',
                request_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SnapshotDiffStatusRequest.SerializeToString,
                response_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SnapshotDiffStatusResponse.FromString,
                _registered_method=True)
        self.GetClusterKey = channel.unary_unary(
                '/pipe.HeliosAgentService/GetClusterKey',
                request_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.GetClusterKeyRequest.SerializeToString,
                response_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.GetClusterKeyResponse.FromString,
                _registered_method=True)
        self.GetMagnetoUpcomingJobsStats = channel.unary_unary(
                '/pipe.HeliosAgentService/GetMagnetoUpcomingJobsStats',
                request_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.GetMagnetoUpcomingJobsStatsRequest.SerializeToString,
                response_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.GetMagnetoUpcomingJobsStatsResponse.FromString,
                _registered_method=True)
        self.SetupClusterForScaling = channel.unary_unary(
                '/pipe.HeliosAgentService/SetupClusterForScaling',
                request_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SetupClusterForScalingRequest.SerializeToString,
                response_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SetupClusterForScalingResponse.FromString,
                _registered_method=True)
        self.TriggerSnapshotSecurityScan = channel.unary_unary(
                '/pipe.HeliosAgentService/TriggerSnapshotSecurityScan',
                request_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.TriggerSnapshotSecurityScanRequest.SerializeToString,
                response_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.TriggerSnapshotSecurityScanResponse.FromString,
                _registered_method=True)


class HeliosAgentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ProxyControlPlaneApi(self, request, context):
        """The rpc used for executing the proxy calls from the iris-mcm server.
        The calls will be proxied to the helios agent on the cluster. The helios
        agent in the cluster will perform the http calls to the iris.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendHeartBeat(self, request, context):
        """Rpc to send heart beat from HELIOS.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartSnapshotDiff(self, request, context):
        """Rpc to get the diff between two snapshots.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSnapshotDiffStatus(self, request, context):
        """Rpc to return the status of a snapshot diff job
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetClusterKey(self, request, context):
        """Rpc to obtain the cluster level encryption key from cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMagnetoUpcomingJobsStats(self, request, context):
        """Rpc method to fetch stats of upcoming protection jobs from magneto.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetupClusterForScaling(self, request, context):
        """Rpc to to setup cluster for the scaling operation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TriggerSnapshotSecurityScan(self, request, context):
        """Rpc to trigger a new security scan
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HeliosAgentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ProxyControlPlaneApi': grpc.unary_unary_rpc_method_handler(
                    servicer.ProxyControlPlaneApi,
                    request_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.ControlPlaneApiRequest.FromString,
                    response_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.ControlPlaneApiResponse.SerializeToString,
            ),
            'SendHeartBeat': grpc.unary_unary_rpc_method_handler(
                    servicer.SendHeartBeat,
                    request_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.HeliosServerHeartBeatRequest.FromString,
                    response_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.HeliosServerHeartBeatResponse.SerializeToString,
            ),
            'StartSnapshotDiff': grpc.unary_unary_rpc_method_handler(
                    servicer.StartSnapshotDiff,
                    request_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SnapshotDiffRequest.FromString,
                    response_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SnapshotDiffResponse.SerializeToString,
            ),
            'GetSnapshotDiffStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSnapshotDiffStatus,
                    request_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SnapshotDiffStatusRequest.FromString,
                    response_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SnapshotDiffStatusResponse.SerializeToString,
            ),
            'GetClusterKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GetClusterKey,
                    request_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.GetClusterKeyRequest.FromString,
                    response_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.GetClusterKeyResponse.SerializeToString,
            ),
            'GetMagnetoUpcomingJobsStats': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMagnetoUpcomingJobsStats,
                    request_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.GetMagnetoUpcomingJobsStatsRequest.FromString,
                    response_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.GetMagnetoUpcomingJobsStatsResponse.SerializeToString,
            ),
            'SetupClusterForScaling': grpc.unary_unary_rpc_method_handler(
                    servicer.SetupClusterForScaling,
                    request_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SetupClusterForScalingRequest.FromString,
                    response_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SetupClusterForScalingResponse.SerializeToString,
            ),
            'TriggerSnapshotSecurityScan': grpc.unary_unary_rpc_method_handler(
                    servicer.TriggerSnapshotSecurityScan,
                    request_deserializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.TriggerSnapshotSecurityScanRequest.FromString,
                    response_serializer=nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.TriggerSnapshotSecurityScanResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pipe.HeliosAgentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('pipe.HeliosAgentService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class HeliosAgentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ProxyControlPlaneApi(request,
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
            '/pipe.HeliosAgentService/ProxyControlPlaneApi',
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.ControlPlaneApiRequest.SerializeToString,
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.ControlPlaneApiResponse.FromString,
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
    def SendHeartBeat(request,
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
            '/pipe.HeliosAgentService/SendHeartBeat',
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.HeliosServerHeartBeatRequest.SerializeToString,
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.HeliosServerHeartBeatResponse.FromString,
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
    def StartSnapshotDiff(request,
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
            '/pipe.HeliosAgentService/StartSnapshotDiff',
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SnapshotDiffRequest.SerializeToString,
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SnapshotDiffResponse.FromString,
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
    def GetSnapshotDiffStatus(request,
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
            '/pipe.HeliosAgentService/GetSnapshotDiffStatus',
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SnapshotDiffStatusRequest.SerializeToString,
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SnapshotDiffStatusResponse.FromString,
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
    def GetClusterKey(request,
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
            '/pipe.HeliosAgentService/GetClusterKey',
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.GetClusterKeyRequest.SerializeToString,
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.GetClusterKeyResponse.FromString,
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
    def GetMagnetoUpcomingJobsStats(request,
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
            '/pipe.HeliosAgentService/GetMagnetoUpcomingJobsStats',
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.GetMagnetoUpcomingJobsStatsRequest.SerializeToString,
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.GetMagnetoUpcomingJobsStatsResponse.FromString,
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
    def SetupClusterForScaling(request,
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
            '/pipe.HeliosAgentService/SetupClusterForScaling',
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SetupClusterForScalingRequest.SerializeToString,
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.SetupClusterForScalingResponse.FromString,
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
    def TriggerSnapshotSecurityScan(request,
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
            '/pipe.HeliosAgentService/TriggerSnapshotSecurityScan',
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.TriggerSnapshotSecurityScanRequest.SerializeToString,
            nexus_dot_eagle__agent_dot_base_dot_pipe__data__pb2.TriggerSnapshotSecurityScanResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
