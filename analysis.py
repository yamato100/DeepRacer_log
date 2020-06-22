# coding: utf-8

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
from tkinter import filedialog
import os,sys
from pathlib import Path
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
from pathlib import Path
from mpl_toolkits.axes_grid1 import make_axes_locatable
import math

#########################################################
# 参照ボタンのクリック時の処理                            #
#########################################################
def button1_clicked():
    fTyp = [("","*")]
    iDir = os.path.abspath(Path().resolve())
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    file1.set(filepath)
    try:
        df = pd.read_csv(file1.get())
    except:
        messagebox.showerror('error', 'ファイルオープンに失敗しました')

#########################################################
# ログ解析                                               #
######################################################### 
def analysis():
    df = pd.read_csv(file1.get())

    # プロット領域(Figure, Axes)の初期化
    fig = plt.figure(figsize=(10, 10))
    ax1 = fig.add_subplot(331)
    ax2 = fig.add_subplot(334)
    ax3 = fig.add_subplot(337)
    ax4 = fig.add_subplot(332)
    ax5 = fig.add_subplot(335)
    ax6 = fig.add_subplot(338)
    ax7 = fig.add_subplot(333)
    ax8 = fig.add_subplot(336)
    ax9 = fig.add_subplot(339)

    # 3回の走行それぞれのTime, Progressを算出
    time = [0,0,0]
    progress = [0,0,0]
    for i in range(3):
        time_start = df[df['episodes'] == i].time.min()
        time_end = df[df['episodes'] == i].time.max()
        time[i] = time_end - time_start
        progress[i] = df[df['episodes'] == i].current_progress.max()

    # time,progressを表示
    text1 = 'Time:%1.2f \nProgress:%1.2f' %(time[0], progress[0])
    ax1.text(2.5, 2, text1, fontsize=9)
    text2 = 'Time:%1.2f \nProgress:%1.2f' %(time[1], progress[1])
    ax2.text(2.5, 2, text2, fontsize=9)
    text3 = 'Time:%1.2f \nProgress:%1.2f' %(time[2], progress[2])
    ax3.text(2.5, 2, text3, fontsize=9)

    # レース周毎に分裂
    df1 = df[df.episodes == 0]  # 1週目
    df2 = df[df.episodes == 1]  # 2週目
    df3 = df[df.episodes == 2]  # 3週目 

    # 走行軌跡    
    ax1.scatter(df1.x, df1.y)
    ax1.set_title("1st-rap Driving locus")
    ax1.set_xlim(0,8)
    ax1.set_ylim(0,5)
    ax2.scatter(df2.x, df2.y)
    ax2.set_title("2nd-rap Driving locus")
    ax2.set_xlim(0,8)
    ax2.set_ylim(0,5)
    ax3.scatter(df3.x, df3.y)
    ax3.set_title("3rd-rap Driving locus")
    ax3.set_xlim(0,8)
    ax3.set_ylim(0,5)
    
    # 車速
    im4 = ax4.scatter(df1.x, df1.y, marker='o', alpha=0.3, c=df1.speed, cmap=cm.rainbow, vmin=0, vmax=12)
    ax4.set_title("1st-rap Vehicle speed")
    ax4.set_xlim(0,8)
    ax4.set_ylim(0,5)
    plt.colorbar(im4, ax = ax4, orientation = "vertical") 
    im5 = ax5.scatter(df2.x, df2.y, marker='o', alpha=0.3, c=df2.speed, cmap=cm.rainbow, vmin=0, vmax=12)
    ax5.set_title("2nd-rap Vehicle speed")
    ax5.set_xlim(0,8)
    ax5.set_ylim(0,5)
    plt.colorbar(im5, ax = ax5, orientation = "vertical") 
    im6 = ax6.scatter(df3.x, df3.y, marker='o', alpha=0.3, c=df3.speed, cmap=cm.rainbow, vmin=0, vmax=12)
    ax6.set_title("3rd-rap Vehicle speed")
    ax6.set_xlim(0,8)
    ax6.set_ylim(0,5)
    plt.colorbar(im6, ax = ax6, orientation = "vertical") 

    # ステアリング角度
    speed_min=df.speed.min()
    speed_max=df.speed.max()
 
#    plt.figure(figsize=(9.0, 5.0))
    
    # ステアリング角度の大きさによってマーカー種類を変える
    #   -  0.0度(0.00 rad)のときは "○"
    #   - 12.5度(0.22 rad)のときは "△"
    #   - 25.0度(0.44 rad)のときは "×
    
#    df1_st0 = df1[df1['steering'] == 0.0]
#    df1_st1 = df1[df1['steering'].abs() == 0.22]
#    df1_st2 = df1[df1['steering'].abs() == 0.44]
    im7 = ax7.scatter(df1.x, df1.y, marker='$○$', alpha=0.3, c=df1.steering*180/math.pi, cmap=cm.rainbow, vmin=-30, vmax=30)
#    ax7.scatter(df1_st0.x, df1_st0.y, marker='$○$', alpha=0.3, c=df1_st0.speed, cmap=cm.rainbow, vmin=speed_min, vmax=speed_max)
#    ax7.scatter(df1_st1.x, df1_st1.y, marker='$△$', alpha=0.3, c=df1_st1.speed, cmap=cm.rainbow, vmin=speed_min, vmax=speed_max)
#    ax7.scatter(df1_st2.x, df1_st2.y, marker='$×$', alpha=0.3, c=df1_st2.speed, cmap=cm.rainbow, vmin=speed_min, vmax=speed_max)
    ax7.set_title("1st-rap Steering angle")
    ax7.set_xlim(0,8)
    ax7.set_ylim(0,5)
    plt.colorbar(im7, ax = ax7, orientation = "vertical") 

#    df2_st0 = df2[df2['steering'] == 0.0]
#    df2_st1 = df2[df2['steering'].abs() == 0.22]
#    df2_st2 = df2[df2['steering'].abs() == 0.44]
    im8 = ax8.scatter(df2.x, df2.y, marker='$○$', alpha=0.3, c=df2.steering*180/math.pi, cmap=cm.rainbow, vmin=-30, vmax=30)
#    ax8.scatter(df2_st0.x, df2_st0.y, marker='$○$', alpha=0.3, c=df2_st0.speed, cmap=cm.rainbow, vmin=speed_min, vmax=speed_max)
#    ax8.scatter(df2_st1.x, df2_st1.y, marker='$△$', alpha=0.3, c=df2_st1.speed, cmap=cm.rainbow, vmin=speed_min, vmax=speed_max)
#    ax8.scatter(df2_st2.x, df2_st2.y, marker='$×$', alpha=0.3, c=df2_st2.speed, cmap=cm.rainbow, vmin=speed_min, vmax=speed_max)
    ax8.set_title("2nd-rap Steering angle")
    ax8.set_xlim(0,8)
    ax8.set_ylim(0,5)
    plt.colorbar(im8, ax = ax8, orientation = "vertical") 

#    df3_st0 = df3[df3['steering'] == 0.0]
#    df3_st1 = df3[df3['steering'].abs() == 0.22]
#    df3_st2 = df3[df3['steering'].abs() == 0.44]
    im9 = ax9.scatter(df3.x, df3.y, marker='$○$', alpha=0.3, c=df3.steering*180/math.pi, cmap=cm.rainbow, vmin=-30, vmax=30)    
#    ax9.scatter(df3_st0.x, df3_st0.y, marker='$○$', alpha=0.3, c=df3_st0.speed, cmap=cm.rainbow, vmin=speed_min, vmax=speed_max)
#    ax9.scatter(df3_st1.x, df3_st1.y, marker='$△$', alpha=0.3, c=df3_st1.speed, cmap=cm.rainbow, vmin=speed_min, vmax=speed_max)
#    ax9.scatter(df3_st2.x, df3_st2.y, marker='$×$', alpha=0.3, c=df3_st2.speed, cmap=cm.rainbow, vmin=speed_min, vmax=speed_max)
    ax9.set_title("3rd-rap Steering angle")
    ax9.set_xlim(0,8)
    ax9.set_ylim(0,5)
    plt.colorbar(im9, ax = ax9, orientation = "vertical")  

    #plt.colorbar()

    plt.show()


#----- ルートフレームの作成 -----
root = tk.Tk()
root.title("DeepRacer Log Analysis           Ver.1.3")
#root.geometry("470x400")

#----- フレーム1の設定 -----frame1
frame1 = tk.Frame(root)
frame1.pack(fill="x")

# ラベル
s0 = StringVar()
s0.set('<ログファイル選択>')
label0 = ttk.Label(frame1, textvariable=s0)
label0.pack( side='left', padx=5, pady=5 )

#----- フレーム2の設定 -----frame2
frame2 = tk.Frame(root)
frame2.pack(fill="x")

# 表示欄
file1 = StringVar()
file1_entry = ttk.Entry(frame2, textvariable=file1, width=60)
file1_entry.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

# ボタン
# 参照
button1 = ttk.Button(frame2, text=u'参照', command=button1_clicked)
button1.grid(row=1, column=4, columnspan=1, padx=5, pady=5)

#----- フレーム4の設定 -----frame4
frame4 = tk.Frame(root)
frame4.pack(fill="x")

# ラベル
s1 = StringVar()
s1.set('<解析>')
label1 = ttk.Label(frame4, textvariable=s1)
label1.pack( side='left', padx=5, pady=5 )

#----- フレーム3の設定 -----frame3
frame3 = tk.Frame(root)
frame3.pack(fill="x")

# 実行
button3 = ttk.Button(frame3, text=u'実行', command = analysis)
#button3.grid(row=1, column=1, rowspan=2, columnspan=3, sticky=tk.W + tk.E + tk.N + tk.S, padx=10, pady=5)
button3.grid(row=1, column=5, rowspan=2, columnspan=5, sticky=tk.W + tk.E + tk.N + tk.S, padx=20, pady=10)
#button4 = ttk.Button(frame3, text=u'結果', command=result)
#button4.grid(row=1, column=3, rowspan=1, columnspan=2, sticky=tk.W + tk.E + tk.N + tk.S, padx=10, pady=5)
#button5 = ttk.Button(frame3, text=u'ステアリング角度', command=steering_angle)
#button5.grid(row=1, column=5, rowspan=1, columnspan=2, sticky=tk.W + tk.E + tk.N + tk.S, padx=10, pady=5)

#----- アプリケーションの実行 -----
root.mainloop()