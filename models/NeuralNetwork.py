import tensorflow as tf
import DataPrepare as dp
import numpy as np
import os


def random_init(x,num_feature_1st,num_feature_2nd):
    W1 =  tf.Variable(tf.random_normal([num_feature_1st,num_feature_2nd],mean=0.0,stddev=0.01))
    bias1 = tf.Variable(tf.random_normal([num_feature_2nd],mean=0.0,stddev=0.01))
    W2 = tf.Variable(tf.random_normal([num_feature_2nd,1],mean=0.0,stddev=0.01))
    bias2 = tf.Variable(tf.random_normal([1],mean=0.0,stddev=0.01))

    return [W1,bias1,W2,bias2]




def softsign(z):
    """The softsign function, applied elementwise."""
    return z / (1. + np.abs(z))




def multilayer_perceptron(x,num_feature_1st,num_feature_2nd):
    params = random_init(x,num_feature_1st,num_feature_2nd)
    layer_1 = tf.add(tf.matmul(x,params[0]),params[1])
    layer_1 = softsign(layer_1)
    #layer_1 = tf.nn.relu(layer_1)
    layer_2 = tf.add(tf.matmul(layer_1,params[2]),params[3])
    #output = tf.nn.softmax(layer_2)
    output = tf.nn.sigmoid(layer_2)

    return output





def next_batch(num, dataX,dataY):
    idx = np.arange(0,len(dataX))
    np.random.shuffle(idx)
    idx = idx[0:num]
    dataX_shuffle = [dataX[i] for i in idx]
    dataY_shuffle = [dataY[i] for i in idx]
    dataX_shuffle = np.asarray(dataX_shuffle)
    dataY_shuffle = np.asarray(dataY_shuffle)
    return dataX_shuffle, dataY_shuffle




if __name__ == "__main__":
    #sess = tf.InteractiveSession()

    learning_rate = 0.001
    training_epochs = 15
    batch_size = 100
    display_step = 1
    num_feature_1st = 6
    num_feature_2nd = 500


    x = tf.placeholder(tf.float32, [None, 6])
    y = tf.placeholder(tf.float32)


    data = dp.dataPrepareForLogistic(dp.datas, dp.path)
    trainX = data[0]
    testX = data[1]   # a matrix
    trainY = data[2] # a vector with binary number
    testY = data[3]
    params = random_init(x,num_feature_1st,num_feature_2nd)



    # construct model
    pred = multilayer_perceptron(x, num_feature_1st, num_feature_2nd)
    cost = -tf.reduce_sum(y * tf.log(pred))
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    # construct logging
    with tf.name_scope("loss"):
        loss = -tf.reduce_sum(y*tf.log(pred))
    loss_summary = tf.summary.scalar("loss", loss)


    # initializing
    init = tf.global_variables_initializer()

    # saving model
    model_saver = tf.train.Saver()
    with tf.Session() as sess:
        sess.run(init)

        # logging
        train_writer = tf.summary.FileWriter("/Users/Lai/Dropbox/PersonalProject/MachineLearningForSports/models/curve",sess.graph)

        # train
        summary_loss = None
        for epoch in range(training_epochs):
            avg_cost = 0
            total_batch = int(len(trainX[:,0])/batch_size)
            for i in range(total_batch):
                batch_x, batch_y = next_batch(batch_size,trainX,trainY)
                _, c = sess.run([optimizer,cost],feed_dict = {x:batch_x,y:batch_y})
                summary_loss = sess.run(loss_summary, feed_dict={x:batch_x,y:batch_y})
                train_writer.add_summary(summary_loss, i)

                avg_cost += c/total_batch

            if epoch % display_step ==0:
                print("Epoch: ", "%04d" % (epoch+1), " cost = ", "{:.9f}".format(avg_cost))

        print("Optimization Finished!")
        #train_writer.add_summary(summary_loss, training_epochs)

        # check the test error
        predicted_values = np.sum([np.random.binomial(1, p=pred.eval(feed_dict={x: testX})) for i in range(1)], axis=0)
        correct_prediction = [(predicted_values[i] == testY[i]) for i in range(len(predicted_values))]
        print(sum(correct_prediction)/len(predicted_values))

        #save the mdoel
        save_path = model_saver.save(sess, "/Users/Lai/Dropbox/PersonalProject/MachineLearningForSports/models/neural_model.ckpt")





















