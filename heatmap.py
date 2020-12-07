#seaborn, pandas, numpy, matplotlib를 pip install해야합니다.
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

#총 3가지 파일이 들어가야합니다
def main():
    #여기에는 숫자로 매칭된 Matrix가 들어가야합니다.
    df = pd.read_csv("D:\\사업개발실(2020) - 복사본\\10월\\UIBR\\홍용찬\\[내부_UIBR] Matrix 코드 공유\\UIBRMatrixReal.txt", header=0, index_col=0)


    col = {}
    #여기에는 Column에 들어갈 병 이름을 교체합니다.
    #예시) MT6176이 옴에 매칭됩니다.
    with open("D:\\사업개발실(2020) - 복사본\\10월\\UIBR\\홍용찬\\[내부_UIBR] Matrix 코드 공유\\UIBRSpecies.txt", encoding = "utf-8") as f:
        for line in f:
            (key,val) = line.split("\t")
            col[key] = val.strip()
    df.rename(col, axis=1, inplace=True)
    
    row = {}
    #여기에는 Column에 들어갈 식물 이름을 교체합니다.
    #예시) T10이 Solanum tuberosum에 매칭됩니다.
    with open("D:\\사업개발실(2020) - 복사본\\10월\\UIBR\\홍용찬\\[내부_UIBR] Matrix 코드 공유\\UIBRName.txt", encoding = "utf-8") as f:
        for line in f:
            (key,val) = line.split("\t")
            row[key] = val.strip()
    df.rename(row, axis=0, inplace=True)

    #전체 df확인
    print(df)


    #7가지 방법
    method = ["single", "average", "complete", "weighted", "centroid", "median", "ward"]
    #10 metrics
    metric = ["euclidean", "minkowski", "cityblock", "seuclidean", "sqeuclidean", "cosine","correlation","hamming","jaccard","chebyshev"]
    #총 70가지 조합
    
    #맑은고딕을 기준으로 하였습니다.
    plt.rcParams['font.family'] =  ['Malgun Gothic']
    mpl.rcParams['axes.unicode_minus'] = False

    sns.set(font='Malgun Gothic', font_scale = 1)

    #ClusterMap이 여기쓰입니다.
    for i in method:
        for j in metric:
            try:
                sns.set(font='Malgun Gothic', font_scale = 0.1)
                cm = sns.clustermap(df, metric=j, standard_scale=1, method=i, cmap="viridis", robust='TRUE', col_cluster=True,row_cluster=True, xticklabels=True, yticklables=True)
                plt.setp(cm.ax_heatmap.yaxis.get_ticklabels(), fontsize = 0.1)
                cm.savefig('D:\\사업개발실(2020) - 복사본\\10월\\UIBR\\홍용찬\\[내부_UIBR] Matrix 코드 공유\\heatmap\\heatmap_'+i+'_'+j+'.png', dpi=800)
            except:
                print("Error"+":"+i+" , "+j)

    
if __name__ == "__main__":
    main()

    