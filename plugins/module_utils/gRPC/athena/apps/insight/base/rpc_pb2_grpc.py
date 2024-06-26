# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from athena.apps.insight.base import rpc_pb2 as athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2
from athena.apps.insight.base import task_pb2 as athena_dot_apps_dot_insight_dot_base_dot_task__pb2

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
        + f' but the generated code in athena/apps/insight/base/rpc_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class CrawlerStub(object):
    """----------------------------------------------------------------------------

    --------------------------------------------------------------------------
    Minion --> Master messages.
    --------------------------------------------------------------------------
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Heartbeat = channel.unary_unary(
                '/base.Crawler/Heartbeat',
                request_serializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.HeartbeatArg.SerializeToString,
                response_deserializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.HeartbeatResult.FromString,
                _registered_method=True)
        self.ExecuteSubTasks = channel.unary_unary(
                '/base.Crawler/ExecuteSubTasks',
                request_serializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.ExecuteSubTasksArg.SerializeToString,
                response_deserializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.ExecuteSubTasksResult.FromString,
                _registered_method=True)
        self.ListSubTasks = channel.unary_stream(
                '/base.Crawler/ListSubTasks',
                request_serializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.ListSubTasksArg.SerializeToString,
                response_deserializer=athena_dot_apps_dot_insight_dot_base_dot_task__pb2.SubTaskStateProto.FromString,
                _registered_method=True)
        self.GetObjectConfig = channel.unary_unary(
                '/base.Crawler/GetObjectConfig',
                request_serializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.GetObjectConfigArg.SerializeToString,
                response_deserializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.GetObjectConfigResult.FromString,
                _registered_method=True)
        self.NotifyObjectConfigChange = channel.unary_unary(
                '/base.Crawler/NotifyObjectConfigChange',
                request_serializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.NotifyObjectConfigChangeArg.SerializeToString,
                response_deserializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.NotifyObjectConfigChangeResult.FromString,
                _registered_method=True)


class CrawlerServicer(object):
    """----------------------------------------------------------------------------

    --------------------------------------------------------------------------
    Minion --> Master messages.
    --------------------------------------------------------------------------
    """

    def Heartbeat(self, request, context):
        """Each minion must periodically send a heartbeat to Master.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteSubTasks(self, request, context):
        """--------------------------------------------------------------------------
        Master --> Minion messages.
        --------------------------------------------------------------------------

        - Start executing the given sub-tasks (if not already running).
        - Optionally stop the ones that are not in the list (and delete all traces
        of them).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSubTasks(self, request, context):
        """Return the current state of all known sub-tasks (running or finished).
        TODO(anirvan): Perhaps we don't need the streaming RPC (because the number
        of sub-tasks in a minion's state at any given instant would be small
        enough to be sent back as part of the RPC result. Revisit this.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObjectConfig(self, request, context):
        """--------------------------------------------------------------------------
        Master --> ApiServer messages.
        --------------------------------------------------------------------------

        Returns the configuration configured by the user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NotifyObjectConfigChange(self, request, context):
        """--------------------------------------------------------------------------
        ApiServer --> Master messages.
        --------------------------------------------------------------------------

        Api server sends the following message whenever the user config is
        updated by the user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CrawlerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Heartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.Heartbeat,
                    request_deserializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.HeartbeatArg.FromString,
                    response_serializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.HeartbeatResult.SerializeToString,
            ),
            'ExecuteSubTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteSubTasks,
                    request_deserializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.ExecuteSubTasksArg.FromString,
                    response_serializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.ExecuteSubTasksResult.SerializeToString,
            ),
            'ListSubTasks': grpc.unary_stream_rpc_method_handler(
                    servicer.ListSubTasks,
                    request_deserializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.ListSubTasksArg.FromString,
                    response_serializer=athena_dot_apps_dot_insight_dot_base_dot_task__pb2.SubTaskStateProto.SerializeToString,
            ),
            'GetObjectConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjectConfig,
                    request_deserializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.GetObjectConfigArg.FromString,
                    response_serializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.GetObjectConfigResult.SerializeToString,
            ),
            'NotifyObjectConfigChange': grpc.unary_unary_rpc_method_handler(
                    servicer.NotifyObjectConfigChange,
                    request_deserializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.NotifyObjectConfigChangeArg.FromString,
                    response_serializer=athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.NotifyObjectConfigChangeResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'base.Crawler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('base.Crawler', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Crawler(object):
    """----------------------------------------------------------------------------

    --------------------------------------------------------------------------
    Minion --> Master messages.
    --------------------------------------------------------------------------
    """

    @staticmethod
    def Heartbeat(request,
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
            '/base.Crawler/Heartbeat',
            athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.HeartbeatArg.SerializeToString,
            athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.HeartbeatResult.FromString,
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
    def ExecuteSubTasks(request,
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
            '/base.Crawler/ExecuteSubTasks',
            athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.ExecuteSubTasksArg.SerializeToString,
            athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.ExecuteSubTasksResult.FromString,
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
    def ListSubTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/base.Crawler/ListSubTasks',
            athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.ListSubTasksArg.SerializeToString,
            athena_dot_apps_dot_insight_dot_base_dot_task__pb2.SubTaskStateProto.FromString,
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
    def GetObjectConfig(request,
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
            '/base.Crawler/GetObjectConfig',
            athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.GetObjectConfigArg.SerializeToString,
            athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.GetObjectConfigResult.FromString,
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
    def NotifyObjectConfigChange(request,
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
            '/base.Crawler/NotifyObjectConfigChange',
            athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.NotifyObjectConfigChangeArg.SerializeToString,
            athena_dot_apps_dot_insight_dot_base_dot_rpc__pb2.NotifyObjectConfigChangeResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
