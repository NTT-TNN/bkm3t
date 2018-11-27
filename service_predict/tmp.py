# from sklearn.decomposition import PCA
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import pickle
#
# df_train_x = pd.read_csv('data/datatest.csv', header=None)
# df_train_y = pd.read_csv('data/datatest_y.txt', header=None)
# df_test_x = pd.read_csv('data/datatest_test_x.csv', header=None)
# df_test_y = pd.read_csv('data/datatest_test_y.txt', header=None)
#
# print(df_test_x.shape, df_test_y.shape)
#
#
# from sklearn.svm import SVC

model = SVC()
model.fit(df_train_x.values, df_train_y.values)
acc = model.score(df_test_x.values, df_test_y.values)
pickle.dump(model, open('model_saved/svm.model', 'wb'))

# pca = PCA(n_components=2)
# data = pca.fit_transform(df_train_x.values, df_train_y.values)
# plt.scatter(data[:, 0], data[:, 1], c='b')
# plt.show()

#
# # # print(df_train_x.shape)
# # df_train = pd.concat([df_train_x, df_train_y], axis=1)
# # df_train.columns = range(0, 31)
# # print(df_train.shape)
# # df_train = df_train.sort_values(30)
# # index = df_train[30].diff()[df_train[30].diff() != 0].index.values
# # print(index)
# # # print(df_train_y)
# # pca = PCA(n_components=2)
# # data = pca.fit_transform(df_train.loc[:,:31].values)
# # color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
# # print(data.shape)
# # print(df_train.iloc[[0, 1779, 2537, 2758, 3355, 3112], 31])
# #
# # for i, val in enumerate(index[1:]):
# #     plt.scatter(data[index[i]:val, 0], data[index[i]: val, 1], c=color[i], label=df_train.iloc[val, 31])
# #
# # plt.legend()
# # plt.show()



# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.array([1, 1, 2, 3, 2, 0])
# y = np.array([0, 1, 1, 2, 3, 2, 1])
#
#
# plt.plot(x, 'r', label='x')
# plt.plot(y, 'g', label='y')
#
# plt.legend()
# # plt.show()
#
# distances = np.zeros((len(y), len(x)))
# for i in range(len(y)):
#     for j in range(len(x)):
#         distances[i, j] = (x[j] - y[i]) ** 2
#
#
# print(distances)


def dtw()