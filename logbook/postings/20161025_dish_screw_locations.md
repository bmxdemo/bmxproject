## Oct 25, 2016: Directly measured screw locations w.r.t. photogrammetry

Figure 1 shows the 3D point cloud from [Evan's posting](https://github.com/bmxdemo/bmxproject/issues/9#issuecomment-252121391) imported into solidworks. We were able to measure the distance in the model between various pairs of screw heads and compare to measurements of the actual dish using our expensive, 2m long ruler. Results are in the next posting from Evan. 

It should be noted just how ragged the screws actually look, though. Figure 2 shows a zoom in. It is clear that it is not really localizing them very well.

### Figure 1 - photogrammetry points imported into Solidworks

![visual_v2_dense_cloud](https://cloud.githubusercontent.com/assets/6098508/19701382/2d685b7c-9ac9-11e6-9fa4-9a12ffc0b562.JPG)

### Figure 2 - screw heads

![screw_heads](https://cloud.githubusercontent.com/assets/6098508/19701666/5c5d1fb6-9aca-11e6-959c-3eb766e88c59.PNG)

### Update from Evan
Here are the differences (in cm) between the measurements that Chris and I took and the measurements in SolidWorks for a few pars of screw heads:
3.66215006e+00
7.97312430e+00
9.14568869e+00
1.29641657e+00
7.53437850e+00
6.12351624e+00
7.72541993e+00
1.18521837e+00
-7.10542736e-15
3.98208287e-01
-1.58555431e+00

When we import a model into SolidWorks it will not be the proper scale, so we must scale it to our measurements. You will notice that one of the differences is zero (or what Python calls zero). This is because we chose this distance to find the scaling factor in SolidWorks so that we could make measurements in cm.