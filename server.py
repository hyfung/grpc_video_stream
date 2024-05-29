import grpc
import videostream_pb2
import videostream_pb2_grpc
from concurrent import futures
import time
import cv2
import numpy as np

class VideoStreamServicer():
    def __init__(self):
        pass

    def Infer(self, request_iterator, context):
        frame_shape = (640,480,3)
        for request in request_iterator:
            frame = np.frombuffer(request.data, dtype=np.uint8).reshape(frame_shape)
            # print(request.data)
            yield videostream_pb2.Result(data=request.data)
            cv2.imshow("Frame", frame)
            cv2.waitKey(33)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    videostream_pb2_grpc.add_VideoStreamServicer_to_server(VideoStreamServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
