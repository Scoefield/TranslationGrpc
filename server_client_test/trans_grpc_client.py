import grpc

import sys
sys.path.append('../')

import trans_grpc_pb2
import trans_grpc_pb2_grpc

def run():
    # 连接 rpc 服务器
    channel = grpc.insecure_channel('localhost:50051')
    # 调用 rpc 服务
    stub = trans_grpc_pb2_grpc.TranslaterStub(channel)
    # response = stub.GetTranslate(trans_grpc_pb2.TransRequest(from_lang="auto", to_lang="zh"))
    # print("Greeter client received: " + response.result)

    response = stub.Translate(trans_grpc_pb2.TransRequest(from_lang="auto", to_lang="zh", query_text="hello world"))
    print("Greeter client received: " + response.result)

if __name__ == '__main__':
    run()