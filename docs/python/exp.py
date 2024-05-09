from torchvision import datasets, transforms
from torch.utils import data
from torch import nn
import torch
from torch.utils import tensorboard


traning_data = datasets.CIFAR10(root='./data', train=True, download=True,
                                transform=transforms.ToTensor())
testing_data = datasets.CIFAR10(root='./data', train=False, download=True,
                                transform=transforms.ToTensor())
# shape = [3, 32, 32]
traning_loader = data.DataLoader(dataset=traning_data, batch_size=64)
testing_loader = data.DataLoader(dataset=testing_data, batch_size=64)


class Mymodel(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, 5, padding='same'),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 32, 5, padding='same'),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 5, padding='same'),
            nn.MaxPool2d(2),
            nn.Flatten(), # [B64, 64*4*4]
            nn.Linear(64*4*4, 64),
            nn.Linear(64, 10),
        )
    def forward(self, x):
        return self.model(x)



def accu(gts, preds):
    right = (gts == preds.argmax(1)).sum()
    return right/gts.shape[0]





epoch = 10 
lr = 1e-2 # 1 * 10^{-2}
model = Mymodel()
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(params=model.parameters(), lr=lr)

writer = tensorboard.SummaryWriter()


for i in range(epoch):
    traning_loss, mini_batch = 0, 0 

    print(f'----------- EPOCH {i} -----------')
    model.train()
    for data in traning_loader:
        mini_batch += 1
        imgs, gts = data
        preds = model(imgs)

        """
        gts      |  LongTensor
        preds    |  FloatTensor
        """

        loss = loss_fn(preds, gts)
        traning_loss += loss.item()
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if mini_batch % 100 == 0:
            print(accu(gts, preds))
            print(f'the traning loss of {mini_batch} is {loss.item()}')
            writer.add_scalar(f'traning loss{i}', loss.item(), mini_batch)

    writer.add_scalar('traning loss per epoch', traning_loss, i)

    model.eval()
    with torch.no_grad():
        testing_loss, testing_accu  = 0, 0
        for data in testing_loader:
            imgs, gts = data
            preds = model(imgs)
            loss = loss_fn(preds, gts)
            testing_loss += loss.item()
            testing_accu = (testing_accu + accu(gts, preds))/2
            
        print(f'whole testing_loss = {testing_loss}, accu = {testing_accu}')

    writer.add_scalar('testing loss per epoch', testing_loss, i)


    torch.save(model.state_dict(), f'./models/{i}.pth')
writer.close()
