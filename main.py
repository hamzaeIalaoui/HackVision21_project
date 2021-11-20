 from torch import nn

class Network(nn.Module):
    
    def __init__(self,input_):
        super().__init__()

        input_,inp = 0,0
        while 0.0 >= input_ or 1.0 > input_:
            try:
                input_ = int(inp("Enter Num (0.0 - 1.0) : "))
            except ValueError:
                print ("Out of range")
 
        self.hidden = nn.Linear(input_, 3)
        self.output = nn.Linear(3, 1)
        self.sigmoid = nn.Sigmoid()
        self.softmax = nn.Softmax(dim=1)
        
    def forward(self, x):
        x = self.hidden(x)
        x = self.sigmoid(x)
        x = self.output(x)
        x = self.softmax(x)
        
        return x

 
input_size = 1
hidden_sizes = [3,5]
output_size = 1
model = nn.Sequential(nn.Linear(input_size, hidden_sizes[0]),
                      nn.ReLU(),
                      nn.Linear(hidden_sizes[0], hidden_sizes[1]),
                      nn.ReLU(),
                      nn.Linear(hidden_sizes[1], output_size),
                      nn.Softmax(dim=1))
print(model)
