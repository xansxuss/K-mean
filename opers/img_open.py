import cv2 ,os,argparse

def open_img(name,folder):
    p=os.path.join(folder,name)
    img=cv2.imread(p)
    cv2.namedWindow(name,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name,2000,2000)
    cv2.imshow(name,img)
    cv2.waitKey(0) == ord('q')
    # cv2.waitKey(2000)
    cv2.destroyAllWindows()

def open_video(name,folder):
    p=os.path.join(folder,name)
    cap = cv2.VideoCapture(p)
    while(cap.isOpened()):
        ret, frame = cap.read()

        cv2.imshow(name,frame)
        fps=cap.get(cv2.CAP_PROP_FPS)
        print(fps)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def show_img(name,img):
    cv2.namedWindow(name,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name,2000,2000)
    cv2.imshow(name,img)
    cv2.waitKey(0) == ord('q')
    # cv2.waitKey(2000)
    cv2.destroyAllWindows()

def write_img(out_name,out_img):
    cv2.imwrite(out_name,out_img)
