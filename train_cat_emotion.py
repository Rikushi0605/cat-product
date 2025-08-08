import tensorflow as tf

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam

datagen = ImageDataGenerator(preprocessing_function=tf.keras.applications.mobilenet_v2.preprocess_input, validation_split=0.2, horizontal_flip=True, zoom_range=0.2)

train_gen = datagen.flow_from_directory('dataset/', target_size=(224, 224), batch_size=32, class_mode='categorical',subset='training')
val_gen = datagen.flow_from_directory('dataset/', target_size=(224, 224), batch_size=32, class_mode='categorical',subset='validation')

base = MobileNetV2(include_top=False, weights='imagenet', input_shape=(224, 224, 3))
x = GlobalAveragePooling2D()(base.output)
x = Dropout(0.3)(x)
output = Dense(train_gen.num_classes, activation='softmax')(x)
model = Model(inputs=base.input, outputs=output)

model.compile(optimizer=Adam(1e-4), loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(train_gen, validation_data=val_gen, epochs=10)

model.save("cat_emotion_model.h5")
