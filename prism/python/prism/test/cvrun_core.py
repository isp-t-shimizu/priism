import time
import cPickle

import prism

# load pickled objects 
with open('griddedvis.pickle', 'rb') as f:
    griddedvis = cPickle.load(f)

with open('uvgridconfig.pickle', 'rb') as f:
    uvgridconfig = cPickle.load(f)

start_time = time.time()

# instantiate
worker = prism.SparseModelingImager(solver_name='sparseimaging')

# set necessary data to worker
worker.griddedvis = griddedvis
worker.uvgridconfig = uvgridconfig

# mfista
L1_list = [1e0, 1e2, 1e4, 1e6, 1e7, 1e8]
Ltsv_list = [1e0, 1e2, 1e4, 1e6, 1e8, 1e10]

# set num_fold to 0 to disable CV
num_fold=10
worker.cvforgridvis(L1_list, Ltsv_list, num_fold=num_fold,
                    imageprefix='hd142527_core', imagepolicy='full',
                    summarize=True, figfile='cvresult_core.png',
                    datafile='cvresult_core.dat', maxiter=1000)

end_time = time.time()
print '{0}: elapsed {1} sec'.format('cvrun_core.py', end_time-start_time)