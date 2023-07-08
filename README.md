"# Data":

Leer y explorar datos:

df = pd.read_csv('./data_mask.csv')
df.info()
df.head(50)
df['mask'].value_counts()
df.duplicated().value_counts()

En este bloque, se carga un archivo CSV llamado data_mask.csv en un DataFrame utilizando la función read_csv() de la biblioteca Pandas. Luego, se imprimen información general sobre el DataFrame con info(), se muestran las primeras 50 filas con head(50), se cuentan los valores únicos en la columna "mask" con value_counts(), y se cuentan los valores duplicados en el DataFrame con duplicated().value_counts().

Visualizar conteo de valores en la columna "mask":

fig = go.Figure(data=go.Bar(x=counts.index, y=counts.values))
fig.update_layout(
    title='Conteo de valores en la columna "mask"',
    xaxis=dict(title='Valores'),
    yaxis=dict(title='Conteo'),
    hovermode='x'
)
fig.show()

En este bloque, se muestra la visualización de una imagen cargada desde un archivo utilizando la biblioteca matplotlib. Se lee la imagen en la variable imagen utilizando plt.imread(), se muestra la imagen con plt.imshow(), se desactivan los ejes con plt.axis('off') y se muestra la imagen en el notebook con plt.show().

Visualizar imágenes MRI y máscaras:

mri_images = ['TCGA_CS_5395_19981004/TCGA_CS_5395_19981004_1.tif']
masks = ['TCGA_CS_5395_19981004/TCGA_CS_5395_19981004_1_mask.tif']
mri_image = mri_images[0]
mask = masks[0]
mri = Image.open(mri_image)
mask = Image.open(mask)
mri_array = np.array(mri)
mask_array = np.array(mask)
plt.figure()
plt.imshow(mri_array, cmap='gray')
plt.title('MRI Image')
plt.axis('off')
plt.show()
plt.figure()
plt.imshow(mask_array, cmap='gray')
plt.title('Mask')
plt.axis('off')
plt.show()

En este bloque, se muestra la visualización de una imagen MRI y su máscara correspondiente. Se definen las rutas de las imágenes MRI y máscaras en las listas mri_images y masks, respectivamente. Luego, se carga la primera imagen y su máscara utilizando Image.open() de la biblioteca PIL. Las imágenes se convierten a arrays numpy utilizando np.array(). Finalmente, se muestra la imagen MRI y la máscara utilizando plt.imshow(), con títulos y ejes desactivados.

Visualizar muestras aleatorias:

muestras_aleatorias = df.sample(n=12)
fig, axs = plt.subplots(4, 3, figsize=(10, 12))
for i, ax in enumerate(axs.flat):
    muestra = muestras_aleatorias.iloc[i]
    imagen = plt.imread(muestra['image_path'])
    mascara = plt.imread(muestra['mask_path'])
    ax.imshow(imagen, cmap='gray')
    ax.imshow(mascara, cmap='Reds', alpha=0.5)
    ax.axis('off')
plt.tight_layout()
plt.show()

En este bloque, se seleccionan aleatoriamente 12 muestras del DataFrame utilizando sample(). Luego, se crea una figura con subplots de 4 filas y 3 columnas utilizando plt.subplots(). Se itera sobre los subplots y se muestra la imagen MRI y su máscara correspondiente utilizando plt.imshow(). Las máscaras se superponen en rojo utilizando alpha=0.5 para la transparencia. Se desactivan los ejes y se ajusta el espaciado entre los subplots con tight_layout(). Finalmente, se muestra la figura con plt.show().
