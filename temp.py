import tensorflow as tf
from numpy.random.mtrand import shuffle

#define filename queue
filename_queue = tf.train.string_input_producer(['/Users/terrycho/training_datav2/queue_test_data/b1.csv'
                                                 ,'/Users/terrycho/training_datav2/queue_test_data/c2.csv']
                                                ,shuffle=False,name='filename_queue')

# define reader
reader = tf.TextLineReader()
key,value = reader.read(filename_queue)

#define decoder
record_defaults = [id, num, year, rtype , rtime = tf.decode_csv(
    value, record_defaults=record_defaults,field_delim=',')

with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    for i in range(100):
        print(sess.run([id, num, year, rtype , rtime]))

    coord.request_stop()
    coord.join(threads)


