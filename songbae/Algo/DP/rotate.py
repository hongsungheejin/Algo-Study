import math 
import matplotlib.pyplot as plt
import math as m
import cv2
import copy
import numpy as np
import argparse
def rotate(img,angle,bilinear=1):
  '''
  Rotate a point counterclockwise by a given angle around a given origin 
  The angle should be given in radians

  input: 
    img: image
    angle: int
    bilinear: option

  output:
    rotated img
  '''
  assert len(img) > 0 and len(img[0]) > 0
  assert angle<=360
  test_img = np.zeros_like(img)
  h, w, c = img.shape
  angle=math.radians(angle)
  test_img = test_img.tolist()
  ox,oy = (h//2, w//2) # center
  for H in range(h):
    for W in range(w):
      px,py =H,W
      qx= ox+math.cos(angle)*(px-ox)-math.sin(angle)*(py-oy)
      qy=oy+math.sin(angle)*(px-ox)+math.cos(angle)*(py-oy)
      t=qx-math.floor(qx)
      v=qy-math.floor(qy)
      qx= math.floor(qx)
      qy= math.floor(qy)
      if qx<1 or qy <1 or qx>=h or qy>=w:continue
      if bilinear:
        test_img[px][py][:] = (t*v)*img[qx][qy][:]+(1-t)*v*img[qx-1][qy][:] + \
            t*(1-v)*img[qx][qy-1][:]+(1-t)*(1-v)*img[qx-1][qy-1][:]
      else:
        test_img[qx][qy][:]=img[px][py][:]
  return test_img

def scale(img,size):
  '''
  input:
    img: image
    size: scaling size

  output:
    scaled image
  
  '''
  assert len(img)>0 and len(img[0])>0
  h,w=len(img),len(img[0])
  scale_img = np.zeros_like(img).tolist()
  s_h,s_w =len(scale_img),len(scale_img[0])
  for H in range(s_h):
    for W in range(s_w):
      px=H/size
      py=W/size
      t=px-math.floor(px)
      v=py-math.floor(py)
      px=math.floor(px)
      py=math.floor(py)
      if px<=1 or py<=1 or px>=h or py>= w:continue 
      scale_img[H][W][:]=t*v*img[px][py][:]+(1-t)*v*img[px-1][py][:]+t*(1-v)*img[px][py-1][:]+(1-t)*(1-v)*img[px-1][py-1][:]
  return scale_img

def shift(img,x,y):
  """
  input :
    img: image
    x: shift by x
    y: shift by y

  output:
    shifted_img
  """
  new_image=np.zeros_like(img).tolist()
  h,w= len(new_image), len(new_image[0])
  for i in range(h):
    for j in range(w):
      px=i-x
      py=j-y
      if px<=0 or py<=0 or px>=h or py>=h :continue
      new_image[px][py][:]=img[i][j][:]
  return new_image
  


if __name__=='__main__':
  parser=argparse.ArgumentParser(description='Only python shift,scale,rotate implement')
  parser.add_argument('--rotate', default=90, type=int, help='default 90 rotation if 0 no rotate function')
  parser.add_argument('--scale', default=1, type=float,
                      help='default 1 scaling if 1 no scaling function')
  parser.add_argument('--shift', default=90, type=int,
                      help='default0 if 0 no shift function')
  args=parser.parse_args()

  img=cv2.imread('../../ong.jpg')
  img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
  if args.shift!=0:
    shift_img=shift(img,args.shift,args.shift)
  if args.rotate!=0:
    rotate_img=rotate(img,args.rotate)
  if args.scale!=1:
    scale_img=scale(img,args.scale)
  
  '''
  visualization
  '''
  img=np.array(img,dtype=np.uint8)
  shift_img=np.array(shift_img,dtype=np.uint8)
  rotate_img = np.array(rotate_img, dtype=np.uint8)
  scale_img = np.array(scale_img, dtype=np.uint8)
  fig,axes=plt.subplots(2,2,dpi=100)
  image_list=[img,shift_img,rotate_img,scale_img]
  image_name=['Base','Shift','Rotate','Scale']
  for i in range(4):
    axes[i//2][i%2].axis('off')
    axes[i//2][i%2].set_title(f'{image_name[i]}')
    axes[i//2][i%2].imshow(image_list[i])
  plt.show()
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()

