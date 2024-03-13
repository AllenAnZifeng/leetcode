#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 3P04
@contact: anz8@mcmaster.ca
@file: asg3.py
@time: 2020/4/9 23:54
'''

time = '''0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
0.18
0.2
0.22
0.24
0.26
0.28
0.3
0.32
0.34
0.36
0.38
0.4
0.42
0.44
0.46
0.48
0.5
0.52
0.54
0.56
0.58
0.6
0.62
0.64
0.66
0.68
0.7
0.72
0.74
0.76
0.78
0.8
0.82
0.84
0.86
0.88
0.9
0.92
0.94
0.96
0.98
'''

plate1 = '''0
388
415
525
635
708
693
627
534
429
361
339
334
332
337
354
378
405
427
449
471
476
456
403
288
107
31
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
'''

plate2='''0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
332
376
493
659
744
737
661
544
425
354
339
339
344
354
373
400
432
461
486
498
488
451
388
290
127
44
0
'''

time = [float(t) for t in time.split()]
plate1 = [float(f) for f in plate1.split()]
plate2 = [float(f) for f in plate2.split()]
#Q1.4

maxLeftForce,maxRightForce =0,0

for i in range(len(time)):
    maxRightForce=max(maxRightForce,plate1[i])
    maxLeftForce=max(maxLeftForce,plate2[i])

maxForce = max(maxLeftForce,maxRightForce)
print('max left force',maxLeftForce)
print('max right  force',maxRightForce)
print('force difference',maxForce)


#Q1.5
mass =62
weight = mass* 9.81

print('left percentage',maxLeftForce/mass,'N/kg')
print('right percentage',round(maxRightForce/mass,1),'N/kg')
print('the maximum vertical '
      'ground reaction force in '
      'number of body weights',round(maxForce/weight,1))

medial_lateral='''0.267
0.277
0.282
0.287
0.284
0.284
0.276
0.28
0.28
0.276
0.278
0.277
0.277
0.283
0.286
0.29
0.293
0.298
0.301
0.305
0.306
0.309
0.31
0.316
0.317
0.32
0.32
0.322
0.321
0.323
0.327
0.326
0.326
0.327
0.325
0.324
0.32
0.317
0.312
0.309
0.306
0.301
0.299
0.296
0.292
0.29
0.286
0.284
0.282
0.279
'''

vertical ='''0.883
0.88
0.878
0.876
0.875
0.875
0.878
0.881
0.888
0.895
0.902
0.907
0.913
0.915
0.916
0.915
0.911
0.908
0.903
0.899
0.893
0.886
0.88
0.874
0.868
0.865
0.863
0.862
0.867
0.872
0.877
0.887
0.894
0.899
0.9
0.904
0.904
0.904
0.901
0.899
0.894
0.888
0.886
0.881
0.874
0.87
0.866
0.86
0.859
0.859
'''

forward='''-0.184
-0.145
-0.108
-0.07
-0.035
0
0.032
0.066
0.098
0.131
0.162
0.194
0.226
0.258
0.29
0.321
0.352
0.383
0.417
0.452
0.486
0.521
0.56
0.598
0.636
0.674
0.71
0.746
0.779
0.812
0.847
0.877
0.91
0.941
0.973
1.004
1.035
1.066
1.098
1.129
1.161
1.197
1.23
1.269
1.308
1.349
1.389
1.428
1.465
1.5
'''
# Q2.4
medial_lateral = [float(d) for d in medial_lateral.split()]
vertical = [float(d) for d in vertical.split()]
forward = [float(d) for d in forward.split()]

# print('medial lateral',medial_lateral)
# print('vertical',vertical)
# print('forward',forward)

print('medial_lateral maximum displacement',max(medial_lateral)-min(medial_lateral))
print('vertical maximum displacement',max(vertical)-min(vertical))

# Q2.5
instantaneous_before = []
for i in range(len(forward)-1):
    instantaneous_before.append(round((forward[i+1]-forward[i])/0.02,2))
# print('instantaneous velocity before',instantaneous_before)

instantaneous_after = []
for i in range(len(forward)-2):
    instantaneous_after.append(round((forward[i+2]-forward[i])/0.04,2))
for j in instantaneous_after:
    print(j)

