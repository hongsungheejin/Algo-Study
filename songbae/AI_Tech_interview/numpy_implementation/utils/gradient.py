import numpy as np 

def _numercial_gradient_1d(f,x):
  h=1e-4
  grad=np.zeros_like(x)

  for idx in range(x.size):
    tmp_val=x[idx]
    x[idx]=float(tmp_val)+h
    fxh1=f(x)

    x[idx]=tmp_val-h
    fxh2=f(x)
    grad[idx]=(fxh1-fxh2)/(2*h)
    x[idx]=tmp_val
  return grad

def numerical_gradient_2d(f,x):
  if x.ndim==1:
    return _numercial_gradient_1d(f,x)
  else:
    grad=np.zeros_like(x)
    for idx,x  in enumerate(x):
      grad[idx]=_numercial_gradient_1d(f,x)
    return grad

def numerical_gradient(f,x):
  h=1e-4
  grad=np.zeros_like(x)
  it=np.nditer(x,flags=['multi_index'],op_flags=['readwrite'])
  while not it.finished:
    idx= it.multi_index
    tmp_val=x[idx]
    x[idx]=float(tmp_val)+h
    fxh1=f(x)
    x[idx]=tmp_val-h
    fxh2=f(x)
    grad[idx]=(fxh1-fxh2)/(2*h)
    x[idx]=tmp_val
    it.iternext()
  return grad