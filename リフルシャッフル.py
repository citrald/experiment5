import numpy as np
import random

strage = np.zeros(60,int)
resultstrage = np.zeros(60,int)
evenstrage = np.zeros(30,int)
oddstrage = np.zeros(30,int)

loop = 1
while loop < 16:
    #変数の準備
    print("ループ回数:{0}".format(loop))
    filename = "seed%d.csv" % (loop)
    print("file opne:{0}".format(filename))

    data = np.loadtxt(filename, delimiter=',',comments = '# seed')

    i = 0
    for n in data:
        strage[i] = n
        if loop == 2:
            print("ループ数:{0},位置:{1},値:{2}".format(loop,i,strage[i]))
        i = i + 1

    #リフルシャッフル
    i = 0
    e = 0
    o = 0
    #カード列を上下に分割
    while i < 60:
      if i < 30 :
        oddstrage[i] = strage[i]
      else:
        evenstrage[i-30] = strage[i]
      i = i + 1
    #分割したカード列を連結
    i = 0
    while i < 60:
      if i % 2 == 1:
        resultstrage[i] = oddstrage[e]
        e = e + 1
      else:
        resultstrage[i] = evenstrage[o]
        o = o + 1
      i = i + 1

    
    #結果の出力
    loop = loop + 1
    filename = "seed%d.csv" % (loop)
    np.savetxt(filename, resultstrage,header = 'seed')
    print("data save :{0}".format(filename))
