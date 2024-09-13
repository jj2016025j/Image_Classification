import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
from torchvision import datasets, transforms

# 定義簡單的模型結構 (可以用自編碼器替代)
class SimpleDiffusionModel(nn.Module):
    def __init__(self):
        super(SimpleDiffusionModel, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(64, 32, kernel_size=2, stride=2),
            nn.ReLU(),
            nn.Conv2d(32, 1, kernel_size=3, padding=1),
            nn.Sigmoid()
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

# 定義加入噪音的過程
def add_noise(imgs, noise_level=0.2):
    noise = torch.randn_like(imgs) * noise_level
    noisy_imgs = imgs + noise
    return torch.clamp(noisy_imgs, 0., 1.)

# 定義去噪過程
def train_model(model, train_loader, optimizer, criterion, epochs=10):
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for imgs, _ in train_loader:
            noisy_imgs = add_noise(imgs)
            optimizer.zero_grad()
            output = model(noisy_imgs)
            loss = criterion(output, imgs)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        print(f"Epoch [{epoch+1}/{epochs}], Loss: {running_loss / len(train_loader):.4f}")

# 加載數據集 (MNIST)
transform = transforms.Compose([transforms.ToTensor()])
train_data = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
train_loader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)

# 初始化模型、優化器和損失函數
model = SimpleDiffusionModel()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.MSELoss()

# 訓練模型
train_model(model, train_loader, optimizer, criterion, epochs=10)

# 測試並顯示結果
def show_images(imgs, noisy_imgs, denoised_imgs, n=5):
    plt.figure(figsize=(15, 5))
    for i in range(n):
        # 原始圖片
        plt.subplot(3, n, i + 1)
        plt.imshow(imgs[i].squeeze().cpu().numpy(), cmap='gray')
        plt.title("Original")
        plt.axis('off')

        # 加噪音的圖片
        plt.subplot(3, n, i + 1 + n)
        plt.imshow(noisy_imgs[i].squeeze().cpu().numpy(), cmap='gray')
        plt.title("Noisy")
        plt.axis('off')

        # 去噪後的圖片
        plt.subplot(3, n, i + 1 + 2 * n)
        plt.imshow(denoised_imgs[i].squeeze().cpu().numpy(), cmap='gray')
        plt.title("Denoised")
        plt.axis('off')

    plt.show()

# 從測試集取一些圖像來測試模型
test_data = datasets.MNIST(root='./data', train=False, transform=transform, download=True)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=10, shuffle=True)

# 取得測試集中的一些圖像
imgs, _ = next(iter(test_loader))
noisy_imgs = add_noise(imgs)
denoised_imgs = model(noisy_imgs)

# 顯示原始、加噪音和去噪的圖片
show_images(imgs, noisy_imgs, denoised_imgs)

