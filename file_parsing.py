import os

# рабочая директория
cwd = os.getcwd()
# папка с фотографиями, подверженными анализу(загружаемые пользователем)
photos_folder = cwd + '/temp/'
if not os.path.isdir(photos_folder):
    os.mkdir(photos_folder)


def files_parse():
    all_files = os.listdir(photos_folder)
    filename_coordinates = []

    for filename in all_files:
        # деление имени файла на составляющие
        temp = filename.split('_')

        # ширина
        latitude = temp[2].replace('lt', '')
        # долгота
        longitude = temp[3].replace('ln', '')

        # создание ноды в формате [название_файла, [ширина, долгота]]
        node = []
        node.append(filename)
        node.append([float(latitude), float(longitude)])

        # добавление фала в обший список файлов
        filename_coordinates.append(node)

    # возвращает [название_файла, [ширина, долгота]] для всех файлов из папки
    return filename_coordinates


def func(file_name):
    # принимает на вход имя фотографии
    path_to_photo = photos_folder + file_name
    # функция, работающая с моделью
    # возвращает True, если есть повреждения
    pass


def computerVision():
    # фотографии лэп с повреждёнными инсуляторами
    results = []

    # все файлы директории в формате [название_файла, [ширина, долгота]]
    files = files_parse()

    for file in files:
        # функция получает название файла
        # в случае дефекта добавляет файл в список повреждённых
        # if (func(file[0])):

        results.append(file)

    return results