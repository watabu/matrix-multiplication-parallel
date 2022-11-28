from pyexpat.model import XML_CQUANT_PLUS
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

linestyles = ["-", "--", "-.", ":", 'dashed', 'dashdot', 'dotted',"-", "--", "-.", ":", 'dashed', 'dashdot', 'dotted']

# 横軸のメモリ
xtics = [1, 4, 8, 16, 32, 64, 90]
xtics_log = [1, 2, 4, 8, 16, 32, 64, 128]

# 実行時間をプロットする
def plot_time(xlist,ylist,namelist,xlabel="X",ylabel="Y",savefile=None,title=""):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    for i in range(len(xlist)):
        ln1 = ax1.plot(xlist[i],ylist[i],label=namelist[i],marker="o",linestyle=linestyles[i])

    h1, l1 = ax1.get_legend_handles_labels()
    ax1.grid(color='gainsboro')
    ax1.set_xlabel(f"{xlabel}")
    ax1.set_ylabel(f"{ylabel}")
    #ax1.set_ylim(pow(2,-6),8)
    #ax1.set_xscale("log",base=2)
    #ax1.set_yscale("log",base=2)
    ax1.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0, fontsize=10) 

    ax1.set_xticks(xtics)
    ax1.set_xticklabels(xtics)

    ax1.set_title(f"{title}")
    
    if(savefile!=None):
        plt.savefig(f"{savefile}",dpi=100,bbox_inches='tight')
        print(f"savefig {savefile} ... done")

# 実行時間をプロットする
def plot_time_log(xlist,ylist,namelist,xlabel="X",ylabel="Y",savefile=None,title=""):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    for i in range(len(xlist)):
        ln1 = ax1.plot(xlist[i],ylist[i],label=namelist[i],marker="o",linestyle=linestyles[i])

    h1, l1 = ax1.get_legend_handles_labels()
    ax1.grid(color='gainsboro')
    ax1.set_xlabel(f"{xlabel}")
    ax1.set_ylabel(f"{ylabel}")
    #ax1.set_ylim(pow(2,-7),pow(2,3))
    ax1.set_xscale("log",base=2)
    ax1.set_yscale("log",base=10)
    ax1.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0, fontsize=10) 

    ax1.set_xticks(xtics_log)
    ax1.set_xticklabels(xtics_log)

    ax1.set_title(f"{title}")
    
    if(savefile!=None):
        plt.savefig(f"{savefile}",dpi=100,bbox_inches='tight')
        print(f"savefig {savefile} ... done")

# 速度向上率をプロットする
def plot_speed(xlist,ylist,namelist,xlabel="X",ylabel="Y",savefile=None,title=""):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    for i in range(len(xlist)):
        ln1 = ax1.plot(xlist[i],ylist[i][0]/ylist[i],label=namelist[i],marker="o",linestyle=linestyles[i])

    h1, l1 = ax1.get_legend_handles_labels()
    ax1.grid(color='gainsboro')
    ax1.set_xlabel(f"{xlabel}")
    ax1.set_ylabel(f"{ylabel}")
    ax1.set_xscale("log",base=2)
    ax1.set_yscale("log",base=2)
    #ax1.set_ylim(pow(2,-6),pow(2,5))
    ax1.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0, fontsize=10) 

    ax1.set_xticks(xtics_log)
    ax1.set_xticklabels(xtics_log)
    
    ax1.set_title(f"{title}")
    if(savefile!=None):
        plt.savefig(f"{savefile}",dpi=100,bbox_inches='tight')
        print(f"savefig {savefile} ... done")

# 並列化効率をプロットする
def plot_effi(xlist,ylist,namelist,xlabel="X",ylabel="Y",savefile=None,title=""):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    for i in range(len(xlist)):
        ln1 = ax1.plot(xlist[i],ylist[i][0]/ylist[i]/xlist[i],label=namelist[i],marker="o",linestyle=linestyles[i])

    h1, l1 = ax1.get_legend_handles_labels()
    ax1.grid(color='gainsboro')
    ax1.set_xlabel(f"{xlabel}")
    ax1.set_ylabel(f"{ylabel}")
    #ax1.set_ylim(pow(2,-4),pow(2,1))
    ax1.set_xscale("log",base=2)
    ax1.set_yscale("log",base=10)
    ax1.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0, fontsize=10) 

    ax1.set_xticks(xtics_log)
    ax1.set_xticklabels(xtics_log)

    ax1.set_title(f"{title}")
    if(savefile!=None):
        plt.savefig(f"{savefile}",dpi=100,bbox_inches='tight')
        print(f"savefig {savefile} ... done")

# Usage: python postprocess/make_graph_scaling_strong.py output/scaling_strong.csv 
def main():
    # 入力の受け取り，csvファイルの読み込み-------------------------
    # コマンドライン引数を受け取る
    args = sys.argv

    if len(args) != 2:
        print("Usage: python make_graph_scaling_strong.py weak.csv")
        return -1

    filepath = args[1]
    try:
        df = pd.read_csv(filepath,sep=" ")
    except:
        print("Error: read_csv failed")
        return -1

    #print(df)


    # dataframeを可視化用に加工-------------------------
    len_df = len(df)
    # 並列度は全ての要素で共通
    x = df.columns.tolist()
    x.remove("matrixA")
    x.remove("matrixB")

    xlist = [[int(i) for i in x]]*len_df
    ylist = [0]*len_df
    namelist = [0]*len_df

    for i, data in df.iterrows():
        matrixA = data["matrixA"]
        matrixB = data["matrixB"]
        
        ylist[i] = data.drop(["matrixA","matrixB"]).values
        # ファイル名のみ抽出
        namelist[i] = matrixB.split("/")[-1]


    # plot-------------------------
    id = "plot_strong"
    outputdir="output"
    plot_time(xlist,ylist,namelist,xlabel="Thread num",ylabel="Time[sec]",savefile=f"{outputdir}/{id}_time.png")
    plot_time_log(xlist,ylist,namelist,xlabel="Thread num",ylabel="Time[sec]",savefile=f"{outputdir}/{id}_time_log.png")
    plot_speed(xlist,ylist,namelist,xlabel="Thread num",ylabel="Speed",savefile=f"{outputdir}/{id}_speed.png")
    plot_effi(xlist,ylist,namelist,xlabel="Thread num",ylabel="Efficiency",savefile=f"{outputdir}/{id}_effi.png")


if (__name__ == "__main__"):
    main()


