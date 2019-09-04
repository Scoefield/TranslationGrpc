# TranslationGrpc
Use grpc to make translation into a microservice interface

## grpc_proto_tool compile python cmd example
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. helloworld.proto