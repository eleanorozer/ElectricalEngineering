import math;

#info
print("Tool for band-pass amplifier circuits. Indicate desired cutoff frequencies, tolerance, and gain. Will find component values to (from lab kit) to match requirements. Tool created by Eleanor.")

# importing resistor and capacitor values available in lab kit
resistors = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2,    10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82,100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820,1e3, 1.2e3, 1.5e3, 1.8e3, 2.2e3, 2.7e3, 3.3e3, 3.9e3, 4.7e3, 5.6e3, 6.8e3, 8.2e3,10e3, 12e3, 15e3, 18e3, 22e3, 27e3, 33e3, 39e3, 47e3, 56e3, 68e3, 82e3,100e3, 120e3, 150e3, 180e3, 220e3, 270e3, 330e3, 390e3, 470e3, 560e3, 680e3, 820e3, 1e6];

capacitors = [4.70E-12,1.00E-11,4.70E-11,1.00E-10,2.20E-10, 3.30E-10,4.70E-10,1.00E-09,2.00E-09,4.70E-09,1.00E-08,2.00E-08,4.70E-08, 4.7E-6,1.00E-07];

# define constants
pi = math.pi

# define desired corner frequencies in Hz
desLowCutoff = 100;
desHighCutoff = 10000;

# define a tolerance and calculate low and high 
tol = .05;

# define range for high cutoff
desHighHighC = desHighCutoff + desHighCutoff * tol;
desLowHighC = desHighCutoff - desHighCutoff * tol;

# define range for low desHighCutoff
desHighLowC = desLowCutoff + desLowCutoff * tol;
desLowLowC = desLowCutoff - desLowCutoff * tol;


# define gain
gainK = 10;

lowGain = gainK - gainK*tol;
highGain = gainK + gainK*tol; 

# define -3dB
neg3dB = 1 / math.sqrt(2)

low3dB = neg3dB*(1 - tol);
high3dB = neg3dB*(1+tol);

#print desired low and high cutoff frequency
print("--------------------------")

for R1 in resistors:
  for C1 in capacitors:
    for R2 in resistors:
      for C2 in capacitors:

        K = (R1*C2)/(R2*C2+R1*C1)
        Q = (math.sqrt(R1*R2*C1*C2)/(R1*C2))
        w0 = 1/(math.sqrt(R1*R2*C1*C2))

        lowCutoff = 1/(2*pi*(R2*C2))
        highCutoff = 1/(2*pi*(R1*C1))
        #highCutoff = 1/math.sqrt(R1*R2*C1*C2)
        #lowCutoff = R1*R2*C1*C2;

        if (lowGain <= K <= highGain):
          if (desLowLowC <= lowCutoff <= desHighLowC):
            if (desLowHighC <= highCutoff <= desHighHighC):
              print("Found some components for you:")
              print("--------------------------")
              print("Low Cutoff:", lowCutoff)
              print("High Cutoff:", highCutoff)
              print("R1 = Zin =", R1)
              print("R2 =", R2)
              print("C1 =", C1)
              print("C2 =", C2)
              print("Gain =", K)
              print("--------------------------")