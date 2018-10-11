#本程序用于计时30秒内未再次被识别到的车位并更新其状态
import time

file = open(r'C:\Users\apple\Desktop\test\result.txt','r')
lines = []
for i in file:
    lines.append(i)
file.close()
n = 0
for n in range(0,len(lines)):
    l = str(lines[n])
    num = l[0:3]
    stn = str(num + ' n' + '\n')
    if l[4] == 'y':
        t = str(time.strftime('%Y:%m:%d:%H:%M:%S',time.localtime(time.time())))
        #print( l[6:10] , l[11:13] , l[14:16] , l[17:19] , l[20:22] , l[23:25])
        #print( t[0:4] , t[5:7] , t[8:10] , t[11:13] , t[14:16] , t[17:19])
        ty = int(t[0:4])
        tM = int(t[5:7])
        td = int(t[8:10])
        th = int(t[11:13])
        tm = int(t[14:16])
        ts = int(t[17:19])
        ly = int(l[6:10])
        lM = int(l[11:13])
        ld = int(l[14:16])
        lh = int(l[17:19])
        lm = int(l[20:22])
        ls = int(l[23:25])
        if ty == ly:
            if tM == lM:
                if td == ld:
                    if th == lh:
                        if tm == lm:
                            if ts - ls < 30:
                                n = n+1
                        elif tm == lm + 1:
                            if ts - ls < -30:
                                n = n+1
                            else:
                                lines.pop(n)
                                lines.insert(n,stn)
                                n = n+1
                        else:
                            lines.pop(n)
                            lines.insert(n,stn)
                            n = n+1
                    elif th == lh + 1 or th == lh - 23:
                        if tm == lm - 59:
                            if ts - ls < -30:
                                n = n+1
                            else:
                                lines.pop(n)
                                lines.insert(n,stn)
                                n = n+1
                        else:
                            lines.pop(n)
                            lines.insert(n,stn)
                            n = n+1
                    else:
                        lines.pop(n)
                        lines.insert(n,stn)
                        n = n+1
                elif td == ld + 1:
                    if th == lh - 23:
                        if tm == lm - 59:
                            if ts - ls < -30:
                                n = n+1
                            else:
                                lines.pop(n)
                                lines.insert(n,stn)
                                n = n+1
                        else:
                            lines.pop(n)
                            lines.insert(n,stn)
                            n = n+1
                    else:
                        lines.pop(n)
                        lines.insert(n,stn)
                        n = n+1
                else:
                    lines.pop(n)
                    lines.insert(n,stn)
                    n = n+1
            elif tM == lM + 1:
                if td == ld - 30 or td == ld - 29 or td == ld - 28 or td == ld - 27:
                    if th == lh - 23:
                        if tm == lm - 59:
                            if ts - ls < -30:
                                n = n+1
                            else:
                                lines.pop(n)
                                lines.insert(n,stn)
                                n = n+1
                        else:
                            lines.pop(n)
                            lines.insert(n,stn)
                            n = n+1
                    else:
                        lines.pop(n)
                        lines.insert(n,stn)
                        n = n+1
                else:
                    lines.pop(n)
                    lines.insert(n,stn)
                    n = n+1
            else:
                lines.pop(n)
                lines.insert(n,stn)
                n = n+1
        elif ty == ly + 1:
            if tM == lM - 11:
                if td == ld - 30:
                    if th == lh - 23:
                        if tm == lm - 59:
                            if ts - ls < -30:
                                n = n+1
                            else:
                                lines.pop(n)
                                lines.insert(n,stn)
                                n = n+1
                        else:
                            lines.pop(n)
                            lines.insert(n,stn)
                            n = n+1
                    else:
                        lines.pop(n)
                        lines.insert(n,stn)
                        n = n+1
                else:
                    lines.pop(n)
                    lines.insert(n,stn)
                    n = n+1
            else:
                lines.pop(n)
                lines.insert(n,stn)
                n = n+1
        else:
            lines.pop(n)
            lines.insert(n,stn)
            n = n+1
    else:
        n = n+1
file_write_obj = open(r'C:\Users\apple\Desktop\test\result.txt', 'w')
for var in lines:
    file_write_obj.writelines(var)
file_write_obj.close()
