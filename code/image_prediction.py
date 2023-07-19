import sys
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def process_file(image_path, target_size=(256, 256)):
    try:
        # Cargar el modelo
        with open('resnet-50-MRI.json', 'r') as json_file:
            json_savedModel = json_file.read()
            model = tf.keras.models.model_from_json(json_savedModel)
            model.load_weights('weights.hdf5')
            model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=["accuracy"])

        # Cargar la imagen y prepararla para la predicción
        img = load_img(image_path, target_size=target_size)
        img_array = img_to_array(img)
        img_array = img_array / 255.0  # Normalizar los valores de píxeles entre 0 y 1

        # Realizar la predicción para la imagen de prueba
        test_image = np.expand_dims(img_array, axis=0)  # Agregar dimensión de lote
        test_predict = model.predict(test_image)

        # Obtener la clase predicha a partir del modelo
        predict = [str(np.argmax(i)) for i in test_predict]
        predict = np.asarray(predict)
        print(predict)

        return img_array, predict

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error al procesar el archivo: {str(e)}")

if __name__ == "__main__":
    # Obtener la ruta del archivo como argumento de línea de comandos
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        process_file(image_path)
    else:
        print("Por favor, especifique la ruta del archivo como argumento.")



'''
Para usar el archivo python y comprbar que funciona debes escribir en el terminal:
python image_prediction (url de imagen)
'''
