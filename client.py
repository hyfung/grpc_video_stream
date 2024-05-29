import grpc
import videostream_pb2
import videostream_pb2_grpc
import cv2
import time

def cam_stream_generator():
    counter = 0
    cap = cv2.VideoCapture(0) # 640 480 3
    while True:
        ret, img = cap.read()
        cv2.imshow("Frame", img)
        cv2.waitKey(33)
        serialized_frame = img.tobytes()
        yield videostream_pb2.Frame(data=serialized_frame)
        counter += 1
        # time.sleep(1)

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = videostream_pb2_grpc.VideoStreamStub(channel)
    responses = stub.Infer(cam_stream_generator())
    
    for response in responses:
        pass
        # print(response.data)
    
    time.sleep(1)

if __name__ == "__main__":
    main()
