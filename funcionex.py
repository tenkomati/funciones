import math

def softmax(*args):
  #returns the soft arg max vector for a given input. The name "softmax" is misleading;
  #is rather a smooth approximation to the arg max function: the function whose value is which index has the maximum.

  inputs=list(args) # a list of the args
  exp_inputs = [] #a vector of the inputs as an exponent of exp() function
  outputs=[] #the output of softmax

  for i in inputs:
    exp_inputs.append(math.exp(i))
  for i in exp_inputs:
    outputs.append(i / sum(exp_inputs))

  return outputs


def argmax(*args):
  #ARG MAX FUNCTION:
  # returns a one hot vector which represent the max arg of the input
  # if there are more than one max value, the function will divide each one by the number of max values.

  inputs=list(args) # a list of the args
  exp_inputs = [] #a vector of the inputs as an exponent of exp() function
  outputs=[] #the output of softmax
  hot_outputs = [] #the one hot vector of the max of the output

  for i in inputs:
    exp_inputs.append(math.exp(i))
  for i in exp_inputs:
    outputs.append(i / sum(exp_inputs))

  max_num= max(outputs) #the max value of the outputs

  n_max = int()

  for i in outputs:
    if i == max_num:
      n_max += 1

  

  for i in outputs:
    if i == max_num:
      hot_outputs.append(1/n_max)
    else:
      hot_outputs.append(0)

  return hot_outputs
