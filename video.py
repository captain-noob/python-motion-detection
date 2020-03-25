import cv2
from datetime import datetime ,timedelta
# import requests
# import winsound
from playsound import playsound


def camera(frame2,frame1):
    while True:

        diff=cv2.absdiff(frame1,frame2)

        grey = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(grey,(5,5),0)

        _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)

        dilate=cv2.dilate(thresh, None, iterations = 2)

        (cnts, _) =cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


        for contour in cnts:
            (x, y, w, h) = cv2.boundingRect(contour)

            if cv2.contourArea(contour) < 6000:
                continue
            motion=1
            (x, y, w, h) = cv2.boundingRect(contour)
            aaa=cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 3)

            # if cnts is True:
            #     flag=1
            # else:
            #     flag=0
            
            time(motion)



            # print(f'motion : {flag}')

            


        # cv2.imshow('Live Output ',frame2) #live output
        cv2.imshow('intermediate ',frame1)
        
        
        

        frame1= frame2
        ret,frame2 = video.read()
        motion=0
        
        if cv2.waitKey(1) == 27:
            break
            exit()


def exit():
    video.release()
    cv2.destroyAllWindows()



def time(flag):
    now=datetime.now().time() #time now
    motion_time.append(now)
    l=len(motion_time)

    if motion_time:
        if flag == 1:
            
            l=len(motion_time)
            time=motion_time[l-1]
            # print(type(time))
            if ((time)==now):

                motion_time.append(now)
                # print(f'last time {motion_time[l-1]}')
                # print(f'\n now  {now}')
                # print('yes')
            else:
                l=0
                # print(f'last time {motion_time[l-1]}')
                # print(f'\n now  {now}')
                # print('no')

            

            # beepsound() #calling
            # print(f'motion time {motion_time}\n')
            # print(f'what is {df}')
        else:
            l=0
            motion_time.clear()

        
        # print(f'length= {l}')
        if l > 810: # alarm on 30th sec
            print(f"Alert......")
            beepsound()
            df.append(motion_time)




    else:
        # print('not')
        motion_time.append(now)


    
    
        

def beepsound():
    # y=10
    # os.system("echo -n '\a';sleep 0.2;" *y)
    # return()
    # print('\a\a\a')
    # playsound('beep.wav')
    #to play sound in windows
    # frequency = 2500  # Set Frequency To 2500 Hertz
    # duration = 1000  # Set Duration To 1000 ms == 1 second
    # winsound.Beep(frequency, duration)
    playsound('beep.wav')






video = cv2.VideoCapture(0)
ret,frame1= video.read()
ret ,frame2=video.read()
motion=None
motion_time=[]
df=[]
camera(frame2,frame1)
# beepsound()


