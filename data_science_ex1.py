from sklearn.datasets import load_digits

digits = load_digits()

print(f'Image data shape: {digits.data.shape}')
print(f'Labeled data shape: {digits.target.shape}')
