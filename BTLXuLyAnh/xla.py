import cv2
import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox

main = tk.Tk()
main.geometry("500x200")
main.title("Geometric Transformation")
win=Label(main, text =" GEOMETRIC TRANSFORMATION",fg='red',font=('times', 15, 'italic bold underline'))
win.place(x=90,y=30)
lb=Label(main, text =" TRANSFORMATION",fg='white',bg='black',heigh= 1,width =18,font=('times', 10, 'italic bold underline'))
lb.place(x=100,y=100)
#number = tk.StringVar()
numberChosen = Combobox(main, width = 12)# Adding Values
numberChosen['values'] = ("Scale", "Rotation", "Shear", "Translation", "Euclidean", "Similarity", "Affine", "Perspective")
numberChosen.place(x=250,y=100)
def click():
    if (numberChosen.get()=="Scale"):
        def nothing1(a):
            print('Chieu dan Fx: ' + str(a/10) + ' lan')
        def nothing2(b):
            print('Chieu dan Fy: ' + str(b/10) + ' lan')
        cv2.namedWindow('Window')
        cv2.createTrackbar('Truc x/10', 'Window', 1, 20, nothing1)
        cv2.createTrackbar('Truc y/10', 'Window', 1, 20, nothing2)
        img = cv2.imread('lena.jpg')
        cv2.imshow('Original', img)
        while True:
            img = cv2.imread('lena.jpg')
            ffx = (cv2.getTrackbarPos('Truc x/10', 'Window'))/10
            ffy = (cv2.getTrackbarPos('Truc y/10', 'Window'))/10
            res1 = cv2.resize(img, None, fx=ffx, fy=ffy, interpolation=cv2.INTER_CUBIC)
            cv2.imshow('Result', res1)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
    elif (numberChosen.get()=="Rotation"):
        def nothing(c):
            print('Hinh xoay ' + str(c) + 'do')
        cv2.namedWindow('Window')
        cv2.createTrackbar('Xoay (do)', 'Window', 0, 360, nothing)
        img = cv2.imread('lena.jpg')
        cv2.imshow('Original', img)
        rows, cols, _ = img.shape
        img = cv2.circle(img, (256, 256), 3, (0, 255, 0), -1)
        while True:
            x = cv2.getTrackbarPos('Xoay (do)', 'Window')
            M = cv2.getRotationMatrix2D((256, 256), x, 1)
            dst = cv2.warpAffine(img, M, (cols, rows))
            cv2.imshow('Resutl', dst)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
    elif (numberChosen.get() == "Shear"):
        def nothing1(a):
            print('Truot ' + str(a/10) + ' lan truc X')
        def nothing2(b):
            print('Truot ' + str(b/10) + ' lan truc Y')
        cv2.namedWindow('Window')
        cv2.createTrackbar('Truot x/10', 'Window', 0, 10, nothing1)
        cv2.createTrackbar('Truot y/10', 'Window', 0, 10, nothing2)
        img = cv2.imread('dt.png')
        cv2.imshow('Original', img)
        rows, cols, _ = img.shape
        while True:
            ffx = (cv2.getTrackbarPos('Truot x/10', 'Window'))/10
            ffy = (cv2.getTrackbarPos('Truot y/10', 'Window'))/10
            M = np.float32([[1, ffx, 0], [ffy, 1, 0]])
            dst = cv2.warpAffine(img, M, (cols, rows))
            cv2.imshow('Result', dst)
            #or
            #plt.imshow(dst)
            #plt.show()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
    elif (numberChosen.get()=="Translation"):
        def nothing1(a):
            print('Dich theo truc X ' + str(a) + ' pixel ')
        def nothing2(b):
            print('Dich theo truc Y ' + str(b) + ' pixel ')
        cv2.namedWindow('Window')
        cv2.createTrackbar('Dich X pixel', 'Window', 0, 600, nothing1)
        cv2.createTrackbar('Dich Y pixel', 'Window', 0, 600, nothing2)
        img = cv2.imread('lena.jpg')
        cv2.imshow('Original', img)
        rows, cols, _ = img.shape
        while True:
            ffx = cv2.getTrackbarPos('Dich X pixel', 'Window')
            ffy = cv2.getTrackbarPos('Dich Y pixel', 'Window')
            M = np.float32([[1, 0, ffx], [0, 1, ffy]])
            dst = cv2.warpAffine(img, M, (cols, rows))
            cv2.imshow('Result', dst)
            #or
            #plt.imshow(dst)
            #plt.show()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
    elif (numberChosen.get()=="Euclidean"):
        def nothing1(a):
            print('Dich theo truc X ' + str(a) + ' pixel ')
        def nothing2(b):
            print('Dich theo truc Y ' + str(b) + ' pixel ')
        def nothing3(c):
            print('Hinh xoay ' + str(c) + ' do')
        cv2.namedWindow('Window')
        cv2.createTrackbar('Dich X pixel', 'Window', 0, 600, nothing1)
        cv2.createTrackbar('Dich Y pixel', 'Window', 0, 600, nothing2)
        cv2.createTrackbar('Xoay (do)', 'Window', 0, 360, nothing3)
        img = cv2.imread('lena.jpg')
        cv2.imshow('Original', img)
        rows, cols, _ = img.shape
        while True:
            ffx = cv2.getTrackbarPos('Dich X pixel', 'Window')
            ffy = cv2.getTrackbarPos('Dich Y pixel', 'Window')
            x = cv2.getTrackbarPos('Xoay (do)', 'Window')
            M = np.float32([[1, 0, ffx], [0, 1, ffy]])
            trunk = cv2.warpAffine(img, M, (cols, rows))
            N = cv2.getRotationMatrix2D((256, 256), x, 1)
            dst = cv2.warpAffine(trunk, N, (cols, rows))
            img = cv2.circle(img, (256-ffx, 256-ffy), 3, (0, 255, 0), -1)
            cv2.imshow('Result', dst)
            #or
            #plt.imshow(dst)
            #plt.show()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
    elif (numberChosen.get()=="Similarity"):
        def nothing1(a):
            print('Dich theo truc X ' + str(a) + ' pixel ')
        def nothing2(b):
            print('Dich theo truc Y ' + str(b) + ' pixel ')
        def nothing3(c):
            print('Hinh xoay ' + str(c) + ' do')
        def nothing4(d):
            print('Chieu dan Fx: ' + str(d/10) + ' lan')
        def nothing5(e):
            print('Chieu dan Fy: ' + str(e/10) + ' lan')
        cv2.namedWindow('Window')
        cv2.createTrackbar('Dich X pixel', 'Window', 0, 600, nothing1)
        cv2.createTrackbar('Dich Y pixel', 'Window', 0, 600, nothing2)
        cv2.createTrackbar('Xoay (do)', 'Window', 0, 360, nothing3)
        cv2.createTrackbar('Truc x/10', 'Window', 1, 20, nothing4)
        cv2.createTrackbar('Truc y/10', 'Window', 1, 20, nothing5)
        img = cv2.imread('lena.jpg')
        cv2.imshow('Original', img)
        rows, cols, _ = img.shape
        while True:
            ffx = cv2.getTrackbarPos('Dich X pixel', 'Window')
            ffy = cv2.getTrackbarPos('Dich Y pixel', 'Window')
            x = cv2.getTrackbarPos('Xoay (do)', 'Window')
            M = np.float32([[1, 0, ffx], [0, 1, ffy]])
            trunk = cv2.warpAffine(img, M, (cols, rows))
            N = cv2.getRotationMatrix2D((256, 256), x, 1)
            dst = cv2.warpAffine(trunk, N, (cols, rows))
            img = cv2.circle(img, (256 - ffx, 256 - ffy), 3, (0, 255, 0), -1)
            y = (cv2.getTrackbarPos('Truc x/10', 'Window')) / 10
            z = (cv2.getTrackbarPos('Truc y/10', 'Window')) / 10
            res1 = cv2.resize(dst, None, fx=y, fy=z, interpolation=cv2.INTER_CUBIC)
            cv2.imshow('Result', res1)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
    elif (numberChosen.get()=="Affine"):
        img = cv2.imread('lena.jpg')
        rows, cols, ch = img.shape
        pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
        pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
        M = cv2.getAffineTransform(pts1, pts2)
        dst = cv2.warpAffine(img, M, (cols, rows))
        img = cv2.circle(img, (50, 50), 10, (0, 255, 0), -1)
        img = cv2.circle(img, (200, 50), 10, (0, 255, 0), -1)
        img = cv2.circle(img, (50, 200), 10, (0, 255, 0), -1)
        dst = cv2.circle(dst, (10, 100), 10, (0, 255, 0), -1)
        dst = cv2.circle(dst, (200, 50), 10, (0, 255, 0), -1)
        dst = cv2.circle(dst, (100, 250), 10, (0, 255, 0), -1)
        cv2.imshow('Original', img)
        cv2.imshow('Result', dst)
        #or
        #plt.subplot(121), plt.imshow(img), plt.title('Input')
        #plt.subplot(122), plt.imshow(dst), plt.title('Output')
        #plt.show()
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif (numberChosen.get()=="Perspective"):
        cap = cv2.VideoCapture('xulyanh.mp4')
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                cv2.circle(frame, (30, 100), 1, (0, 0, 255), -1)
                cv2.circle(frame, (170, 100), 1, (0, 0, 255), -1)
                cv2.circle(frame, (30, 230), 1, (0, 0, 255), -1)
                cv2.circle(frame, (170, 230), 1, (0, 0, 255), -1)
                pts1 = np.float32([[30, 100], [170, 100], [30, 230], [170, 230]])
                pts2 = np.float32([[0, 0], [400, 0], [0, 600], [400, 600]])
                M = cv2.getPerspectiveTransform(pts1, pts2)
                dst = cv2.warpPerspective(frame, M, (400, 600))
                cv2.imshow('Frame', frame)
                cv2.imshow('Result', dst)
            else:
                break
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
B = tk.Button(main, text="Choose", command=click)
B.place(x=350, y=97)
tk.mainloop()
