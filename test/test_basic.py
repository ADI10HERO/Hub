import pytest
import hub
import numpy as np

def test_init():
    print('- Initialize array')
    shape = (10,10,10,10)
    x = hub.array(shape, name="test/example:1", dtype='uint8')
    shape = np.array(shape)
    assert np.all(np.array(x.shape) == shape)
    print('passed')

def test_simple_upload_download():
    print('- Simple Chunk Upload and Download')
    x = hub.array((10,10,10,10), name="test/example:1", dtype='uint8')
    x[0] = np.ones((1,10,10,10), dtype='uint8')
    assert x[0].mean() == 1
    print('passed')

def test_multiple_upload_download():
    print('- Multiple Chunk Upload and Download')
    x = hub.array((10,10,10,10), name="test/example:1", dtype='uint8')
    x[0:3] = np.ones((3,10,10,10), dtype='uint8')
    assert x[0:3].mean() == 1
    print('passed')

def test_cross_chunk_upload_download():
    print('- Cross Chunk Upload and Download')
    x = hub.array((100,100,100), name="test/example:2", dtype='uint8')
    x[2:5, 0:10, 0:10] = np.ones((3,10,10), dtype='uint8')
    assert x[2:5, 0:10, 0:10].mean() == 1
    assert x[2:5, 10:, 10:].mean() == 0
    print('passed')

def test_broadcasting():
    print('- Broadcasting')
    x = hub.array((100,100,100), name="test/example:3", dtype='uint8')
    x[0,0,0] = 11
    assert x[0,0,0] == 11 
    x[0] = 10
    assert x[0].mean() == 10
    x[1] = np.ones((100,100), dtype='uint8')
    assert x[1].mean() == 1
    x[3,90,:] = np.ones((1,1,100), dtype='uint8')
    assert x[3, 90].mean() == 1
    print('passed')   

# Add Shape Check
# Add Type Check

if __name__ == "__main__":
    print('Running Basic Tests')
    test_init()
    test_simple_upload_download()
    test_multiple_upload_download()
    test_cross_chunk_upload_download()
    test_broadcasting()