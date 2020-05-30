# Parallel_benchmarker
A benchmarking tool for benchmarking and comparing C and C++ applications for execution time (made for Parallel computing RU)

## Requirements
```
python 3.#.#
pip3 install matplotlib argparse
```
## IMPORTANT
In order to get the program to work with an argument, the main function needs to be substituted with this :
`int main(int argc, char **argv)` and `n = N` be substituted by `n = atoi(argv[1])`.
After compiling the program, for example with `gcc relax.c -o relax`, the command `./relax 10000000`
will execute program with the default input.


## Usage:
```
  -h, --help            show this help message and exit
  -e EXECUTABLE, --executable EXECUTABLE
                        executable you want to benchmark
  -i MAX_INPUT_SIZE, --Max_Input_Size MAX_INPUT_SIZE
                        maximum input you want to benchmark (default: 10000000)
  -c COMPETITOR, --competitor COMPETITOR
                        competitor executable to compare benchmark
  -f, --fabians_feature
                        a flag which can be set to compensate for possible background processes slowing down the
                        script

```
## Examples:
```
python3 benchmark.py -e relax -c relax_optimised -i 150000 
```
Comparing the time performance of relax vs an optimised version using exponentially growing input until 150000.
```
python3 benchmark.py -e relax_openmp -i 150000
```
benchmarking a script based on an exponentially increasing input until 150000.

## Example output:
![Example output](example.png)

##Question:
feel free to ask in the RU twaars app

