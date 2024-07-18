# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from scribe.newscribe.stub import stub_internal_pb2 as scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2
from scribe.newscribe.stub import stub_pb2 as scribe_dot_newscribe_dot_stub_dot_stub__pb2

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
        + f' but the generated code in scribe/newscribe/stub/stub_internal_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class RpcServiceInternalStub(object):
    """-----------------------------------------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Accept = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/Accept',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.AcceptArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.AcceptResult.FromString,
                _registered_method=True)
        self.PushChosenValues = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/PushChosenValues',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.PushChosenValuesArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.PushChosenValuesResult.FromString,
                _registered_method=True)
        self.FetchReplicaState = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/FetchReplicaState',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.FetchReplicaStateArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.FetchReplicaStateResult.FromString,
                _registered_method=True)
        self.SendChosenNotifications = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/SendChosenNotifications',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.SendChosenNotificationsArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.SendChosenNotificationsResult.FromString,
                _registered_method=True)
        self.SendBulkChosenNotifications = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/SendBulkChosenNotifications',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.SendBulkChosenNotificationsArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.SendChosenNotificationsResult.FromString,
                _registered_method=True)
        self.SendTransactionChosenNotification = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/SendTransactionChosenNotification',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransactionChosenNotificationArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.SendChosenNotificationsResult.FromString,
                _registered_method=True)
        self.CheckReadyForLiveMigration = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/CheckReadyForLiveMigration',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.CheckReadyForLiveMigrationArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.CheckReadyForLiveMigrationResult.FromString,
                _registered_method=True)
        self.TransferDbRecords = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/TransferDbRecords',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferDbRecordsArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferDbRecordsResult.FromString,
                _registered_method=True)
        self.TransferSstFiles = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/TransferSstFiles',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferSstFilesArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferSstFilesResult.FromString,
                _registered_method=True)
        self.TransferWALRecords = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/TransferWALRecords',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferWALRecordsArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferWALRecordsResult.FromString,
                _registered_method=True)
        self.TransferCaughtupSequencer = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/TransferCaughtupSequencer',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferCaughtupSequencerArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferCaughtupSequencerResult.FromString,
                _registered_method=True)
        self.ListKeysToCatchup = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/ListKeysToCatchup',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.ListKeysToCatchupArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.ListKeysToCatchupResult.FromString,
                _registered_method=True)
        self.GCKeys = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/GCKeys',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.GCKeysArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.GCKeysResult.FromString,
                _registered_method=True)
        self.FetchRows = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/FetchRows',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.FetchRowsArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.FetchRowsResult.FromString,
                _registered_method=True)
        self.ReadRange = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/ReadRange',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__pb2.RangeScanArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__pb2.RangeScanResult.FromString,
                _registered_method=True)
        self.PushRows = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/PushRows',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.PushRowsArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.PushRowsResult.FromString,
                _registered_method=True)
        self.CheckViewVersion = channel.unary_unary(
                '/cohesity.scribe.server.stub.RpcServiceInternal/CheckViewVersion',
                request_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.CheckViewVersionArg.SerializeToString,
                response_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.CheckViewVersionResult.FromString,
                _registered_method=True)


class RpcServiceInternalServicer(object):
    """-----------------------------------------------------------------------------

    """

    def Accept(self, request, context):
        """RPC sent from the bucket leader to a replica node to propose values for
        one or more rows.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PushChosenValues(self, request, context):
        """RPC sent from the bucket leader to a replica node to push chosen values
        for one or more rows.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchReplicaState(self, request, context):
        """RPC sent from the bucket leader to a replica node to fetch replica state
        for one or more rows.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendChosenNotifications(self, request, context):
        """RPC sent from the bucket leader to a replica node to send chosen
        notifications for one or more rows.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendBulkChosenNotifications(self, request, context):
        """RPC sent from the bucket leader to a replica node to send chosen
        notifications for one or more rows.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendTransactionChosenNotification(self, request, context):
        """RPC sent from the scribe instance to a replica node to send chosen
        notifications for rows that are part of a transaction.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckReadyForLiveMigration(self, request, context):
        """RPC sent from from sender of live migration to receiver of live migration
        to check if receiver is ready to receive data for a new bucket.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransferDbRecords(self, request, context):
        """RPC sent between scribe servers to transfer records of the rocksdb for a
        bucket on a view change.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransferSstFiles(self, request, context):
        """RPC sent between scribe servers to transfer sst files of the rocksdb for a
        bucket on a view change.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransferWALRecords(self, request, context):
        """RPC sent between scribe servers to transfer records of WAL for a bucket
        on a view change.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransferCaughtupSequencer(self, request, context):
        """RPC sent between scribe servers to transfer caught up sequencer for a
        bucket on a view change.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListKeysToCatchup(self, request, context):
        """RPC sent by the bucket leader to other replica nodes to learn the list of
        keys the leader has to catch-up.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GCKeys(self, request, context):
        """RPC sent by the default primary to instruct the secondary and tertiary
        nodes to garbage collect the keys.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchRows(self, request, context):
        """RPC sent by the bucket leader to another replica in the view to learn
        about the current state of one or more rows.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadRange(self, request, context):
        """RPC sent by the bucket leader to another replica in the view to fetch a
        range of rows. It is used in the "immediately consistent" range scan and
        the data is reconciled by the leader.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PushRows(self, request, context):
        """RPC sent by the bucket leader to another replica in the view to push
        the current state of one or more rows.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckViewVersion(self, request, context):
        """RPC sent by the bucket leader to another replica in the bucket's current
        or target view to validate that the receiver of rpc is in the same view
        version as the sender.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RpcServiceInternalServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Accept': grpc.unary_unary_rpc_method_handler(
                    servicer.Accept,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.AcceptArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.AcceptResult.SerializeToString,
            ),
            'PushChosenValues': grpc.unary_unary_rpc_method_handler(
                    servicer.PushChosenValues,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.PushChosenValuesArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.PushChosenValuesResult.SerializeToString,
            ),
            'FetchReplicaState': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchReplicaState,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.FetchReplicaStateArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.FetchReplicaStateResult.SerializeToString,
            ),
            'SendChosenNotifications': grpc.unary_unary_rpc_method_handler(
                    servicer.SendChosenNotifications,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.SendChosenNotificationsArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.SendChosenNotificationsResult.SerializeToString,
            ),
            'SendBulkChosenNotifications': grpc.unary_unary_rpc_method_handler(
                    servicer.SendBulkChosenNotifications,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.SendBulkChosenNotificationsArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.SendChosenNotificationsResult.SerializeToString,
            ),
            'SendTransactionChosenNotification': grpc.unary_unary_rpc_method_handler(
                    servicer.SendTransactionChosenNotification,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransactionChosenNotificationArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.SendChosenNotificationsResult.SerializeToString,
            ),
            'CheckReadyForLiveMigration': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckReadyForLiveMigration,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.CheckReadyForLiveMigrationArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.CheckReadyForLiveMigrationResult.SerializeToString,
            ),
            'TransferDbRecords': grpc.unary_unary_rpc_method_handler(
                    servicer.TransferDbRecords,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferDbRecordsArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferDbRecordsResult.SerializeToString,
            ),
            'TransferSstFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.TransferSstFiles,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferSstFilesArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferSstFilesResult.SerializeToString,
            ),
            'TransferWALRecords': grpc.unary_unary_rpc_method_handler(
                    servicer.TransferWALRecords,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferWALRecordsArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferWALRecordsResult.SerializeToString,
            ),
            'TransferCaughtupSequencer': grpc.unary_unary_rpc_method_handler(
                    servicer.TransferCaughtupSequencer,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferCaughtupSequencerArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferCaughtupSequencerResult.SerializeToString,
            ),
            'ListKeysToCatchup': grpc.unary_unary_rpc_method_handler(
                    servicer.ListKeysToCatchup,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.ListKeysToCatchupArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.ListKeysToCatchupResult.SerializeToString,
            ),
            'GCKeys': grpc.unary_unary_rpc_method_handler(
                    servicer.GCKeys,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.GCKeysArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.GCKeysResult.SerializeToString,
            ),
            'FetchRows': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchRows,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.FetchRowsArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.FetchRowsResult.SerializeToString,
            ),
            'ReadRange': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadRange,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__pb2.RangeScanArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__pb2.RangeScanResult.SerializeToString,
            ),
            'PushRows': grpc.unary_unary_rpc_method_handler(
                    servicer.PushRows,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.PushRowsArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.PushRowsResult.SerializeToString,
            ),
            'CheckViewVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckViewVersion,
                    request_deserializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.CheckViewVersionArg.FromString,
                    response_serializer=scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.CheckViewVersionResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.scribe.server.stub.RpcServiceInternal', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.scribe.server.stub.RpcServiceInternal', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RpcServiceInternal(object):
    """-----------------------------------------------------------------------------

    """

    @staticmethod
    def Accept(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/Accept',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.AcceptArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.AcceptResult.FromString,
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
    def PushChosenValues(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/PushChosenValues',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.PushChosenValuesArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.PushChosenValuesResult.FromString,
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
    def FetchReplicaState(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/FetchReplicaState',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.FetchReplicaStateArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.FetchReplicaStateResult.FromString,
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
    def SendChosenNotifications(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/SendChosenNotifications',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.SendChosenNotificationsArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.SendChosenNotificationsResult.FromString,
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
    def SendBulkChosenNotifications(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/SendBulkChosenNotifications',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.SendBulkChosenNotificationsArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.SendChosenNotificationsResult.FromString,
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
    def SendTransactionChosenNotification(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/SendTransactionChosenNotification',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransactionChosenNotificationArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.SendChosenNotificationsResult.FromString,
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
    def CheckReadyForLiveMigration(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/CheckReadyForLiveMigration',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.CheckReadyForLiveMigrationArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.CheckReadyForLiveMigrationResult.FromString,
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
    def TransferDbRecords(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/TransferDbRecords',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferDbRecordsArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferDbRecordsResult.FromString,
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
    def TransferSstFiles(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/TransferSstFiles',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferSstFilesArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferSstFilesResult.FromString,
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
    def TransferWALRecords(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/TransferWALRecords',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferWALRecordsArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferWALRecordsResult.FromString,
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
    def TransferCaughtupSequencer(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/TransferCaughtupSequencer',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferCaughtupSequencerArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.TransferCaughtupSequencerResult.FromString,
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
    def ListKeysToCatchup(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/ListKeysToCatchup',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.ListKeysToCatchupArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.ListKeysToCatchupResult.FromString,
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
    def GCKeys(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/GCKeys',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.GCKeysArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.GCKeysResult.FromString,
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
    def FetchRows(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/FetchRows',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.FetchRowsArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.FetchRowsResult.FromString,
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
    def ReadRange(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/ReadRange',
            scribe_dot_newscribe_dot_stub_dot_stub__pb2.RangeScanArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__pb2.RangeScanResult.FromString,
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
    def PushRows(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/PushRows',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.PushRowsArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.PushRowsResult.FromString,
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
    def CheckViewVersion(request,
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
            '/cohesity.scribe.server.stub.RpcServiceInternal/CheckViewVersion',
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.CheckViewVersionArg.SerializeToString,
            scribe_dot_newscribe_dot_stub_dot_stub__internal__pb2.CheckViewVersionResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)