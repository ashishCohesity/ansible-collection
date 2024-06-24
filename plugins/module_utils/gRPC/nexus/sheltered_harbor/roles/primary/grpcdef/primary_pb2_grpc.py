# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from nexus.sheltered_harbor.roles.common.proto import grpc_pb2 as nexus_dot_sheltered__harbor_dot_roles_dot_common_dot_proto_dot_grpc__pb2
from nexus.sheltered_harbor.roles.primary.grpcdef import primary_pb2 as nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2

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
        + f' but the generated code in nexus/sheltered_harbor/roles/primary/grpcdef/primary_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class PrimaryStub(object):
    """Primary cluster service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TLSBootstrap = channel.unary_unary(
                '/cohesity.nexus.shelteredharbor.Primary/TLSBootstrap',
                request_serializer=nexus_dot_sheltered__harbor_dot_roles_dot_common_dot_proto_dot_grpc__pb2.TLSBootstrapReq.SerializeToString,
                response_deserializer=nexus_dot_sheltered__harbor_dot_roles_dot_common_dot_proto_dot_grpc__pb2.TLSBootstrapReply.FromString,
                _registered_method=True)
        self.FinancialEntities = channel.unary_stream(
                '/cohesity.nexus.shelteredharbor.Primary/FinancialEntities',
                request_serializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.FinancialEntitiesReq.SerializeToString,
                response_deserializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.FinancialEntity.FromString,
                _registered_method=True)
        self.DataVaultingArchivePrepare = channel.unary_unary(
                '/cohesity.nexus.shelteredharbor.Primary/DataVaultingArchivePrepare',
                request_serializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareReq.SerializeToString,
                response_deserializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareReply.FromString,
                _registered_method=True)
        self.DataVaultingArchivePrepareStatus = channel.unary_unary(
                '/cohesity.nexus.shelteredharbor.Primary/DataVaultingArchivePrepareStatus',
                request_serializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareStatusReq.SerializeToString,
                response_deserializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareStatusReply.FromString,
                _registered_method=True)
        self.DataVaultingArchivePrepareCancel = channel.unary_unary(
                '/cohesity.nexus.shelteredharbor.Primary/DataVaultingArchivePrepareCancel',
                request_serializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareCancelReq.SerializeToString,
                response_deserializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareCancelReply.FromString,
                _registered_method=True)
        self.DataVaultingTransferUpdate = channel.unary_unary(
                '/cohesity.nexus.shelteredharbor.Primary/DataVaultingTransferUpdate',
                request_serializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingTransferUpdateReq.SerializeToString,
                response_deserializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingTransferUpdateReply.FromString,
                _registered_method=True)


class PrimaryServicer(object):
    """Primary cluster service definition.
    """

    def TLSBootstrap(self, request, context):
        """Bootstrap mTLS between Primary and Sheltered Harbor using join token.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FinancialEntities(self, request, context):
        """List registered Financial Entities.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DataVaultingArchivePrepare(self, request, context):
        """Trigger Archive preperation for Data Vaulting.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DataVaultingArchivePrepareStatus(self, request, context):
        """Check status Archive preperation for Data Vaulting.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DataVaultingArchivePrepareCancel(self, request, context):
        """Cancel Archive preperation for Data Vaulting.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DataVaultingTransferUpdate(self, request, context):
        """Update status Data Vaulting for Archive on the Vault.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PrimaryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TLSBootstrap': grpc.unary_unary_rpc_method_handler(
                    servicer.TLSBootstrap,
                    request_deserializer=nexus_dot_sheltered__harbor_dot_roles_dot_common_dot_proto_dot_grpc__pb2.TLSBootstrapReq.FromString,
                    response_serializer=nexus_dot_sheltered__harbor_dot_roles_dot_common_dot_proto_dot_grpc__pb2.TLSBootstrapReply.SerializeToString,
            ),
            'FinancialEntities': grpc.unary_stream_rpc_method_handler(
                    servicer.FinancialEntities,
                    request_deserializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.FinancialEntitiesReq.FromString,
                    response_serializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.FinancialEntity.SerializeToString,
            ),
            'DataVaultingArchivePrepare': grpc.unary_unary_rpc_method_handler(
                    servicer.DataVaultingArchivePrepare,
                    request_deserializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareReq.FromString,
                    response_serializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareReply.SerializeToString,
            ),
            'DataVaultingArchivePrepareStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.DataVaultingArchivePrepareStatus,
                    request_deserializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareStatusReq.FromString,
                    response_serializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareStatusReply.SerializeToString,
            ),
            'DataVaultingArchivePrepareCancel': grpc.unary_unary_rpc_method_handler(
                    servicer.DataVaultingArchivePrepareCancel,
                    request_deserializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareCancelReq.FromString,
                    response_serializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareCancelReply.SerializeToString,
            ),
            'DataVaultingTransferUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.DataVaultingTransferUpdate,
                    request_deserializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingTransferUpdateReq.FromString,
                    response_serializer=nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingTransferUpdateReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.nexus.shelteredharbor.Primary', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.nexus.shelteredharbor.Primary', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Primary(object):
    """Primary cluster service definition.
    """

    @staticmethod
    def TLSBootstrap(request,
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
            '/cohesity.nexus.shelteredharbor.Primary/TLSBootstrap',
            nexus_dot_sheltered__harbor_dot_roles_dot_common_dot_proto_dot_grpc__pb2.TLSBootstrapReq.SerializeToString,
            nexus_dot_sheltered__harbor_dot_roles_dot_common_dot_proto_dot_grpc__pb2.TLSBootstrapReply.FromString,
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
    def FinancialEntities(request,
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
            '/cohesity.nexus.shelteredharbor.Primary/FinancialEntities',
            nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.FinancialEntitiesReq.SerializeToString,
            nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.FinancialEntity.FromString,
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
    def DataVaultingArchivePrepare(request,
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
            '/cohesity.nexus.shelteredharbor.Primary/DataVaultingArchivePrepare',
            nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareReq.SerializeToString,
            nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareReply.FromString,
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
    def DataVaultingArchivePrepareStatus(request,
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
            '/cohesity.nexus.shelteredharbor.Primary/DataVaultingArchivePrepareStatus',
            nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareStatusReq.SerializeToString,
            nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareStatusReply.FromString,
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
    def DataVaultingArchivePrepareCancel(request,
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
            '/cohesity.nexus.shelteredharbor.Primary/DataVaultingArchivePrepareCancel',
            nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareCancelReq.SerializeToString,
            nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingArchivePrepareCancelReply.FromString,
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
    def DataVaultingTransferUpdate(request,
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
            '/cohesity.nexus.shelteredharbor.Primary/DataVaultingTransferUpdate',
            nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingTransferUpdateReq.SerializeToString,
            nexus_dot_sheltered__harbor_dot_roles_dot_primary_dot_grpcdef_dot_primary__pb2.DataVaultingTransferUpdateReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
