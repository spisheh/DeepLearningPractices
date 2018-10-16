def softmax(x):
    """Calculates the softmax for each row of the input x.
    Workd for a row vector and also for matrices of shape (n, m).
    Argument:
    x -- A numpy matrix of shape (n,m)

    Returns:
    s -- A numpy matrix equal to the softmax of x, of shape (n,m)
    """
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp,axis=1, keepdims = True)
    
    return s


def L1(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L1 loss function defined above
    """    
    loss = np.sum(abs(y-yhat),axis=0)
    
    return loss


def L2(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L2 loss function defined above
    """
    loss = np.sum((y-yhat)**2,axis=0)
    
    return loss


def sigmoid(x):
    """
    Compute the sigmoid of x

    Arguments:
    x -- A scalar or numpy array of any size

    Return:
    s -- sigmoid(x)
    """
    s=np.exp(-x)+1
    s = 1/s
    
    return s

def sigmoid_derivative(x):
    """
    Compute the gradient (also called the slope or derivative)
     of the sigmoid function with respect to its input x.
    
    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """
    s = sigmoid(x)
    ds = s*(1-s)
    
    return ds


