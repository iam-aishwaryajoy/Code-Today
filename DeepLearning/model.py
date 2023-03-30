from import_lib import *
from tuner import *

class FashionMnist:
    def __init__(self):
        self.train_images = 0
        self.train_labels = 0
        self.test_images = 0
        self.test_labels = 0
        self.tuner = 0

    def preprocessing(self):
        self.train_images = self.train_images.reshape((self.train_images.shape[0], 28, 28, 1))
        self.test_images = self.test_images.reshape((self.test_images.shape[0], 28, 28, 1))
        self.train_labels = to_categorical(self.train_labels)
        self.test_labels = to_categorical(self.test_labels)

        self.train_images = self.train_images.astype('float32')
        self.test_images = self.test_images.astype('float32')
        self.train_images = self.train_images / 255.0
        self.test_images = self.test_images / 255.0


    def define_model(self, hp):
        num_hidden_layers = 1  
        num_units_conv = 8
        num_units_dense = 8

        c_kernel = 1
        m_kernel = 1

        dropout_rate = 0.1
        learning_rate = 0.01
        momentum = 0.9
        activation = 'relu'

        if hp:
            num_hidden_layers = hp.Choice('num_hidden_layers', values=[1,2,3,5])
            num_units_conv = hp.Choice('num_units_conv', values=[8, 16, 32, 64,128])
            num_units_dense = hp.Choice('num_units_dense', values=[8, 16, 32, 64,128])
            dropout_rate = hp.Float('droput_rate', min_value=0.1, max_value=0.5)
            learning_rate = hp.Float('learning_rate', min_value=0.0001 , max_value=0.01)
            momentum = hp.Float('momentum', min_value=0.9, max_value=0.99)
            c_kernel = hp.Choice('c_kernel', values=[1, 3, 5,7])
            m_kernel = hp.Choice('m_kernel', values=[1, 2, 3])
            act_conv = hp.Choice('act_conv', values=['relu','sigmoid','tanh'])
            act_dense= hp.Choice('act_dense', values=['relu','sigmoid','tanh'])

        inputs = Input(shape=(28,28,1))
        x = Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform')(inputs)

        for _ in range(1, num_hidden_layers):
            x = Conv2D(num_units_conv, (c_kernel,c_kernel), padding='same', activation=act_conv)(x)       
            x = Dense(num_units_dense, activation=act_dense)(x)
            x = Dropout(dropout_rate)(x)
            x = BatchNormalization()(x)

        x = Flatten()(x)    
        x = Dense(100, activation='relu', kernel_initializer='he_uniform')(x)
        outputs = Dense(10, activation='softmax')(x)
        model = keras.Model(inputs=inputs, outputs=outputs, name="HyperModel")
        model.compile(optimizer=SGD(lr=learning_rate, momentum=momentum), loss='categorical_crossentropy', metrics=['accuracy'])

        return model

    def load_data(self):
        fashion_mnist = tf.keras.datasets.fashion_mnist
        (self.train_images, self.train_labels), (self.test_images, self.test_labels) = fashion_mnist.load_data()

    def train_data(self, tuner):
        self.tuner = tuner
        self.tuner.search(self.train_images, self.train_labels, validation_data=(self.test_images, self.test_labels), epochs=10, verbose=True)
        self.tuner.results_summary(1)

    def build_model_and_retrain(self):
        hypermodel = self.tuner.get_best_models(num_models=1)[0]
        callbck = [tf.keras.callbacks.EarlyStopping(monitor='val_accuracy', patience=3)]
        hypermodel.fit(self.train_images, self.train_labels, epochs=20, batch_size=64, validation_data=(self.test_images, self.test_labels), callbacks=callbck)
        _, acc = hypermodel.evaluate(self.test_images, self.test_labels, verbose=1)
        eval_result = acc

        return hypermodel, eval_result
        
        
if __name__ == '__main__':

    fashion_model = FashionMnist()
    model = fashion_model.define_model
    tuner = CustomTuner(model,
            objective='val_accuracy',
            max_trials=50,
            directory='logs',
            project_name='fashion_mnist',
            overwrite=True)
    fashion_model.load_data()
    fashion_model.preprocessing()

    best_hyperparameter = fashion_model.train_data(tuner)

    hypermodel, eval_result = fashion_model.build_model_and_retrain()
    print("Final model:")
    hypermodel.summary()

    hypermodel.save("hypermodel.h5")

    print("[test loss, test accuracy]:", eval_result*100)
