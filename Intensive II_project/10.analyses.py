
import csv
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
#1. 分析bert两个模型的versions的效果
def version_performance(path):
    i = 0
    j = 0
    t = 0
    w = 0
    csv_reader = csv.reader(open(path))
    for line in csv_reader:
        ##large:
        if line[5] == line[1]:
            i += 1 ###large correct
        else:
            j += 1
        if line[6] == line[1]:
            t += 1
        else:
            w +=1
    return i, j,t,w
sg_version_performance = version_performance("/Users/zhoujie/Desktop/paper_project/pl_sva_mask_full_para_duplicate_bert_base.csv")
pl_version_performance = version_performance("/Users/zhoujie/Desktop/paper_project/sg_sva_mask_full_para_duplicate_bert_base.csv")
print(sg_version_performance)
print(pl_version_performance)

###2. len(sent) plot
def len_sent(path1,path2,title):
    tuple_list = []
    dict_z1 = {}
    dict_z2 = {}
    csv_reader1 = csv.reader(open(path1))
    for line in csv_reader1:
        x_sent_len = line[7]
        # x_list.append(x_sent_len)
        if line[5] == line[1]:
            if x_sent_len not in dict_z1:
                dict_z1[x_sent_len] = 1
            else:
                dict_z1[x_sent_len] += 1
    csv_reader2 = csv.reader(open(path2))
    for line in csv_reader2:
        x_sent_len = line[7]
        # x_list.append(x_sent_len)
        if line[5] == line[1]:
            if x_sent_len not in dict_z2:
                dict_z2[x_sent_len] = 1
            else:
                dict_z2[x_sent_len] += 1
    tuple_list1 = list(dict_z1.items())
    tuple_list2 = list(dict_z2.items())
    new_list1= sorted(tuple_list1,key=lambda x:x[0])
    new_list2 = sorted(tuple_list2, key=lambda x: x[0])
    x1_list = [int(tuple[0]) for tuple in new_list1]
    y1_list = [tuple[1] for tuple in new_list1]
    x2_list = [int(tuple[0]) for tuple in new_list2]
    y2_list = [tuple[1] for tuple in new_list2]
    fig, ax = plt.subplots()

    x1_axis = np.array(x1_list)
    y1_axis = np.array(y1_list)
    x2_axis = np.array(x2_list)
    y2_axis = np.array(y2_list)
    # ax.plot(x1_axis, y1_axis, label='sg')
    # ax.plot(x2_axis, y2_axis, label='pl')
    # ax.set_xlabel('x - SL')  # 设置x轴名称 x label
    # ax.set_ylabel('y - Good Prediction Number')
    plt.title(title)
    plt.scatter(x1_axis, y1_axis)
    plt.scatter(x2_axis, y2_axis)
    plt.xlabel("x - SL")
    plt.ylabel("y - Good Prediction Number")

    plt.show()
# len_sent("/Users/zhoujie/Desktop/paper_project/sg_sva_mask_full_para_duplicate_bert_base.csv","/Users/zhoujie/Desktop/paper_project/pl_sva_mask_full_para_duplicate_bert_base.csv","sg-pl SL")

###3. svd plot
def svd(path1,title):
    tuple_list = []
    dict_z1 = {}
    dict_z2 = {}
    csv_reader1 = csv.reader(open(path1))
    for line in csv_reader1:
        svd = line[8]
        # x_list.append(x_sent_len)
        if line[5] == line[1]:
            if svd not in dict_z1:
                dict_z1[svd] = 1
            else:
                dict_z1[svd] += 1
    # csv_reader2 = csv.reader(open(path2))
    # for line in csv_reader2:
    #     svd = line[7]
    #     # x_list.append(x_sent_len)
    #     if line[6] == line[1]:
    #         if svd not in dict_z2:
    #             dict_z2[svd] = 1
    #         else:
    #             dict_z2[svd] += 1
    tuple_list1 = list(dict_z1.items())
    # tuple_list2 = list(dict_z2.items())
    new_list1= sorted(tuple_list1,key=lambda x:x[0])
    # new_list2 = sorted(tuple_list2, key=lambda x: x[0])
    x1_list = [int(tuple[0]) for tuple in new_list1]
    y1_list = [tuple[1] for tuple in new_list1]
    # x2_list = [int(tuple[0]) for tuple in new_list2]
    # y2_list = [tuple[1] for tuple in new_list2]
    fig, ax = plt.subplots()

    x1_axis = np.array(x1_list)
    y1_axis = np.array(y1_list)
    # x2_axis = np.array(x2_list)
    # y2_axis = np.array(y2_list)
    # ax.plot(x1_axis, y1_axis, label='sg')
    # ax.plot(x2_axis, y2_axis, label='pl')
    # ax.set_xlabel('x - SL')  # 设置x轴名称 x label
    # ax.set_ylabel('y - Good Prediction Number')
    plt.title(title)
    plt.scatter(x1_axis, y1_axis)
    # plt.scatter(x2_axis, y2_axis)
    plt.xlabel("x - SVD")
    plt.ylabel("y - Good Prediction Number")

    plt.show()
# svd("/Users/zhoujie/Desktop/paper_project/sg_sva_mask_full_para_duplicate_bert_base.csv","/Users/zhoujie/Desktop/paper_project/pl_sva_mask_full_para_duplicate_bert_base.csv","sg-pl SVD")
# svd("/Users/zhoujie/Desktop/paper_project/sg_sva_mask_full_para_duplicate_bert_base.csv","sg_svd")
# svd("//Users/zhoujie/Desktop/paper_project/pl_sva_mask_full_para_duplicate_bert_base.csv","pl_svd")
# svd("/Users/zhoujie/Desktop/paper_project/all_data.csv","sg-pl SVD")
#

###4. All_NN_BEF plot
def All_NN_BEF(path1,title):
    tuple_list = []
    dict_z1 = {}
    dict_z2 = {}
    csv_reader1 = csv.reader(open(path1))
    for line in csv_reader1:
        svd = line[13]
        # x_list.append(x_sent_len)
        if svd != "none":
            if line[6] == line[1]:
                if svd not in dict_z1:
                    dict_z1[svd] = 1
                else:
                    dict_z1[svd] += 1
    # csv_reader2 = csv.reader(open(path2))
    # for line in csv_reader2:
    #     svd = line[7]
    #     # x_list.append(x_sent_len)
    #     if line[6] == line[1]:
    #         if svd not in dict_z2:
    #             dict_z2[svd] = 1
    #         else:
    #             dict_z2[svd] += 1
    tuple_list1 = list(dict_z1.items())
    # tuple_list2 = list(dict_z2.items())
    new_list1= sorted(tuple_list1,key=lambda x:x[0])
    # new_list2 = sorted(tuple_list2, key=lambda x: x[0])
    x1_list = [int(tuple[0]) for tuple in new_list1]
    y1_list = [tuple[1] for tuple in new_list1]
    # x2_list = [int(tuple[0]) for tuple in new_list2]
    # y2_list = [tuple[1] for tuple in new_list2]
    fig, ax = plt.subplots()

    x1_axis = np.array(x1_list)
    y1_axis = np.array(y1_list)
    # x2_axis = np.array(x2_list)
    # y2_axis = np.array(y2_list)
    # ax.plot(x1_axis, y1_axis, label='sg')
    # ax.plot(x2_axis, y2_axis, label='pl')
    # ax.set_xlabel('x - SL')  # 设置x轴名称 x label
    # ax.set_ylabel('y - Good Prediction Number')
    plt.title(title)
    plt.scatter(x1_axis, y1_axis)
    # plt.scatter(x2_axis, y2_axis)
    plt.xlabel("x - NEAR_NVD")
    plt.ylabel("y - Good Prediction Number")

    plt.show()
# svd("/Users/zhoujie/Desktop/paper_project/sg_sva_mask_full_para_duplicate_bert_base.csv","/Users/zhoujie/Desktop/paper_project/pl_sva_mask_full_para_duplicate_bert_base.csv","sg-pl SVD")
All_NN_BEF("/Users/zhoujie/Desktop/paper_project/sg_sva_mask_full_para_duplicate_bert_base.csv","sg NEAR_NVD")
All_NN_BEF("//Users/zhoujie/Desktop/paper_project/pl_sva_mask_full_para_duplicate_bert_base.csv","pl NEAR_NVD")
All_NN_BEF("/Users/zhoujie/Desktop/paper_project/all_data.csv","sg-pl NEAR_NVD")