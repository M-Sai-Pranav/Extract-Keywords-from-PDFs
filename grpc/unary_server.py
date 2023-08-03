import grpc
from concurrent import futures
import time
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
from pdfExtract import extractData 


class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):  
        #  Step 4 -> Proto Buff call (created in main.js) is being executed here 


        # get the string from the incoming request
        print('entered')
        message = request.message
        result = f'Hello I am up and running received "{message}" message from you'
        print('checking py ------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>> 3')
        result = {'message': result, 'received': True}
        print(result)
        print('checking py ------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>> 2')
        extractData() # Step 5 -> this fuction is being called and navigate to pdfExtract.py file
        return pb2.MessageResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('checking py ------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>> 1')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()