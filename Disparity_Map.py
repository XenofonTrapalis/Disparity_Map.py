from PIL import Image
import numpy as np

img_R = np.array(Image.open('im6.png').convert('L'))
img_L = np.array(Image.open('im2.png').convert('L'))
img_R = np.asarray(img_R)
img_L = np.asarray(img_L)


Disp = np.zeros((375,450))
for i in range(7,367):
    print(i)
    Disparity = 80
    for j in range(7,442):
        best_ssd = 10000000000000
        if j < 362:
            Disparity = Disparity
        else:
            Disparity -= 1
        for d in range(1,Disparity):
            ssd = np.sum(abs(np.subtract(img_R[i-7 : i+8, j-7 : j+8],img_L[i-7 : i+8, j+d-7 : j+d+8]))**2)
            if (ssd < best_ssd):
                best_ssd = ssd
                best_d = d*3
        Disp [i,j] = best_d


Disp = np.asarray(Disp, dtype=np.uint8)
img2= Image.fromarray(Disp)
img2.save('Disparity_Map.png')
img2.show()
