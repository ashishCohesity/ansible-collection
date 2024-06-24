import grpc
from concurrent import futures
from magneto.agents.stub import agent_rpc_pb2_grpc, agent_param_pb2
from magneto.agents.stub.agent_base_pb2 import AgentBaseArg

class AgentRpcServiceServicer(agent_rpc_pb2_grpc.AgentRpcServiceServicer):
    def GetAgentInfo(self, request, context):
        # Simulate or fetch agent information
        agent_info = agent_param_pb2.AgentInfoProto(
            agent_name="Sample Agent",
            agent_status="Running"
        )
        # Create a response
        response = agent_param_pb2.GetAgentInfoResult(agent_info=agent_info)
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agent_rpc_pb2_grpc.add_AgentRpcServiceServicer_to_server(AgentRpcServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
