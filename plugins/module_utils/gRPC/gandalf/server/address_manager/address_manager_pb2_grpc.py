# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from gandalf.server.address_manager import address_manager_pb2 as gandalf_dot_server_dot_address__manager_dot_address__manager__pb2

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
        + f' but the generated code in gandalf/server/address_manager/address_manager_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class AddressManagerRpcServiceStub(object):
    """-----------------------------------------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FetchIpInfo = channel.unary_unary(
                '/cohesity.gandalf.server.AddressManagerRpcService/FetchIpInfo',
                request_serializer=gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.FetchIpInfoArg.SerializeToString,
                response_deserializer=gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.FetchIpInfoResult.FromString,
                _registered_method=True)
        self.PushIpInfo = channel.unary_unary(
                '/cohesity.gandalf.server.AddressManagerRpcService/PushIpInfo',
                request_serializer=gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.PushIpInfoArg.SerializeToString,
                response_deserializer=gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.PushIpInfoResult.FromString,
                _registered_method=True)
        self.Probe = channel.unary_unary(
                '/cohesity.gandalf.server.AddressManagerRpcService/Probe',
                request_serializer=gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.ProbeArg.SerializeToString,
                response_deserializer=gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.ProbeResult.FromString,
                _registered_method=True)


class AddressManagerRpcServiceServicer(object):
    """-----------------------------------------------------------------------------

    """

    def FetchIpInfo(self, request, context):
        """Rpc used by gandalf server to fetch the ip address information from
        another gandalf server. This is used during add node where the newly
        added node fetches the information from another node for bootstrapping and
        before establishing its first gandalf session.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PushIpInfo(self, request, context):
        """Rpc used by gandalf server to push the ip address information to other
        nodes. This is used for handling the cluster ip address changes. One
        gandalf node will get the new ip addresses of all the other nodes from the
        user, and that gandalf will push the info to other nodes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Probe(self, request, context):
        """Rpc used by gandalf server to fetch the information about a remote node.
        During ip address changes, this rpc is used by one gandalf server to
        re-construct the ClusterIpInfoProto for pushing to all the other nodes.
        In steady state, this is used by nodes for probing to discover the gandalf
        master, and keeping the view information updated.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AddressManagerRpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FetchIpInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchIpInfo,
                    request_deserializer=gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.FetchIpInfoArg.FromString,
                    response_serializer=gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.FetchIpInfoResult.SerializeToString,
            ),
            'PushIpInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.PushIpInfo,
                    request_deserializer=gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.PushIpInfoArg.FromString,
                    response_serializer=gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.PushIpInfoResult.SerializeToString,
            ),
            'Probe': grpc.unary_unary_rpc_method_handler(
                    servicer.Probe,
                    request_deserializer=gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.ProbeArg.FromString,
                    response_serializer=gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.ProbeResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.gandalf.server.AddressManagerRpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.gandalf.server.AddressManagerRpcService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AddressManagerRpcService(object):
    """-----------------------------------------------------------------------------

    """

    @staticmethod
    def FetchIpInfo(request,
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
            '/cohesity.gandalf.server.AddressManagerRpcService/FetchIpInfo',
            gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.FetchIpInfoArg.SerializeToString,
            gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.FetchIpInfoResult.FromString,
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
    def PushIpInfo(request,
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
            '/cohesity.gandalf.server.AddressManagerRpcService/PushIpInfo',
            gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.PushIpInfoArg.SerializeToString,
            gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.PushIpInfoResult.FromString,
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
    def Probe(request,
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
            '/cohesity.gandalf.server.AddressManagerRpcService/Probe',
            gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.ProbeArg.SerializeToString,
            gandalf_dot_server_dot_address__manager_dot_address__manager__pb2.ProbeResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
