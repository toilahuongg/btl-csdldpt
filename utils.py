import numpy
def hog_to_str(hog_features):
  return ','.join(str(f) for f in hog_features)

def str_to_hog(hog_features_str):
  return numpy.array([float(x) for x in hog_features_str.split(',')])