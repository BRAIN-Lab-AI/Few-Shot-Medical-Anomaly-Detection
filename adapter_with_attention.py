import torch
import torch.nn as nn
import torch.nn.functional as F

class AdapterWithAttention(nn.Module):
    def __init__(self, dim, reduction_factor=16, dropout=0.1):
        super().__init__()
        hidden_dim = dim // reduction_factor  # Reduce dimension for bottleneck

        # MLP part
        self.mlp = nn.Sequential(
            nn.Linear(dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, dim),
        )

        # Attention part
        self.attention = nn.MultiheadAttention(embed_dim=dim, num_heads=4, batch_first=True)

        # Dropout and LayerNorm
        self.dropout = nn.Dropout(dropout)
        self.norm1 = nn.LayerNorm(dim)
        self.norm2 = nn.LayerNorm(dim)

        # Initialize weights properly
        self._init_weights()

    def _init_weights(self):
        # Xavier initialization for better learning
        for module in self.modules():
            if isinstance(module, nn.Linear):
                nn.init.xavier_uniform_(module.weight)
                if module.bias is not None:
                    nn.init.constant_(module.bias, 0)

    def forward(self, x):

        attn_output, _ = self.attention(x, x, x)
        x = x + self.dropout(attn_output)
        x = self.norm1(x)

        # MLP block
        mlp_output = self.mlp(x)
        x = x + self.dropout(mlp_output)
        x = self.norm2(x)

        return x
