**this Repository is forked from https://github.com/manzilzaheer/CoverTree**

# Tree Based Nearest Neighbor Search with Guarantees

We present parallel implementations of two tree based nearest neighbor search data structures: SG-Tree and Cover Tree.

## Cover Tree
The cover tree data structure was originally presented in and improved in:

1. Alina Beygelzimer, Sham Kakade, and John Langford. "Cover trees for nearest neighbor." Proceedings of the 23rd international conference on Machine learning. ACM, 2006.
2. Mike Izbicki and Christian Shelton. "Faster cover trees." Proceedings of the 32nd International Conference on Machine Learning (ICML-15). 2015.

## SG-Tree
SG-Tree is a new data structure for exact nearest neighbor search inspired from Cover Tree and its improvement, which has been used in the [TerraPattern](http://www.terrapattern.com/) project. At a high level, SG-Tree tries to create a hierarchical tree where each node performs a "coarse" clustering. The centers of these "clusters" become the children and subsequent insertions are recursively performed on these children. When performing the NN query, we prune out solutions based on a subset of the dimensions that are being queried. This is particularly useful when trying to find the nearest neighbor in highly clustered subset of the data, e.g. when the data comes from a recursive mixture of Gaussians or more generally time marginalized coalscent process . The effect of these two optimizations is that our data structure is extremely simple, highly parallelizable and is comparable in performance to existing NN implementations on many data-sets. 
 
Under active development

### New: Moving to Python3
### New: Python wrappers added
Just use `python setup.py install` and then in python you can `import nntree`. The python API details are provided in `API.pdf`.
 If you do not have root priveledges, install with `python setup.py install --user` and make sure to have the folder in path. 
## Organisation
1. All codes are under `src` within respective folder
2. Dependencies are provided under `lib` folder
3. For running cover tree an example script is provided under `scripts`
4. `data` is a placeholder folder where to put the data
5. `build` and `dist` folder will be created to hold the executables


## Requirements
1. gcc >= 5.0 or Intel&reg; C++ Compiler 2017 for using C++14 features

## How to use
We will show how to run our Cover Tree on a single machine using synthetic dataset

1. First of all compile by hitting make

   ```bash
     make
   ```

2. Generate synthetic dataset

   ```bash
     python data/generateData.py
   ```


3. Run Cover Tree

   ```bash
      dist/cover_tree data/train_100d_1000k_1000.dat data/test_100d_1000k_10.dat
   ```

The make file has some useful features:

- if you have Intel&reg; C++ Compiler, then you can instead

   ```bash
     make intel
   ```

- or if you want to use Intel&reg; C++ Compiler's cross-file optimization (ipo), then hit
   
   ```bash
     make inteltogether
   ```

- Yet an other alternative is to use the LLVM/CLang compiler (minimal required version is 3.4, for c++14 support)

   ```bash
     make llvm
   ```

For this to work under linux,
you would probably have to install at least these packages
(in version 3.4 or later):
clang libc++-dev

- Also you can selectively compile individual modules by specifying

   ```bash
     make <module-name>
   ```

- or clean individually by

   ```bash
     make clean-<module-name>
   ```

## Performance
Based on our evaluation the implementation is easily scalable and efficient. For example on Amazon EC2 c4.8xlarge, we could insert more than 1 million vectors of 1000 dimensions in Euclidean space with L2 norm under 250 seconds. During query time we can process > 300 queries per second per core.

## Troubleshooting
If the build fails and throws error like "instruction not found", then most probably the system does not support AVX2 instruction sets. To solve this issue, in `setup.py` and `src/cover_tree/makefile` please change `march=core-avx2`to `march=corei7`.

