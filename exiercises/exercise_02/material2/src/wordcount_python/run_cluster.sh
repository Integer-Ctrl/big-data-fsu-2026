#!/bin/bash
hdfs dfs -rm -r result_dir
time hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -combiner reducer.py -input test_dir -output result_dir
