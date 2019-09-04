from concurrent import futures
import time
import grpc

import sys
sys.path.append('../')

import trans_grpc_pb2
import trans_grpc_pb2_grpc
from sangfor_trans import get_translate
from sangfor_trans.config import GOOGLE, BAIDU, APP_ID, SECRET_KEY, CRAWL, API


# 实现 proto 文件中定义的 GreeterServicer
class Translater(trans_grpc_pb2_grpc.TranslaterServicer):
   
    def Translate(self, request, context):
        trans_type = request.trans_type or GOOGLE
        mode = request.mode or CRAWL
        # if mode == API:
        app_id = request.app_id or APP_ID
        secret_key = request.secret_key or SECRET_KEY

        from_lang = request.from_lang
        to_lang = request.to_lang
        query_text = request.query_text

        translator = get_translate.GetTranslator(trans_type=trans_type, mode=mode, app_id=app_id, secret_key=secret_key)
        result = translator.translate(from_lang, to_lang, query_text)
        return trans_grpc_pb2.TransReply(result="translation result is: {}".format(result))


def serve():
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    trans_grpc_pb2_grpc.add_TranslaterServicer_to_server(Translater(), server)
    server.add_insecure_port('[::]:50051')
    print("server start...")
    server.start()
    try:
        while True:
            time.sleep(60*60*24) # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()