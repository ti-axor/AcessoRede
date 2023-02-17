import os as sis
import ctypes
from dotenv import load_dotenv
import consts


def get_info_user(index: int):
    GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
    NameDisplay = index

    size = ctypes.pointer(ctypes.c_ulong(0))
    GetUserNameEx(NameDisplay, None, size)

    nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
    GetUserNameEx(NameDisplay, nameBuffer, size)
    # ref: https://stackoverflow.com/questions/21766954/how-to-get-windows-users-full-name-in-python

    return nameBuffer.value


# verificar se existe arquivo run
# se existe sobre-escreve direção do arquivo run e somar ao nome do arquivo batch e da direção do python.exe
# se não existe escreve direção do arquivo run e somar ao nome do arquivo batch e da direção do python.exe
def create_run_file(user):
    try:
        name = "".join(user.split(" "))
        dir_py = f"C:\\Users\\{name}\\AppData\\Local\\Microsoft\\WindowsApps"
        dir_access = f"C:\\Users\\{name}\\Desktop\\AcessoRede"
        script_run = '@echo off\n"{0}\python.exe" "{1}\acesso_rede.py"\nexit\n'.format(
            dir_py, dir_access
        )
        file = f"C:\\Users\\{name}\\Desktop\\AcessoRede\\run.bat"
        print(script_run, file)
        arquivo = open(file, "w+")
        arquivo.writelines(script_run)
    except FileNotFoundError:
        arquivo = open(file, "w+")
        arquivo.writelines(script_run)
        print(script_run, file)


# chama função create_run_file
# verifica se existe arquivo vbs
# se existe, sobre-escreve direção do arquivo run.bat
# se não existe, cria arquivo vbs com direção de arquivo run.bat
def create_vbs_file(user):
    try:
        name = "".join(user.split(" "))
        dir_file_run = f"C:\\Users\{name}\\Desktop\\AcessoRede\\run.bat"
        script_vbs = 'Set WshShell = CreateObject("WScript.Shell")\n\ncmds=WshShell.RUN("{0}", 0, True)\n\n\nSet WshShell = Nothing\n'.format(
            dir_file_run
        )
        file = f"C:\\Users\{name}\\Desktop\\AcessoRede\\run_bg.vbs"
        if not sis.path.isfile(dir_file_run):
            raise Exception("FileNotFountError")
        arquivo = open(file, "w+")
        arquivo.writelines(script_vbs)
    except Exception as e:
        print(e.args)
        create_run_file(user)
        arquivo = open(file, "w+")
        arquivo.writelines(script_vbs)


# função principal
def main():
    user = get_info_user(3)

    create_vbs_file(user)


if __name__ == "__main__":
    main()
