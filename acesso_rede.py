import os as sis
import ctypes
from dotenv import load_dotenv
import consts


load_dotenv()


line_cmd = sis.getenv("LINE")
middle = sis.getenv("MID")
final = sis.getenv("FINAL")
password = sis.getenv("PASSWORD")


# função recupera informações sobre o usuario windows. O indice determina qual info retornar.
def get_info_user(index: int):
    GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
    NameDisplay = index

    size = ctypes.pointer(ctypes.c_ulong(0))
    GetUserNameEx(NameDisplay, None, size)

    nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
    GetUserNameEx(NameDisplay, nameBuffer, size)
    # ref: https://stackoverflow.com/questions/21766954/how-to-get-windows-users-full-name-in-python

    return nameBuffer.value


def return_user(email: str):
    return email.split("@")[0]


def check_usuario(email: str):
    try:
        user = return_user(email)
        check = consts.axor_to_mdl[user]
    except KeyError:
        check = user
    return check


def list_net_user(email: str):
    try:
        user = return_user(email)
        check = consts.axor_to_mdl[user]
    except KeyError:
        check = user
    return consts.user_list[check]


# função gera script customizado para usuário
def create_cmd_line(email: str, letter: str, network: str):
    user = check_usuario(email)

    if user == "lmosa":
        return f"{line_cmd} {letter} {middle}{network}"
    # checagem de usuarios
    return f"{line_cmd} {letter} {middle}{network} {password} {final}{user}"


def execute_arquivo_batch(path):
    # https://stackoverflow.com/questions/5469301/run-a-bat-file-using-python-code
    sis.system(path)

    return print("Executado com sucesso!!")


def create_file(email: str, nome_arquivo: str):
    try:
        list_user = list_net_user(email)

        # utilizar map para escrever linhas de cmd no arquivo
        arquivo = open(nome_arquivo, "w+")
        for line in list_user:
            arquivo.writelines(create_cmd_line(email, line["lct"], line["drt"]) + "\n")
    except FileNotFoundError:
        # utilizar map para escrever linhas de cmd no arquivo fw.writelines(line + '\n' for line in line_list)
        arquivo = open(nome_arquivo, "w+")
        for line in list_user:
            arquivo.writelines(create_cmd_line(email, line["lct"], line["drt"]) + "\n")
    arquivo.close()

    return execute_arquivo_batch(nome_arquivo)


def exit_from_all(arquivo_del):
    e = "X:"
    cmd_delete = "net use {0} /delete /yes".format(e)

    arquivo = open(arquivo_del, "w+")
    arquivo.writelines(
        'Set WshNetwork = Wscript.CreateObject("Wscript.Network")' + "\n"
    )
    arquivo.writelines("on error resume next" + "\n")
    for i in consts.direc:
        e = i
        cmd_delete = 'WSHNetwork.RemoveNetworkDrive "{0}", True, True'.format(e)
        arquivo.writelines(cmd_delete + "\n")

    return print("Pronto para Excluir rede")


# função principal
def main():
    email = get_info_user(8)
    user = get_info_user(3)
    prefix = f"C:\\Users\\{''.join(user.split(' '))}\\Desktop\\AcessoRede\\"
    nome_arquivo = f"{prefix}acesso.bat"
    arquivo_del = f"{prefix}del.vbs"

    exit_from_all(arquivo_del)
    execute_arquivo_batch(arquivo_del)

    create_file(email, nome_arquivo)

    sis.remove(nome_arquivo)
    return sis.remove(arquivo_del)


if __name__ == "__main__":
    main()
