import pyroot_logon
import HWWconfig

#list of tuples that have the optimized inputs for each mass point
#tuple is (mass, mvaVariableName, mvaCut, min4bodymass, max4bodymass, nbins,
#          alpha, alphaDown, alphaUp)

############################ SET Best #############################
optimalPars2 = [
    ( 170, "mva2j170mu", 0.300, 170.0, 250.0, 8, 0.110, 0.090, 0.140, (55.0,65.0), (95.0,115.0) ),
    ( 180, "mva2j180mu", 0.600, 170.0, 250.0, 8, 0.120, 0.080, 0.160, (55.0,65.0), (95.0,115.0) ),
    #( 190, "mva2j190mu", 0.700, 180.0, 250.0, 7, 0.020, 0.000, 0.170, (55.0,65.0), (95.0,115.0) ),
    #( 190, "mva2j190mu", 0.700, 170.0, 250.0, 8, 0.110, 0.020, 0.190, (55.0,65.0), (95.0,115.0) ),
    ( 190, "mva2j190mu", 0.600, 170.0, 250.0, 8, 0.060, 0.010, 0.120, (55.0,65.0), (95.0,115.0) ),
    ( 200, "mva2j200mu", 0.600, 180.0, 250.0, 7, 0.250, 0.190, 0.310, (55.0,65.0), (95.0,115.0) ),
    ( 250, "mva2j250mu", 0.700, 200.0, 500.0, 15, 0.150, 0.080, 0.210, (55.0,65.0), (95.0,200.0) ),
    ( 300, "mva2j300mu", 0.600, 240.0, 500.0, 13, 0.280, 0.170, 0.390, (55.0,65.0), (95.0,200.0) ),
    ( 350, "mva2j350mu", 0.600, 300.0, 780.0, 12, 0.280, 0.140, 0.410, (55.0,65.0), (95.0,200.0) ),
    ( 400, "mva2j400mu", 0.600, 300.0, 780.0, 12, 0.150, 0.000, 0.310, (55.0,65.0), (95.0,200.0) ),
    ( 450, "mva2j450mu", 0.600, 300.0, 780.0, 12, 0.400, 0.250, 0.550, (55.0,65.0), (95.0,200.0) ),
    ( 500, "mva2j500mu", 0.600, 300.0, 780.0, 12, 0.320, 0.130, 0.520, (55.0,65.0), (95.0,200.0) ),
    ( 550, "mva2j550mu", 0.600, 300.0, 780.0, 12, 0.110, 0.000, 0.240, (40.0,65.0), (95.0,200.0) ),
    ( 600, "mva2j600mu", 0.800, 300.0, 780.0, 12, 0.000, 0.000, 0.080, (40.0,65.0), (95.0,200.0) )

]
optimalPars3 = [
    ( 170, "mva3j170mu", 0.300, 170.0, 250.0, 8, 0.220, 0.160, 0.280, (55.0,65.0), (95.0,115.0) ),
    ( 180, "mva3j180mu", 0.300, 170.0, 250.0, 8, 0.230, 0.170, 0.290, (55.0,65.0), (95.0,115.0) ),
    #( 190, "mva3j190mu", 0.300, 180.0, 250.0, 7, 0.320, 0.240, 0.410, (55.0,65.0), (95.0,115.0) ),
    ( 190, "mva3j190mu", 0.300, 170.0, 250.0, 8, 0.260, 0.200, 0.320, (55.0,65.0), (95.0,115.0) ),
    ( 200, "mva3j200mu", 0.300, 180.0, 250.0, 7, 0.280, 0.190, 0.380, (55.0,65.0), (95.0,115.0) ),
    ( 250, "mva3j250mu", 0.400, 200.0, 500.0, 15, 0.410, 0.310, 0.520, (55.0,65.0), (95.0,200.0) ),
    ( 300, "mva3j300mu", 0.500, 240.0, 500.0, 13, 0.290, 0.170, 0.430, (55.0,65.0), (95.0,200.0) ),
    ( 350, "mva3j350mu", 0.500, 300.0, 780.0, 12, 0.000, 0.000, 0.200, (55.0,65.0), (95.0,200.0) ),
    ( 400, "mva3j400mu", 0.500, 300.0, 780.0, 12, 0.000, 0.000, 0.340, (55.0,65.0), (95.0,200.0) ),
    ( 450, "mva3j450mu", 0.500, 300.0, 780.0, 12, 0.000, 0.000, 0.220, (55.0,65.0), (95.0,200.0) ),
    ( 500, "mva3j500mu", 0.500, 300.0, 780.0, 12, 0.080, 0.000, 0.400, (55.0,65.0), (95.0,200.0) ),
    ( 550, "mva3j550mu", 0.600, 300.0, 780.0, 12, 0.000, 0.000, 0.180, (40.0,65.0), (95.0,200.0) ),
    ( 600, "mva3j600mu", 0.800, 300.0, 780.0, 12, 0.720, 0.530, 0.920, (40.0,65.0), (95.0,200.0) )
    ]


############################ SET 1 #############################
#optimalPars2 = [
#    ( 170, "mva2j170mu", 0.300, 170.0, 250.0, 8, 0.110, 0.090, 0.130, (55.0,65.0), (95.0,115.0) ),
#    ( 180, "mva2j180mu", 0.300, 170.0, 250.0, 8, 0.150, 0.130, 0.170, (55.0,65.0), (95.0,115.0) ),
#    ( 190, "mva2j190mu", 0.300, 170.0, 250.0, 8, 0.150, 0.130, 0.170, (55.0,65.0), (95.0,115.0) ),
#    ( 200, "mva2j200mu", 0.300, 170.0, 250.0, 8, 0.190, 0.170, 0.210, (55.0,65.0), (95.0,115.0) ),
#    ( 250, "mva2j250mu", 0.300, 200.0, 500.0, 15, 0.340, 0.310, 0.380, (55.0,65.0), (95.0,115.0) ),
#    ( 300, "mva2j300mu", 0.300, 200.0, 500.0, 15, 0.380, 0.350, 0.410, (55.0,65.0), (95.0,115.0) ),
#    ( 350, "mva2j350mu", 0.300, 260.0, 780.0, 13, 0.450, 0.350, 0.550, (55.0,65.0), (95.0,115.0) ),
#    ( 400, "mva2j400mu", 0.300, 260.0, 780.0, 13, 0.470, 0.380, 0.560, (55.0,65.0), (95.0,115.0) ),
#    ( 450, "mva2j450mu", 0.300, 260.0, 780.0, 13, 0.420, 0.330, 0.510, (55.0,65.0), (95.0,115.0) ),
#    ( 500, "mva2j500mu", 0.300, 260.0, 780.0, 13, 0.560, 0.460, 0.650, (55.0,65.0), (95.0,115.0) ),
#    ( 550, "mva2j550mu", 0.300, 260.0, 780.0, 13, 0.490, 0.400, 0.580, (55.0,65.0), (95.0,115.0) ),
#    ( 600, "mva2j600mu", 0.300, 260.0, 780.0, 13, 0.550, 0.450, 0.640, (55.0,65.0), (95.0,115.0) )
#]
#
############################# SET 2 #############################
#optimalPars2 = [
#    ( 170, "mva2j170mu", 0.400, 170.0, 250.0, 8, 0.110, 0.090, 0.140, (55.0,65.0), (95.0,115.0) ),
#    ( 180, "mva2j180mu", 0.400, 170.0, 250.0, 8, 0.140, 0.110, 0.160, (55.0,65.0), (95.0,115.0) ),
#    ( 190, "mva2j190mu", 0.400, 170.0, 250.0, 8, 0.140, 0.110, 0.170, (55.0,65.0), (95.0,115.0) ),
#    ( 200, "mva2j200mu", 0.400, 170.0, 250.0, 8, 0.180, 0.150, 0.200, (55.0,65.0), (95.0,115.0) ),
#    ( 250, "mva2j250mu", 0.400, 200.0, 500.0, 15, 0.300, 0.260, 0.340, (55.0,65.0), (95.0,115.0) ),
#    ( 300, "mva2j300mu", 0.400, 200.0, 500.0, 15, 0.400, 0.370, 0.440, (55.0,65.0), (95.0,115.0) ),
#    ( 350, "mva2j350mu", 0.400, 260.0, 780.0, 13, 0.460, 0.350, 0.550, (55.0,65.0), (95.0,115.0) ),
#    ( 400, "mva2j400mu", 0.400, 260.0, 780.0, 13, 0.520, 0.410, 0.620, (55.0,65.0), (95.0,115.0) ),
#    ( 450, "mva2j450mu", 0.400, 260.0, 780.0, 13, 0.450, 0.340, 0.550, (55.0,65.0), (95.0,115.0) ),
#    ( 500, "mva2j500mu", 0.400, 260.0, 780.0, 13, 0.520, 0.430, 0.610, (55.0,65.0), (95.0,115.0) ),
#    ( 550, "mva2j550mu", 0.400, 260.0, 780.0, 13, 0.570, 0.450, 0.680, (55.0,65.0), (95.0,115.0) ),
#    ( 600, "mva2j600mu", 0.400, 260.0, 780.0, 13, 0.610, 0.510, 0.720, (55.0,65.0), (95.0,115.0) )
#]
#
############################# SET 3 #############################
#optimalPars2 = [
#    ( 170, "mva2j170mu", 0.500, 170.0, 250.0, 8, 0.110, 0.080, 0.140, (55.0,65.0), (95.0,115.0) ),
#    ( 180, "mva2j180mu", 0.500, 170.0, 250.0, 8, 0.120, 0.090, 0.150, (55.0,65.0), (95.0,115.0) ),
#    ( 190, "mva2j190mu", 0.500, 170.0, 250.0, 8, 0.110, 0.080, 0.150, (55.0,65.0), (95.0,115.0) ),
#    ( 200, "mva2j200mu", 0.500, 170.0, 250.0, 8, 0.200, 0.170, 0.230, (55.0,65.0), (95.0,115.0) ),
#    ( 250, "mva2j250mu", 0.500, 200.0, 500.0, 15, 0.300, 0.260, 0.350, (55.0,65.0), (95.0,115.0) ),
#    ( 300, "mva2j300mu", 0.500, 200.0, 500.0, 15, 0.380, 0.340, 0.420, (55.0,65.0), (95.0,115.0) ),
#    ( 350, "mva2j350mu", 0.500, 260.0, 780.0, 13, 0.420, 0.320, 0.520, (55.0,65.0), (95.0,115.0) ),
#    ( 400, "mva2j400mu", 0.500, 260.0, 780.0, 13, 0.420, 0.320, 0.520, (55.0,65.0), (95.0,115.0) ),
#    ( 450, "mva2j450mu", 0.500, 260.0, 780.0, 13, 0.510, 0.400, 0.630, (55.0,65.0), (95.0,115.0) ),
#    ( 500, "mva2j500mu", 0.500, 260.0, 780.0, 13, 0.470, 0.360, 0.580, (55.0,65.0), (95.0,115.0) ),
#    ( 550, "mva2j550mu", 0.500, 260.0, 780.0, 13, 0.470, 0.340, 0.590, (55.0,65.0), (95.0,115.0) ),
#    ( 600, "mva2j600mu", 0.500, 260.0, 780.0, 13, 0.420, 0.320, 0.520, (55.0,65.0), (95.0,115.0) )
#]
#
#
############################# SET 4 #############################
#optimalPars2 = [
#    ( 170, "mva2j170mu", 0.600, 170.0, 250.0, 8, 0.150, 0.100, 0.190, (55.0,65.0), (95.0,115.0) ),
#    ( 180, "mva2j180mu", 0.600, 170.0, 250.0, 8, 0.120, 0.080, 0.160, (55.0,65.0), (95.0,115.0) ),
#    ( 190, "mva2j190mu", 0.600, 170.0, 250.0, 8, 0.060, 0.010, 0.110, (55.0,65.0), (95.0,115.0) ),
#    ( 200, "mva2j200mu", 0.600, 170.0, 250.0, 8, 0.190, 0.150, 0.220, (55.0,65.0), (95.0,115.0) ),
#    ( 250, "mva2j250mu", 0.600, 200.0, 500.0, 15, 0.260, 0.200, 0.320, (55.0,65.0), (95.0,115.0) ),
#    ( 300, "mva2j300mu", 0.600, 200.0, 500.0, 15, 0.390, 0.350, 0.430, (55.0,65.0), (95.0,115.0) ),
#    ( 350, "mva2j350mu", 0.600, 260.0, 780.0, 13, 0.380, 0.270, 0.480, (55.0,65.0), (95.0,115.0) ),
#    ( 400, "mva2j400mu", 0.600, 260.0, 780.0, 13, 0.370, 0.240, 0.480, (55.0,65.0), (95.0,115.0) ),
#    ( 450, "mva2j450mu", 0.600, 260.0, 780.0, 13, 0.510, 0.400, 0.610, (55.0,65.0), (95.0,115.0) ),
#    ( 500, "mva2j500mu", 0.600, 260.0, 780.0, 13, 0.450, 0.340, 0.550, (55.0,65.0), (95.0,115.0) ),
#    ( 550, "mva2j550mu", 0.600, 260.0, 780.0, 13, 0.240, 0.070, 0.390, (55.0,65.0), (95.0,115.0) ),
#    ( 600, "mva2j600mu", 0.600, 260.0, 780.0, 13, 0.220, 0.100, 0.330, (55.0,65.0), (95.0,115.0) )
#]
#
#
############################# SET 5 #############################
#optimalPars2 = [
#    ( 170, "mva2j170mu", 0.700, 170.0, 250.0, 8, 0.220, 0.150, 0.290, (55.0,65.0), (95.0,115.0) ),
#    ( 180, "mva2j180mu", 0.700, 170.0, 250.0, 8, 0.160, 0.110, 0.210, (55.0,65.0), (95.0,115.0) ),
#    ( 190, "mva2j190mu", 0.700, 170.0, 250.0, 8, 0.110, 0.030, 0.180, (55.0,65.0), (95.0,115.0) ),
#    ( 200, "mva2j200mu", 0.700, 170.0, 250.0, 8, 0.180, 0.130, 0.230, (55.0,65.0), (95.0,115.0) ),
#    ( 250, "mva2j250mu", 0.700, 200.0, 500.0, 15, 0.190, 0.110, 0.260, (55.0,65.0), (95.0,115.0) ),
#    ( 300, "mva2j300mu", 0.700, 200.0, 500.0, 15, 0.360, 0.300, 0.410, (55.0,65.0), (95.0,115.0) ),
#    ( 350, "mva2j350mu", 0.700, 260.0, 780.0, 13, 0.160, 0.030, 0.260, (55.0,65.0), (95.0,115.0) ),
#    ( 400, "mva2j400mu", 0.700, 260.0, 780.0, 13, 0.270, 0.140, 0.380, (55.0,65.0), (95.0,115.0) ),
#    ( 450, "mva2j450mu", 0.700, 260.0, 780.0, 13, 0.300, 0.150, 0.440, (55.0,65.0), (95.0,115.0) ),
#    ( 500, "mva2j500mu", 0.700, 260.0, 780.0, 13, 0.390, 0.260, 0.510, (55.0,65.0), (95.0,115.0) ),
#    ( 550, "mva2j550mu", 0.700, 260.0, 780.0, 13, 0.210, 0.030, 0.360, (55.0,65.0), (95.0,115.0) ),
#    ( 600, "mva2j600mu", 0.700, 260.0, 780.0, 13, 0.190, 0.040, 0.310, (55.0,65.0), (95.0,115.0) )
#]
#
############################## SET 6 #############################
#optimalPars2 = [
#    ( 170, "mva2j170mu", 0.800, 170.0, 250.0, 8, 0.190, 0.080, 0.320, (55.0,65.0), (95.0,115.0) ),
#    ( 180, "mva2j180mu", 0.800, 170.0, 250.0, 8, 0.160, 0.030, 0.290, (55.0,65.0), (95.0,115.0) ),
#    ( 190, "mva2j190mu", 0.800, 170.0, 250.0, 8, 0.000, 0.000, 0.130, (55.0,65.0), (95.0,115.0) ),
#    ( 200, "mva2j200mu", 0.800, 170.0, 250.0, 8, 0.330, 0.250, 0.410, (55.0,65.0), (95.0,115.0) ),
#    ( 250, "mva2j250mu", 0.800, 200.0, 500.0, 15, 0.160, 0.040, 0.280, (55.0,65.0), (95.0,115.0) ),
#    ( 300, "mva2j300mu", 0.800, 200.0, 500.0, 15, 0.250, 0.160, 0.330, (55.0,65.0), (95.0,115.0) ),
#    ( 350, "mva2j350mu", 0.800, 260.0, 780.0, 13, 0.000, 0.000, 0.140, (55.0,65.0), (95.0,115.0) ),
#    ( 400, "mva2j400mu", 0.800, 260.0, 780.0, 13, 0.190, 0.020, 0.330, (55.0,65.0), (95.0,115.0) ),
#    ( 450, "mva2j450mu", 0.800, 260.0, 780.0, 13, 0.170, 0.000, 0.310, (55.0,65.0), (95.0,115.0) ),
#    ( 500, "mva2j500mu", 0.800, 260.0, 780.0, 13, 0.130, 0.000, 0.300, (55.0,65.0), (95.0,115.0) ),
#    ( 550, "mva2j550mu", 0.800, 260.0, 780.0, 13, 0.040, 0.000, 0.220, (55.0,65.0), (95.0,115.0) ),
#    ( 600, "mva2j600mu", 0.800, 260.0, 780.0, 13, 0.130, 0.000, 0.270, (55.0,65.0), (95.0,115.0) )
#]
#
#
#
############################# SET 1 #############################
#optimalPars3 = [
#    ( 170, "mva3j170mu", 0.300, 170.0, 250.0, 8, 0.220, 0.160, 0.280, (55.0,65.0), (95.0,115.0) ),
#    ( 180, "mva3j180mu", 0.300, 170.0, 250.0, 8, 0.230, 0.170, 0.290, (55.0,65.0), (95.0,115.0) ),
#    ( 190, "mva3j190mu", 0.300, 170.0, 250.0, 8, 0.260, 0.200, 0.320, (55.0,65.0), (95.0,115.0) ),
#    ( 200, "mva3j200mu", 0.300, 170.0, 250.0, 8, 0.270, 0.210, 0.330, (55.0,65.0), (95.0,115.0) ),
#    ( 250, "mva3j250mu", 0.300, 200.0, 500.0, 15, 0.090, 0.000, 0.230, (55.0,65.0), (95.0,115.0) ),
#    ( 300, "mva3j300mu", 0.300, 200.0, 500.0, 15, 0.110, 0.000, 0.250, (55.0,65.0), (95.0,115.0) ),
#    ( 350, "mva3j350mu", 0.300, 260.0, 780.0, 13, 0.000, 0.000, 0.150, (55.0,65.0), (95.0,115.0) ),
#    ( 400, "mva3j400mu", 0.300, 260.0, 780.0, 13, 0.000, 0.000, 0.120, (55.0,65.0), (95.0,115.0) ),
#    ( 450, "mva3j450mu", 0.300, 260.0, 780.0, 13, 0.000, 0.000, 0.210, (55.0,65.0), (95.0,115.0) ),
#    ( 500, "mva3j500mu", 0.300, 260.0, 780.0, 13, 0.000, 0.000, 0.280, (55.0,65.0), (95.0,115.0) ),
#    ( 550, "mva3j550mu", 0.300, 260.0, 780.0, 13, 0.020, 0.000, 0.240, (55.0,65.0), (95.0,115.0) ),
#    ( 600, "mva3j600mu", 0.300, 260.0, 780.0, 13, 0.010, 0.000, 0.240, (55.0,65.0), (95.0,115.0) )
#    ]
#
## ############################ SET 2 #############################
## optimalPars3 = [
##     ( 170, "mva3j170mu", 0.400, 170.0, 250.0, 8, 0.200, 0.140, 0.260, (55.0,65.0), (95.0,115.0) ),
##     ( 180, "mva3j180mu", 0.400, 170.0, 250.0, 8, 0.240, 0.180, 0.300, (55.0,65.0), (95.0,115.0) ),
##     ( 190, "mva3j190mu", 0.400, 170.0, 250.0, 8, 0.310, 0.250, 0.380, (55.0,65.0), (95.0,115.0) ),
##     ( 200, "mva3j200mu", 0.400, 170.0, 250.0, 8, 0.310, 0.240, 0.390, (55.0,65.0), (95.0,115.0) ),
##     ( 250, "mva3j250mu", 0.400, 200.0, 500.0, 15, 0.000, 0.000, 0.140, (55.0,65.0), (95.0,115.0) ),
##     ( 300, "mva3j300mu", 0.400, 200.0, 500.0, 15, 0.120, 0.000, 0.250, (55.0,65.0), (95.0,115.0) ),
##     ( 350, "mva3j350mu", 0.400, 260.0, 780.0, 13, 0.000, 0.000, 0.200, (55.0,65.0), (95.0,115.0) ),
##     ( 400, "mva3j400mu", 0.400, 260.0, 780.0, 13, 0.000, 0.000, 0.150, (55.0,65.0), (95.0,115.0) ),
##     ( 450, "mva3j450mu", 0.400, 260.0, 780.0, 13, 0.000, 0.000, 0.220, (55.0,65.0), (95.0,115.0) ),
##     ( 500, "mva3j500mu", 0.400, 260.0, 780.0, 13, 0.060, 0.000, 0.350, (55.0,65.0), (95.0,115.0) ),
##     ( 550, "mva3j550mu", 0.400, 260.0, 780.0, 13, 0.130, 0.000, 0.320, (55.0,65.0), (95.0,115.0) ),
##     ( 600, "mva3j600mu", 0.400, 260.0, 780.0, 13, 0.080, 0.000, 0.270, (55.0,65.0), (95.0,115.0) )
##     ]

############################# SET 3 #############################
#optimalPars3 = [
#    ( 170, "mva3j170mu", 0.500, 170.0, 250.0, 8, 0.210, 0.140, 0.290, (55.0,65.0), (95.0,115.0) ),
#    ( 180, "mva3j180mu", 0.500, 170.0, 250.0, 8, 0.280, 0.210, 0.360, (55.0,65.0), (95.0,115.0) ),
#    ( 190, "mva3j190mu", 0.500, 170.0, 250.0, 8, 0.330, 0.250, 0.420, (55.0,65.0), (95.0,115.0) ),
#    ( 200, "mva3j200mu", 0.500, 170.0, 250.0, 8, 0.300, 0.230, 0.380, (55.0,65.0), (95.0,115.0) ),
#    ( 250, "mva3j250mu", 0.500, 200.0, 500.0, 15, 0.230, 0.070, 0.390, (55.0,65.0), (95.0,115.0) ),
#    ( 300, "mva3j300mu", 0.500, 200.0, 500.0, 15, 0.230, 0.100, 0.350, (55.0,65.0), (95.0,115.0) ),
#    ( 350, "mva3j350mu", 0.500, 260.0, 780.0, 13, 0.000, 0.000, 0.240, (55.0,65.0), (95.0,115.0) ),
#    ( 400, "mva3j400mu", 0.500, 260.0, 780.0, 13, 0.000, 0.000, 0.190, (55.0,65.0), (95.0,115.0) ),
#    ( 450, "mva3j450mu", 0.500, 260.0, 780.0, 13, 0.030, 0.000, 0.300, (55.0,65.0), (95.0,115.0) ),
#    ( 500, "mva3j500mu", 0.500, 260.0, 780.0, 13, 0.000, 0.000, 0.160, (55.0,65.0), (95.0,115.0) ),
#    ( 550, "mva3j550mu", 0.500, 260.0, 780.0, 13, 0.120, 0.000, 0.310, (55.0,65.0), (95.0,115.0) ),
#    ( 600, "mva3j600mu", 0.500, 260.0, 780.0, 13, 0.240, 0.100, 0.390, (55.0,65.0), (95.0,115.0) )
#    ]
#
############################# SET 4 #############################
#optimalPars3 = [
#    ( 170, "mva3j170mu", 0.600, 170.0, 250.0, 8, 0.070, 0.000, 0.150, (55.0,65.0), (95.0,115.0) ),
#    ( 180, "mva3j180mu", 0.600, 170.0, 250.0, 8, 0.450, 0.280, 0.670, (55.0,65.0), (95.0,115.0) ),
#    ( 190, "mva3j190mu", 0.600, 170.0, 250.0, 8, 0.510, 0.340, 0.700, (55.0,65.0), (95.0,115.0) ),
#    ( 200, "mva3j200mu", 0.600, 170.0, 250.0, 8, 0.430, 0.320, 0.550, (55.0,65.0), (95.0,115.0) ),
#    ( 250, "mva3j250mu", 0.600, 200.0, 500.0, 15, 0.340, 0.200, 0.490, (55.0,65.0), (95.0,115.0) ),
#    ( 300, "mva3j300mu", 0.600, 200.0, 500.0, 15, 0.160, 0.010, 0.300, (55.0,65.0), (95.0,115.0) ),
#    ( 350, "mva3j350mu", 0.600, 260.0, 780.0, 13, 0.000, 0.000, 0.460, (55.0,65.0), (95.0,115.0) ),
#    ( 400, "mva3j400mu", 0.600, 260.0, 780.0, 13, 0.000, 0.000, 0.230, (55.0,65.0), (95.0,115.0) ),
#    ( 450, "mva3j450mu", 0.600, 260.0, 780.0, 13, 0.140, 0.000, 0.400, (55.0,65.0), (95.0,115.0) ),
#    ( 500, "mva3j500mu", 0.600, 260.0, 780.0, 13, 0.000, 0.000, 0.140, (55.0,65.0), (95.0,115.0) ),
#    ( 550, "mva3j550mu", 0.600, 260.0, 780.0, 13, 0.090, 0.000, 0.280, (55.0,65.0), (95.0,115.0) ),
#    ( 600, "mva3j600mu", 0.600, 260.0, 780.0, 13, 0.300, 0.140, 0.470, (55.0,65.0), (95.0,115.0) )
#    ]
#

## ############################ SET 5 #############################
## optimalPars3 = [
##     ( 170, "mva3j170mu", 0.700, 170.0, 250.0, 8, 0.040, 0.000, 0.140, (55.0,65.0), (95.0,115.0) ),
##     ( 180, "mva3j180mu", 0.700, 170.0, 250.0, 8, 0.580, 0.330, 1.000, (55.0,65.0), (95.0,115.0) ),
##     ( 190, "mva3j190mu", 0.700, 170.0, 250.0, 8, 0.710, 0.510, 0.930, (55.0,65.0), (95.0,115.0) ),
##     ( 200, "mva3j200mu", 0.700, 170.0, 250.0, 8, 0.590, 0.430, 0.770, (55.0,65.0), (95.0,115.0) ),
##     ( 250, "mva3j250mu", 0.700, 200.0, 500.0, 15, 0.300, 0.160, 0.460, (55.0,65.0), (95.0,115.0) ),
##     ( 300, "mva3j300mu", 0.700, 200.0, 500.0, 15, 0.220, 0.020, 0.430, (55.0,65.0), (95.0,115.0) ),
##     ( 350, "mva3j350mu", 0.700, 260.0, 780.0, 13, 0.000, 0.000, 0.330, (55.0,65.0), (95.0,115.0) ),
##     ( 400, "mva3j400mu", 0.700, 260.0, 780.0, 13, 0.000, 0.000, 0.080, (55.0,65.0), (95.0,115.0) ),
##     ( 450, "mva3j450mu", 0.700, 260.0, 780.0, 13, 0.000, 0.000, 0.260, (55.0,65.0), (95.0,115.0) ),
##     ( 500, "mva3j500mu", 0.700, 260.0, 780.0, 13, 0.120, 0.000, 0.710, (55.0,65.0), (95.0,115.0) ),
##     ( 550, "mva3j550mu", 0.700, 260.0, 780.0, 13, 0.000, 0.000, 0.140, (55.0,65.0), (95.0,115.0) ),
##     ( 600, "mva3j600mu", 0.700, 260.0, 780.0, 13, 0.120, 0.000, 0.300, (55.0,65.0), (95.0,115.0) )
##     ]

## ############################ SET 6 #############################
## optimalPars3 = [
##     ( 170, "mva3j170mu", 0.800, 170.0, 250.0, 8, 0.000, 0.000, 0.000, (55.0,65.0), (95.0,115.0) ),
##     ( 180, "mva3j180mu", 0.800, 170.0, 250.0, 8, 0.250, 0.050, 0.480, (55.0,65.0), (95.0,115.0) ),
##     ( 190, "mva3j190mu", 0.800, 170.0, 250.0, 8, 0.780, 0.580, 0.950, (55.0,65.0), (95.0,115.0) ),
##     ( 200, "mva3j200mu", 0.800, 170.0, 250.0, 8, 0.000, 0.000, 0.120, (55.0,65.0), (95.0,115.0) ),
##     ( 250, "mva3j250mu", 0.800, 200.0, 500.0, 15, 0.880, 0.460, 0.970, (55.0,65.0), (95.0,115.0) ),
##     ( 300, "mva3j300mu", 0.800, 200.0, 500.0, 15, 0.690, 0.510, 0.850, (55.0,65.0), (95.0,115.0) ),
##     ( 350, "mva3j350mu", 0.800, 260.0, 780.0, 13, 0.860, 0.480, 1.000, (55.0,65.0), (95.0,115.0) ),
##     ( 400, "mva3j400mu", 0.800, 260.0, 780.0, 13, 0.050, 0.000, 0.340, (55.0,65.0), (95.0,115.0) ),
##     ( 450, "mva3j450mu", 0.800, 260.0, 780.0, 13, 0.010, 0.000, 0.350, (55.0,65.0), (95.0,115.0) ),
##     ( 500, "mva3j500mu", 0.800, 260.0, 780.0, 13, 1.000, 0.500, 1.000, (55.0,65.0), (95.0,115.0) ),
##     ( 550, "mva3j550mu", 0.800, 260.0, 780.0, 13, 0.500, 0.180, 0.890, (55.0,65.0), (95.0,115.0) ),
##     ( 600, "mva3j600mu", 0.800, 260.0, 780.0, 13, 0.080, 0.000, 0.400, (55.0,65.0), (95.0,115.0) )
##     ]


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
#optimalPars2 = [
#    ( 170, "mva2j170mu", 0.520, 170.0, 250.0, 8, 0.120, 0.080, 0.150, (55.0,65.0), (95.0,115.0) ),
#    ( 180, "mva2j180mu", 0.670, 170.0, 250.0, 8, 0.160, 0.110, 0.210, (55.0,65.0), (95.0,115.0) ),
#    ( 190, "mva2j190mu", 0.710, 170.0, 250.0, 8, 0.090, 0.000, 0.170, (55.0,65.0), (95.0,115.0) ),
#    ( 200, "mva2j200mu", 0.640, 170.0, 250.0, 8, 0.210, 0.170, 0.250, (55.0,65.0), (95.0,115.0) ),
#    ( 250, "mva2j250mu", 0.710, 200.0, 500.0, 15, 0.210, 0.140, 0.290, (55.0,65.0), (95.0,115.0) ),
#    ( 300, "mva2j300mu", 0.720, 200.0, 500.0, 15, 0.340, 0.280, 0.400, (55.0,65.0), (95.0,115.0) ),
#    ( 350, "mva2j350mu", 0.690, 260.0, 780.0, 13, 0.150, 0.020, 0.260, (55.0,65.0), (95.0,115.0) ),
#    ( 400, "mva2j400mu", 0.700, 260.0, 780.0, 13, 0.280, 0.130, 0.400, (50.0,65.0), (100.0,115.0) ),
#    ( 450, "mva2j450mu", 0.620, 260.0, 780.0, 13, 0.440, 0.310, 0.550, (55.0,65.0), (95.0,115.0) ),
#    ( 500, "mva2j500mu", 0.720, 260.0, 780.0, 13, 0.300, 0.150, 0.430, (55.0,65.0), (95.0,115.0) ),
#    ( 550, "mva2j550mu", 0.750, 260.0, 780.0, 13, 0.210, 0.000, 0.390, (50.0,65.0), (100.0,115.0) ),
#    ( 600, "mva2j600mu", 0.890, 260.0, 780.0, 13, 0.130, 0.000, 0.400, (55.0,65.0), (95.0,115.0) )
#    ]
#
#optimalPars3 = [
#    ( 170, "mva3j170mu", 0.440, 170.0, 250.0, 8, 0.210, 0.140, 0.280, (55.0,65.0), (95.0,115.0) ),
#    ( 180, "mva3j180mu", 0.400, 170.0, 250.0, 8, 0.240, 0.180, 0.300, (55.0,65.0), (95.0,115.0) ),
#    ( 190, "mva3j190mu", 0.390, 170.0, 250.0, 8, 0.330, 0.260, 0.400, (55.0,65.0), (95.0,115.0) ),
#    ( 200, "mva3j200mu", 0.510, 170.0, 250.0, 8, 0.350, 0.280, 0.430, (55.0,65.0), (95.0,115.0) ),
#    ( 250, "mva3j250mu", 0.590, 200.0, 500.0, 15, 0.270, 0.140, 0.410, (55.0,65.0), (95.0,115.0) ),
#    ( 300, "mva3j300mu", 0.470, 200.0, 500.0, 15, 0.150, 0.020, 0.270, (55.0,65.0), (95.0,115.0) ),
#    ( 350, "mva3j350mu", 0.550, 260.0, 780.0, 13, 0.000, 0.000, 0.230, (50.0,65.0), (100.0,115.0) ),
#    ( 400, "mva3j400mu", 0.570, 260.0, 780.0, 13, 0.000, 0.000, 0.290, (50.0,65.0), (100.0,115.0) ),
#    ( 450, "mva3j450mu", 0.520, 260.0, 780.0, 13, 0.000, 0.000, 0.250, (50.0,65.0), (100.0,115.0) ),
#    ( 500, "mva3j500mu", 0.480, 260.0, 780.0, 13, 0.000, 0.000, 0.150, (50.0,65.0), (100.0,115.0) ),
#    ( 550, "mva3j550mu", 0.440, 260.0, 780.0, 13, 0.210, 0.010, 0.450, (45.0,65.0), (95.0,105.0) ),
#    ( 600, "mva3j600mu", 0.720, 260.0, 780.0, 13, 0.090, 0.000, 0.350, (55.0,65.0), (95.0,115.0) )
#    ]
#####################################################################################################

def theConfig(Nj, mcdir = '', initFile = '', mH=400):

    if Nj == 3:
        optPars = HWWconfig.getOptimalPars(mH, optimalPars3)
    else:
        optPars = HWWconfig.getOptimalPars(mH, optimalPars2)
    
    mvaVarNames  = optPars[1]
    mvaCutValues = optPars[2]
    HWWconfig.minMlvjj = optPars[3]
    HWWconfig.maxMlvjj = optPars[4]

    fitterPars = HWWconfig.theConfig(Nj, mcdir, initFile)
    fitterPars.includeMuons = True
    fitterPars.includeElectrons = False
    
    fitterPars.cuts += '&& (%s > %f) ' % (mvaVarNames,mvaCutValues)

    print '2-body cuts:', fitterPars.cuts
    
    return fitterPars

def the4BodyConfig(twoBodyConfig, mH=400, syst=0):
    if twoBodyConfig.njets == 3:
        optPars = HWWconfig.getOptimalPars(mH, optimalPars3)
    else:
        optPars = HWWconfig.getOptimalPars(mH, optimalPars2)
    HWWconfig.minMlvjj = optPars[3]
    HWWconfig.maxMlvjj = optPars[4]
    alpha = optPars[6+syst]
    fitterPars = HWWconfig.the4BodyConfig(twoBodyConfig, alpha, optPars[9],
                                          optPars[10])
    fitterPars.nbins = optPars[5]
    return fitterPars
