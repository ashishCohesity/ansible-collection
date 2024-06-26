# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from athena.apps.vulscanner.go.bootstrapper.base import rpc_pb2 as athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2

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
        + f' but the generated code in athena/apps/vulscanner/go/bootstrapper/base/rpc_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class BootstrapperStub(object):
    """----------------------------------------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PrepareVolume = channel.unary_unary(
                '/cohesity.athena.apps.vulscanner.bootstrapper.base.Bootstrapper/PrepareVolume',
                request_serializer=athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.PrepareVolumeRequest.SerializeToString,
                response_deserializer=athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.PrepareVolumeResult.FromString,
                _registered_method=True)
        self.GetStatus = channel.unary_unary(
                '/cohesity.athena.apps.vulscanner.bootstrapper.base.Bootstrapper/GetStatus',
                request_serializer=athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.GetStatusRequest.SerializeToString,
                response_deserializer=athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.GetStatusResult.FromString,
                _registered_method=True)
        self.DeleteStatus = channel.unary_unary(
                '/cohesity.athena.apps.vulscanner.bootstrapper.base.Bootstrapper/DeleteStatus',
                request_serializer=athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.DeleteStatusRequest.SerializeToString,
                response_deserializer=athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.DeleteStatusResult.FromString,
                _registered_method=True)


class BootstrapperServicer(object):
    """----------------------------------------------------------------------------

    """

    def PrepareVolume(self, request, context):
        """Start prepare volume.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStatus(self, request, context):
        """Status of prepare volume.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteStatus(self, request, context):
        """Remove status of prepare volume for cleanup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BootstrapperServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PrepareVolume': grpc.unary_unary_rpc_method_handler(
                    servicer.PrepareVolume,
                    request_deserializer=athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.PrepareVolumeRequest.FromString,
                    response_serializer=athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.PrepareVolumeResult.SerializeToString,
            ),
            'GetStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatus,
                    request_deserializer=athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.GetStatusRequest.FromString,
                    response_serializer=athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.GetStatusResult.SerializeToString,
            ),
            'DeleteStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteStatus,
                    request_deserializer=athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.DeleteStatusRequest.FromString,
                    response_serializer=athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.DeleteStatusResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.athena.apps.vulscanner.bootstrapper.base.Bootstrapper', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.athena.apps.vulscanner.bootstrapper.base.Bootstrapper', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Bootstrapper(object):
    """----------------------------------------------------------------------------

    """

    @staticmethod
    def PrepareVolume(request,
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
            '/cohesity.athena.apps.vulscanner.bootstrapper.base.Bootstrapper/PrepareVolume',
            athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.PrepareVolumeRequest.SerializeToString,
            athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.PrepareVolumeResult.FromString,
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
    def GetStatus(request,
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
            '/cohesity.athena.apps.vulscanner.bootstrapper.base.Bootstrapper/GetStatus',
            athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.GetStatusRequest.SerializeToString,
            athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.GetStatusResult.FromString,
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
    def DeleteStatus(request,
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
            '/cohesity.athena.apps.vulscanner.bootstrapper.base.Bootstrapper/DeleteStatus',
            athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.DeleteStatusRequest.SerializeToString,
            athena_dot_apps_dot_vulscanner_dot_go_dot_bootstrapper_dot_base_dot_rpc__pb2.DeleteStatusResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
