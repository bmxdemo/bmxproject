Chris Sheehy and I have begun the process of using reflective tape and low exposure photographs to improve the photogrammetry procedure.  First of all, PhotoScan has a coordinate system that is not ideal -- it defines the direction that the camera is pointing (in one of any of the arbitrary photographs) to be -z.  The 3D model ends up sitting in a troubling position and when the XYZ points are exported from PhotoScan, it is difficult to analyze.  To account for this, we have written a simple python script that rotates the dish by applying rotation matrices to each exported point in the .txt file.

The code is here:
https://github.com/bmxdemo/bmxproject/blob/master/ipynb/parab3d.py

The code reads in the .txt file of XYZ points.  For now, all we have is the points from the original process in which we did not use reflective tape.  We realized that Rhino is not necessary after all, and thus here is the file of points exported directly from PhotoScan, located on my Google Drive since the file is too large for GitHub:

https://drive.google.com/drive/folders/0BxSWxTxFUD23ZXRFTHRST3lRM0U?usp=sharing

Here is the output of the code.  It plots the unrotated figure in blue and the rotated figure in red.  Since I had previously rotated this set of points by hand in PhotoScan (which is a pain, and hence the reason for the code) we set the rotation angles to zero, and the red and blue figures are overlaid.  The point is that every time we take a new set of photos it is anyone's guess as to how the coordinate system will orient itself.  So, while the figure does not need to be rotated for the old photos, it will need to be rotated for the new reflective tape photos.  

![petalv1](https://cloud.githubusercontent.com/assets/17692591/18458188/205ad724-792d-11e6-9ac2-67e5fd745d89.png)

Now for the reflective tape.  The first step was to figure out which tape would work best.  First, we tried 5997T81 floor tape.  Here is a photo of what this looks like on the petal at low exposure:

![img_2513](https://cloud.githubusercontent.com/assets/17692591/18458217/5db9feba-792d-11e6-8d42-878e84b9e821.JPG)

This was not really reflective enough, so today we tried 15835T58 vehicle tape.  You can see the improvement in this photo: 

![img_2528](https://cloud.githubusercontent.com/assets/17692591/18458227/67e76760-792d-11e6-8c94-6bce98650d5d.JPG)

Now, this tape will be cut up and placed all over the petal, but today I quickly took some photos with the strip sitting in the center of the dish to see what PhotoScan could do with it.  Here is the model it produced:

![vehicle_tape_model](https://cloud.githubusercontent.com/assets/17692591/18458371/99f929b8-792e-11e6-99b8-a01ae85cf7b1.png)

This is, indeed, extremely crude; however, I merely wanted to see if PhotoScan could handle low exposure images, and it seems like it can.  Therefore, the next steps are to cover the petal in the reflective vehicle tape and make a model in PhotoScan to export and analyze.