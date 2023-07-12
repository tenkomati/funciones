import math

def softmax(*args):
  #returns the soft arg max vector for a given input. The name "softmax" is misleading;
  #is rather a smooth approximation to the arg max function: the function whose value is which index has the maximum.

  inputs=list(args) # a list of the args
  exp_inputs = [math.exp(i) for i in inputs] #a vector of the inputs as an exponent of exp() function
  outputs=[i / sum(exp_inputs) for i in exp_inputs] #the output of softmax

  return outputs


def argmax(*args):
  #ARG MAX FUNCTION:
  # returns a one hot vector which represent the max arg of the input
  # if there are more than one max value, the function will divide each one by the number of max values.

  inputs=list(args) # a list of the args
  exp_inputs = [math.exp(i) for i in inputs] #a vector of the inputs as an exponent of exp() function
  outputs=[i / sum(exp_inputs) for i in exp_inputs] #the output of softmax
  max_num= max(outputs) 
  n_max = sum(1 for i in outputs if i == max_num)
  hot_outputs = [1/n_max if i == max_num else 0 for i in outputs] #the one hot vector of the max of the output
  
  return hot_outputs
