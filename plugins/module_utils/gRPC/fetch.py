import base64
import argparse
import json
import os
from client import FetchFilesArg, AgentBaseArg, GRPCClient


def decode_file_name(encoded_name):
    return base64.b64decode(encoded_name).decode("utf-8")


def main():
    parser = argparse.ArgumentParser(description="Execute RPC call")
    parser.add_argument("rpc", type=str, help="The RPC method to execute")
    args = parser.parse_args()

    grpc_client = GRPCClient()

    if args.rpc == "FetchFilesData":
        # Example encoded file name from the listFiles response
        encoded_file_names = [
            "L2hvbWUvY29oZXNpdHlhZ2VudC9jb2hlc2l0eWFnZW50L2RhdGEvbG9ncy9saW51eF9hZ2VudF9leGVjLnBhcmVudC5sb2NhbGhvc3QubG9jYWxkb21haW4uY29oZXNpdHlhZ2VudC5sb2cuSU5GTy4yMDI0MDYxNC0wOTQ3MjUuMTU3NDMyMg=="
        ]

        # Decode file names
        decoded_file_names = [decode_file_name(name) for name in encoded_file_names]

        # Verify file existence
        for file_name in decoded_file_names:
            if not os.path.exists(file_name):
                print(f"Error: File not found - {file_name}")
                return

        # Create the FetchFilesArg request
        request_data = FetchFilesArg(
            header=AgentBaseArg(
                task_id=-1,
                client_agent_api_version=-1,
                agent_incarnation_id=-1,
                cluster_id=-1,
                cluster_incarnation_id=-1,
            ),
            file_name_vec=[name.encode("utf-8") for name in decoded_file_names],
            offset_bytes=0,
            limit_size_bytes=-1,
        )
        service_method = "FetchFilesData"
        output_file = "FetchFilesData.json"

        response = grpc_client.execute_rpc_call(service_method, request_data)
        response_json = json.loads(response)

        with open(output_file, "w") as f:
            json.dump(response_json, f, indent=4)


if __name__ == "__main__":
    main()
