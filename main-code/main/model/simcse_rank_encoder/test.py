import torch
import torch.nn as nn

# a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
# b = torch.tensor([[3, 5], [8, 6]], dtype=torch.float32)
# #
# # loss_fn1 = torch.nn.MSELoss(reduction='none')
# # loss1 = loss_fn1(a*0.05, b)
# # print(loss1)  # 输出结果：tensor([[ 4.,  9.],
# # #                 [25.,  4.]])
# z1=torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
# z2=torch.tensor([[3, 5], [8, 6],[4,5]], dtype=torch.float32)
# a=z1.unsqueeze(1)
# b=z2.unsqueeze(0)
# print(a.size())
# print(b.size())
# c=torch.cosine_similarity(z1,z2)
# print(c)
# import numpy as np
# a=np.array(4,2,9)
# z1 = a[:,0]
# z2=a[:,1]
# print(z1)
# print(z2)


# a=3
# b=5
# c=a+b
# '''
# if a=3:
#    b=2
# '''
# print(c)

import numpy as np
init_list = info_list = [ [[1,2],[2,3],[3,4],[5,6],[7,8]], [[1,3],[1,4],[1,5],[1,6],[1,7]], [[2,4],[2,5],[2,6],[2,7],[2,8]],
                [[3,5],[3,6],[3,7],[3,8],[3,9]], [[4,3],[4,4],[4,5],[4,6],[4,7]], [[5,1],[5,2],[5,3],[5,5],[5,0]] ]
arr_data = np.array(init_list)
print(arr_data[:,0,:])
print("-------")
print(arr_data[:,:,0])

