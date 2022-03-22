import torch.nn as nn


class LSTMClassifier(nn.Module):
    """
    This LSTM model will be used to perform sentiment analysis on /r/wallstreetbets posts.
    """
    
    def __init__(self, embedding_dim, hidden_dim, vocab_size):
        super(LSTMClassifier, self).__init__()
        
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim)
        self.dense1 = nn.Linear(in_features=hidden_dim, out_features=1)
        self.relu = nn.ReLU()
        self.dense2 = nn.Linear(in_features=4, out_features=1)
        self.sig = nn.Sigmoid()
        
        self.word_dict = None
    
    def forward(self, x):
        # TODO: modify so that different numbers of random/target samples can be used
        
        # Data from four comments are passed to the LSTM network. The first comment corresponds 
        # to the target stock for which we'd like to predict a change in the rank popularity while 
        # the following three discuss a random sample of other names at the same time period. The 
        # hidden layer value at the last position on each comment is fed into a dense activation 
        # layer to process the four comments at once. 
        # 
        # Note that lengths is a 4 x batch_size tensor and that indexes the last letter of
        # each post in the example. 
        # TODO: 
        #   - implement approach that allows LSTM to address documents independently
        #   - implement appraoch that spaces documents evenly
        #   - modify to allow different example combinations (e)
        x = x.t()
        batch_size = x.size(1)
        lengths = x[:4]
        reviews = x[4:]
        embeds = self.embedding(reviews)
        lstm_out, _ = self.lstm(embeds)
        out1 = self.dense1(lstm_out)
        out1 = out1[lengths - 1, range(batch_size)]
        out1 = self.relu(out1.squeeze().t())
        out2 = self.dense2(out1)
        return self.sig(out2.squeeze())