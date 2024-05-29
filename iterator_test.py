import grpc
import videostream_pb2
import videostream_pb2_grpc
import cv2
import time

def cam_stream_generator():
    cap = cv2.VideoCapture(0) # 640 480 3
    while True:
        ret, img = cap.read()
        yield img

def main():
    for frame in cam_stream_generator():
        cv2.imshow("Frame", frame)
        cv2.waitKey(33)

if __name__ == "__main__":
    main()
