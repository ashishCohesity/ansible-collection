# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from gaia.dataplane.api import api_pb2 as gaia_dot_dataplane_dot_api_dot_api__pb2

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
        + f' but the generated code in gaia/dataplane/api/grpc_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class GRpcServiceStub(object):
    """The following mirrors the definitions in RpcService in rpc.proto.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetObjects = channel.unary_unary(
                '/cohesity.gaia.dataplane.api.GRpcService/GetObjects',
                request_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetObjectsArg.SerializeToString,
                response_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetObjectsResult.FromString,
                _registered_method=True)
        self.GetSubObjects = channel.unary_unary(
                '/cohesity.gaia.dataplane.api.GRpcService/GetSubObjects',
                request_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetSubObjectsArg.SerializeToString,
                response_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetSubObjectsResult.FromString,
                _registered_method=True)
        self.ListDocuments = channel.unary_unary(
                '/cohesity.gaia.dataplane.api.GRpcService/ListDocuments',
                request_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.ListDocumentsArg.SerializeToString,
                response_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.ListDocumentsResult.FromString,
                _registered_method=True)
        self.GetDocuments = channel.unary_unary(
                '/cohesity.gaia.dataplane.api.GRpcService/GetDocuments',
                request_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetDocumentsArg.SerializeToString,
                response_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetDocumentsResult.FromString,
                _registered_method=True)
        self.GetConvertedDocuments = channel.unary_unary(
                '/cohesity.gaia.dataplane.api.GRpcService/GetConvertedDocuments',
                request_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetConvertedDocumentsArg.SerializeToString,
                response_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetConvertedDocumentsResult.FromString,
                _registered_method=True)
        self.UpdateCleanupState = channel.unary_unary(
                '/cohesity.gaia.dataplane.api.GRpcService/UpdateCleanupState',
                request_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.UpdateCleanupStateArg.SerializeToString,
                response_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.UpdateCleanupStateResult.FromString,
                _registered_method=True)
        self.IndexDocuments = channel.unary_unary(
                '/cohesity.gaia.dataplane.api.GRpcService/IndexDocuments',
                request_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.IndexDocumentsArg.SerializeToString,
                response_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.IndexDocumentsResult.FromString,
                _registered_method=True)
        self.GetIndexingStatus = channel.unary_unary(
                '/cohesity.gaia.dataplane.api.GRpcService/GetIndexingStatus',
                request_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetIndexingStatusArg.SerializeToString,
                response_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetIndexingStatusResult.FromString,
                _registered_method=True)
        self.ReportIndexingStatus = channel.unary_unary(
                '/cohesity.gaia.dataplane.api.GRpcService/ReportIndexingStatus',
                request_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.ReportIndexingStatusArg.SerializeToString,
                response_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.ReportIndexingStatusResult.FromString,
                _registered_method=True)
        self.CancelIndexing = channel.unary_unary(
                '/cohesity.gaia.dataplane.api.GRpcService/CancelIndexing',
                request_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.CancelIndexingArg.SerializeToString,
                response_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.CancelIndexingResult.FromString,
                _registered_method=True)


class GRpcServiceServicer(object):
    """The following mirrors the definitions in RpcService in rpc.proto.
    """

    def GetObjects(self, request, context):
        """Returns the objects available in Cohesity Data Cloud.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSubObjects(self, request, context):
        """Returns the sub objects in the goven object.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDocuments(self, request, context):
        """Returns the specified list of documents available in Cohesity Data Cloud.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDocuments(self, request, context):
        """Returns the specified documents available in Cohesity Data Cloud.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConvertedDocuments(self, request, context):
        """Returns the specified documents after converting them to plain text.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCleanupState(self, request, context):
        """All the above RPC routines are fielded by the DataAccessor slave.
        UpdateCleanupState is the only one that is fielded by the DataAccessor
        master. It sent by a slave to the master to record cleanup state. In
        case the master detects the slave death, it'll do the cleanup on the
        slave's behalf. Cleanup should be idempotent.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IndexDocuments(self, request, context):
        """
        RPC routines for the Indexer service

        Starts indexing data based on the provided filters. This RPC can be sent
        either to the indexing service master or slave. If the slave_data field is
        not set, then it is assumed to be sent to the master. Otherwise it is
        sent by the master to the slave.

        When sent from the master to the slave, it may be sent redundantly more
        than once. The slave should deal with that. It can be sent redundantly
        upon RPC retries, or it may also be resent by a newly elected master if
        it isn't sure the prior master managed to send it.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIndexingStatus(self, request, context):
        """Get the status of a previously started indexing operation. This is only
        handled by the Indexer master.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReportIndexingStatus(self, request, context):
        """Report on the progress of a prior indexing task. Sent by the Indexer
        slave to the Indexer master.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelIndexing(self, request, context):
        """Cancel an ongoing indexing job/task. This can be sent to either the
        Indexer master or the slave (depending on the task_handle field in the
        arg). The master is the one who sends it to the slave. It is async - the
        cancellation is recorded and will be acted on in the background. But the
        response is returned sooner.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GRpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetObjects': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjects,
                    request_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetObjectsArg.FromString,
                    response_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetObjectsResult.SerializeToString,
            ),
            'GetSubObjects': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSubObjects,
                    request_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetSubObjectsArg.FromString,
                    response_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetSubObjectsResult.SerializeToString,
            ),
            'ListDocuments': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDocuments,
                    request_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.ListDocumentsArg.FromString,
                    response_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.ListDocumentsResult.SerializeToString,
            ),
            'GetDocuments': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDocuments,
                    request_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetDocumentsArg.FromString,
                    response_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetDocumentsResult.SerializeToString,
            ),
            'GetConvertedDocuments': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConvertedDocuments,
                    request_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetConvertedDocumentsArg.FromString,
                    response_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetConvertedDocumentsResult.SerializeToString,
            ),
            'UpdateCleanupState': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCleanupState,
                    request_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.UpdateCleanupStateArg.FromString,
                    response_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.UpdateCleanupStateResult.SerializeToString,
            ),
            'IndexDocuments': grpc.unary_unary_rpc_method_handler(
                    servicer.IndexDocuments,
                    request_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.IndexDocumentsArg.FromString,
                    response_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.IndexDocumentsResult.SerializeToString,
            ),
            'GetIndexingStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIndexingStatus,
                    request_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetIndexingStatusArg.FromString,
                    response_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.GetIndexingStatusResult.SerializeToString,
            ),
            'ReportIndexingStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportIndexingStatus,
                    request_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.ReportIndexingStatusArg.FromString,
                    response_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.ReportIndexingStatusResult.SerializeToString,
            ),
            'CancelIndexing': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelIndexing,
                    request_deserializer=gaia_dot_dataplane_dot_api_dot_api__pb2.CancelIndexingArg.FromString,
                    response_serializer=gaia_dot_dataplane_dot_api_dot_api__pb2.CancelIndexingResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.gaia.dataplane.api.GRpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.gaia.dataplane.api.GRpcService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class GRpcService(object):
    """The following mirrors the definitions in RpcService in rpc.proto.
    """

    @staticmethod
    def GetObjects(request,
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
            '/cohesity.gaia.dataplane.api.GRpcService/GetObjects',
            gaia_dot_dataplane_dot_api_dot_api__pb2.GetObjectsArg.SerializeToString,
            gaia_dot_dataplane_dot_api_dot_api__pb2.GetObjectsResult.FromString,
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
    def GetSubObjects(request,
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
            '/cohesity.gaia.dataplane.api.GRpcService/GetSubObjects',
            gaia_dot_dataplane_dot_api_dot_api__pb2.GetSubObjectsArg.SerializeToString,
            gaia_dot_dataplane_dot_api_dot_api__pb2.GetSubObjectsResult.FromString,
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
    def ListDocuments(request,
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
            '/cohesity.gaia.dataplane.api.GRpcService/ListDocuments',
            gaia_dot_dataplane_dot_api_dot_api__pb2.ListDocumentsArg.SerializeToString,
            gaia_dot_dataplane_dot_api_dot_api__pb2.ListDocumentsResult.FromString,
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
    def GetDocuments(request,
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
            '/cohesity.gaia.dataplane.api.GRpcService/GetDocuments',
            gaia_dot_dataplane_dot_api_dot_api__pb2.GetDocumentsArg.SerializeToString,
            gaia_dot_dataplane_dot_api_dot_api__pb2.GetDocumentsResult.FromString,
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
    def GetConvertedDocuments(request,
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
            '/cohesity.gaia.dataplane.api.GRpcService/GetConvertedDocuments',
            gaia_dot_dataplane_dot_api_dot_api__pb2.GetConvertedDocumentsArg.SerializeToString,
            gaia_dot_dataplane_dot_api_dot_api__pb2.GetConvertedDocumentsResult.FromString,
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
    def UpdateCleanupState(request,
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
            '/cohesity.gaia.dataplane.api.GRpcService/UpdateCleanupState',
            gaia_dot_dataplane_dot_api_dot_api__pb2.UpdateCleanupStateArg.SerializeToString,
            gaia_dot_dataplane_dot_api_dot_api__pb2.UpdateCleanupStateResult.FromString,
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
    def IndexDocuments(request,
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
            '/cohesity.gaia.dataplane.api.GRpcService/IndexDocuments',
            gaia_dot_dataplane_dot_api_dot_api__pb2.IndexDocumentsArg.SerializeToString,
            gaia_dot_dataplane_dot_api_dot_api__pb2.IndexDocumentsResult.FromString,
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
    def GetIndexingStatus(request,
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
            '/cohesity.gaia.dataplane.api.GRpcService/GetIndexingStatus',
            gaia_dot_dataplane_dot_api_dot_api__pb2.GetIndexingStatusArg.SerializeToString,
            gaia_dot_dataplane_dot_api_dot_api__pb2.GetIndexingStatusResult.FromString,
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
    def ReportIndexingStatus(request,
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
            '/cohesity.gaia.dataplane.api.GRpcService/ReportIndexingStatus',
            gaia_dot_dataplane_dot_api_dot_api__pb2.ReportIndexingStatusArg.SerializeToString,
            gaia_dot_dataplane_dot_api_dot_api__pb2.ReportIndexingStatusResult.FromString,
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
    def CancelIndexing(request,
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
            '/cohesity.gaia.dataplane.api.GRpcService/CancelIndexing',
            gaia_dot_dataplane_dot_api_dot_api__pb2.CancelIndexingArg.SerializeToString,
            gaia_dot_dataplane_dot_api_dot_api__pb2.CancelIndexingResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
