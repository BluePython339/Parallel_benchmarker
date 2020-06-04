# Made by the one and only Bluepython339
# python 3.8.3

from subprocess import *
import timeit
import os
import matplotlib.pyplot as plt
import argparse

error_check = False


parser = argparse.ArgumentParser(description='C and C++ executable benchmarker.')
parser.add_argument('-e','--executable', help="executable you want to benchmark", type=str, required=True)
parser.add_argument('-i','--Max_Input_Size', help="maximum input you want to benchmark (default: 10000000)", type=int, default=10000000)
parser.add_argument('-c','--competitor', help="competitor executable to compare benchmark", type=str)
parser.add_argument('-f','--fabians_feature', help="a flag which can be set to compensate for possible background processes slowing down the script",action='store_true')


def execute(datasize, executable):
	print("checking datasize {}".format(datasize))
	procces = check_output(['./{} {}'.format(executable, datasize)],shell=True)
	tmp = procces.decode('utf-8').split(' ')
	procces = float(tmp[0])+(float(tmp[1])/1000000000)
	return float(procces) #start the c script with passed data

def bench_it(maxInput, executable):
	output_num = [] #list of inputs we tried
	output_time = [] # list of times it look per input
	inputsize = 100000 # starting input size
	 #i mad it easy for you to configure
	while inputsize < maxInput: #
		print("now trying: {}".format(inputsize))
		#creating the timeing object
		#adding the new datasize to the list
		output_num.append(inputsize)
		#starting the timing sequence
		if error_check:
			outputs = [] #fabians feature
			for i in range(5):
				outputs.append(execute(inputsize, executable))
			output_time.append((sum(outputs)/5))
		else:
			output_time.append(execute(inputsize, executable))
		#calculating the new input size and rounding it to the nearest int
		inputsize = int(inputsize+(inputsize/4))

	return output_num, output_time #returning the test results

if __name__ == "__main__":
	args = parser.parse_args()

	if args.fabians_feature:
		error_check = True

	a = bench_it(args.Max_Input_Size, args.executable)
	plt.plot(a[0],a[1], label=args.executable)
	if args.competitor:
		b = bench_it(args.Max_Input_Size, args.competitor)
		plt.plot(b[0],b[1], label=args.competitor) #calculating the plot values
		plt.title("{} benchmark compared to {}".format(args.executable, args.competitor))
	else:
		plt.title("benchmark for {}".format(args.executable																													))
	plt.xlabel("inputsize")
	plt.ylabel("time in seconds")
	plt.legend()
	plt.show() #plotting the graph