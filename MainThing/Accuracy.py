from os import system
from telnetlib import X3PAD
Judge=0
DanInt={1:3313}

DanIntSong={1:{1:695, #v3段位物量
               2:621,
               3:718,
               4:1279},

            2:{1:1397,
               2:1090,
               3:805,
               4:1212},

            3:{1:1055,
               2:1489,
               3:1288,
               4:1789},

            4:{1:1865,
               2:1434,
               3:1288,
               4:1839},

            5:{1:1282,
               2:1706,
               3:1473,
               4:1939},

            6:{1:1694,
               2:1636,
               3:1803,
               4:2115},

            7:{1:1701,
               2:1799,
               3:2132,
               4:1899},

            8:{1:2237,
               2:2081,
               3:2280,
               4:2000},

            9:{1:2374,
               2:1889,
               3:2142,
               4:1810},

            10:{1:2034,
                2:1740,
                3:2270,
                4:2166},

            11:{1:1952,
                2:2013,
                3:1953,
                4:2111},

            12:{1:2107,
                2:1953,
                3:2386,
                4:2674},

            13:{1:2518,
                2:2636,
                3:2326,
                4:2511},

            14:{1:2634,
                2:2212,
                3:2336,
                4:2602},

            15:{1:2734,
                2:2417,
                3:3089,
                4:2974},

            16:{1:2483,
                2:2276,
                3:2921,
                4:3194},

            17:{1:2846,
                2:2260,
                3:2333,
                4:3347},

            18:{1:3789,
                2:3663,
                3:2424,
                4:3255},

            19:{1:3888,
                2:3030,
                3:3581,
                4:3700},

            20:{1:2828,
                2:3362,
                3:3393,
                4:5100},

            21:{1:831,
                2:955,
                3:907,
                4:654},
            
            22:{1:1152,
                2:850,
                3:950,
                4:969},
            
            23:{1:1169,
                2:850,
                3:950,
                4:1347},
            
            24:{1:1400,
                2:1402,
                3:1685,
                4:1599},
            
            25:{1:1953,
                2:2250,
                3:2166,
                4:1667},
            
            26:{1:1487,
                2:1424,
                3:1381,
                4:1587},
            
            27:{1:1909,
                2:1814,
                3:1777,
                4:2681},
            
            29:{1:1799,
                2:2023,
                3:2281,
                4:1787},
            
            30:{1:2659,
                2:2188,
                3:2194,
                4:2187},
            
            31:{1:2164,
                2:1952,
                3:1823,
                4:3249},
            
            32:{1:2871,
                2:2024,
                3:1871,
                4:2452},
            
            33:{1:2327,
                2:1593,
                3:2166,
                4:2200},
            
            34:{1:2731,
                2:2653,
                3:2033,
                4:2796},
            
            35:{1:3229,
                2:2731,
                3:2561,
                4:2109},
            
            36:{1:1766,
                2:1861,
                3:3171,
                4:1680},
            
            37:{1:2339,
                2:2461,
                3:2177,
                4:2177},
            
            38:{1:1929,
                2:2380,
                3:2710,
                4:4675},
            
            39:{1:3987,
                2:1874,
                3:4363,
                4:3843},


            40:{1:3468,
                2:3335,
                3:3698,
                4:5061}}


def GetDan(n):
    S1=['1','2','3','4','5','6','7','8','9','10']
    global Judge
    if "v2" in n:                       #如果传入段位含v2则调用v2数据
        target=18
        if "f" in n:
            target=40
        elif "ex" in n:
            Judge = 96
            target = 28
            for a1 in n:
                if a1 in S1:
                    target += int(a1)
        else:
            Judge = 95
            for a1 in n:
                if a1 in S1:
                    target += int(a1)
    elif "v3" in n:                     #如果传入段位含v3则调用v3数据
        target=-3
        if "f" in n:
            Judge = 96
            target = 20
        elif "ex" in n:
            Judge=96
            target=7
            for a1 in n:
                if a1 in S1:
                    target += int(a1)
        else:
            Judge=95
            for a1 in n:
                if a1 in S1:
                    target += int(a1)
    else:                               #默认情况选用v3
        if "f" in n:
            Judge = 96
            target = 20
        elif "ex" in n:
            Judge=96
            target=7
            for a1 in n:
                if a1 in S1:
                    target += int(a1)
        else:
            Judge=95
            target=0
            for a1 in n:
                if a1 in S1:
                    target += int(a1)
    return target

def DongTai(*args):
    a2=int(input("过段标准:"))
    WuLiang_1=int(input("请输入第一首物量"))  
    WuLiang_2=int(input("请输入第二首物量"))  
    WuLiang_3=int(input("请输入第三首物量"))  
    WuLiang_4=int(input("请输入第四首物量"))
    Acc_1=float(input("请输入你第一首的acc:"))
    Acc_2=float(input("请输入你第二首的acc:"))
    Acc_3=float(input("请输入你第三首的acc:"))
    Acc_4=float(input("请输入你第四首的acc:"))
    WuLiang_12=WuLiang_1+WuLiang_2
    WuLiang_123=WuLiang_12+WuLiang_3
    WuLiang_124=WuLiang_1+WuLiang_2+WuLiang_4
    WuLiang_234=WuLiang_2+WuLiang_3+WuLiang_4
    WuLiang_134=WuLiang_1+WuLiang_3+WuLiang_4
    WuLiang_1234=WuLiang_123+WuLiang_4
    QuanZhong_1=Acc_1 / WuLiang_1234
    QuanZhong_2=Acc_2 / WuLiang_1234
    QuanZhong_3=Acc_3 / WuLiang_1234
    QuanZhong_4=Acc_4 / WuLiang_1234
    Result_1=Acc_1
    Result_2=(Acc_2 * WuLiang_12 - Acc_1 * WuLiang_1) / WuLiang_2
    Result_3=(Acc_3 * WuLiang_123 - Acc_2 * WuLiang_12) / WuLiang_3
    Result_4=(Acc_4 * WuLiang_1234 - Acc_3 * WuLiang_123) / WuLiang_4
    print('第一首acc为:',"%.4f" % Result_1 + "%",
          '第二首acc为:',"%.4f" % Result_2 + "%",
          '第三首acc为:',"%.4f" % Result_3 + "%",
          '第四首acc为:',"%.4f" % Result_4 + "%")
    if Acc_4 >= a2:
        print("恭喜过段")
    else:
        print("仍有不足 继续练习")
    system("pause")
    
    



if __name__=="__main__":
    Index=str(input("请输入你想要测算的段位(如未表明v2或v3,则默认为v3):"))
    if  '自' in Index:
        a=DongTai()
    WuLiang_1=DanIntSong[GetDan(Index)][1]  
    WuLiang_2=DanIntSong[GetDan(Index)][2]  
    WuLiang_3=DanIntSong[GetDan(Index)][3]  
    WuLiang_4=DanIntSong[GetDan(Index)][4]
    Acc_1=float(input("请输入你第一首的acc:"))
    Acc_2=float(input("请输入你第二首的acc:"))
    Acc_3=float(input("请输入你第三首的acc:"))
    Acc_4=float(input("请输入你第四首的acc:"))
    WuLiang_12=WuLiang_1+WuLiang_2
    WuLiang_123=WuLiang_12+WuLiang_3
    WuLiang_124=WuLiang_1+WuLiang_2+WuLiang_4
    WuLiang_234=WuLiang_2+WuLiang_3+WuLiang_4
    WuLiang_134=WuLiang_1+WuLiang_3+WuLiang_4
    WuLiang_1234=WuLiang_123+WuLiang_4
    QuanZhong_1=Acc_1 / WuLiang_1234
    QuanZhong_2=Acc_2 / WuLiang_1234
    QuanZhong_3=Acc_3 / WuLiang_1234
    QuanZhong_4=Acc_4 / WuLiang_1234
    Result_1=Acc_1
    Result_2=(Acc_2 * WuLiang_12 - Acc_1 * WuLiang_1) / WuLiang_2
    Result_3=(Acc_3 * WuLiang_123 - Acc_2 * WuLiang_12) / WuLiang_3
    Result_4=(Acc_4 * WuLiang_1234 - Acc_3 * WuLiang_123) / WuLiang_4
    print('第一首acc为:',"%.4f" % Result_1 + "%",
          '第二首acc为:',"%.4f" % Result_2 + "%",
          '第三首acc为:',"%.4f" % Result_3 + "%",
          '第四首acc为:',"%.4f" % Result_4 + "%")
    if Acc_4 >= Judge:
        print("恭喜过段")
    else:
        print("仍有不足 继续练习")
    system("pause")
      


