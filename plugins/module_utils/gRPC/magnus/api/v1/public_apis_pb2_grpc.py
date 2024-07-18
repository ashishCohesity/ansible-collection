# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from magnus.api.v1 import public_vmware_data_pb2 as magnus_dot_api_dot_v1_dot_public__vmware__data__pb2

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
        + f' but the generated code in magnus/api/v1/public_apis_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class MagnusPublicGRPCServiceStub(object):
    """-----------------------------------------------------------------------------
    Magnus public GRPC APIs.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.VMwareDatastoreAction = channel.unary_unary(
                '/cohesity.magnus.api.v1.MagnusPublicGRPCService/VMwareDatastoreAction',
                request_serializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareDatastoreActionArg.SerializeToString,
                response_deserializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareDatastoreActionResult.FromString,
                _registered_method=True)
        self.VMwareDatastoreActionTaskStatus = channel.unary_unary(
                '/cohesity.magnus.api.v1.MagnusPublicGRPCService/VMwareDatastoreActionTaskStatus',
                request_serializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareDatastoreActionTaskStatusArg.SerializeToString,
                response_deserializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareDatastoreActionTaskStatusResult.FromString,
                _registered_method=True)
        self.VMwareVMAction = channel.unary_unary(
                '/cohesity.magnus.api.v1.MagnusPublicGRPCService/VMwareVMAction',
                request_serializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareVMActionArg.SerializeToString,
                response_deserializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareVMActionResult.FromString,
                _registered_method=True)
        self.VMwareVMActionTaskStatus = channel.unary_unary(
                '/cohesity.magnus.api.v1.MagnusPublicGRPCService/VMwareVMActionTaskStatus',
                request_serializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareVMActionTaskStatusArg.SerializeToString,
                response_deserializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareVMActionTaskStatusResult.FromString,
                _registered_method=True)


class MagnusPublicGRPCServiceServicer(object):
    """-----------------------------------------------------------------------------
    Magnus public GRPC APIs.
    """

    def VMwareDatastoreAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VMwareDatastoreActionTaskStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VMwareVMAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VMwareVMActionTaskStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MagnusPublicGRPCServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'VMwareDatastoreAction': grpc.unary_unary_rpc_method_handler(
                    servicer.VMwareDatastoreAction,
                    request_deserializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareDatastoreActionArg.FromString,
                    response_serializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareDatastoreActionResult.SerializeToString,
            ),
            'VMwareDatastoreActionTaskStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.VMwareDatastoreActionTaskStatus,
                    request_deserializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareDatastoreActionTaskStatusArg.FromString,
                    response_serializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareDatastoreActionTaskStatusResult.SerializeToString,
            ),
            'VMwareVMAction': grpc.unary_unary_rpc_method_handler(
                    servicer.VMwareVMAction,
                    request_deserializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareVMActionArg.FromString,
                    response_serializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareVMActionResult.SerializeToString,
            ),
            'VMwareVMActionTaskStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.VMwareVMActionTaskStatus,
                    request_deserializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareVMActionTaskStatusArg.FromString,
                    response_serializer=magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareVMActionTaskStatusResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.magnus.api.v1.MagnusPublicGRPCService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.magnus.api.v1.MagnusPublicGRPCService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MagnusPublicGRPCService(object):
    """-----------------------------------------------------------------------------
    Magnus public GRPC APIs.
    """

    @staticmethod
    def VMwareDatastoreAction(request,
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
            '/cohesity.magnus.api.v1.MagnusPublicGRPCService/VMwareDatastoreAction',
            magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareDatastoreActionArg.SerializeToString,
            magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareDatastoreActionResult.FromString,
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
    def VMwareDatastoreActionTaskStatus(request,
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
            '/cohesity.magnus.api.v1.MagnusPublicGRPCService/VMwareDatastoreActionTaskStatus',
            magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareDatastoreActionTaskStatusArg.SerializeToString,
            magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareDatastoreActionTaskStatusResult.FromString,
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
    def VMwareVMAction(request,
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
            '/cohesity.magnus.api.v1.MagnusPublicGRPCService/VMwareVMAction',
            magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareVMActionArg.SerializeToString,
            magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareVMActionResult.FromString,
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
    def VMwareVMActionTaskStatus(request,
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
            '/cohesity.magnus.api.v1.MagnusPublicGRPCService/VMwareVMActionTaskStatus',
            magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareVMActionTaskStatusArg.SerializeToString,
            magnus_dot_api_dot_v1_dot_public__vmware__data__pb2.VMwareVMActionTaskStatusResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)