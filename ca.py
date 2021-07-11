import torch
x = torch.tensor([[1,2,3],[4,4,5,]])
x= x.view(-1, x.size(2))
print(x)