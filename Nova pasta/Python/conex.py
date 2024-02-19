import socket
import sys
server_port = 2000
buffer = 1024
def connecting():

    value =input("Press the ip address to start the communication\n")
    confirmation = input(f"The destination is{value}. Is that correct?\n0-No,1-Yes")
    confirmation = (False if int(confirmation)==0 else True)
    if confirmation is False:
        print("Exiting..")
        sys.exit()
    return start_connection(value)    

   

def checking_ip_address(ip_address):

    if len(ip_address)==9 and ip_address is not None:
        return True
    print("Ending the program.. check if the ip adress is corrected")
    sys.exit()

def start_connection(ip_address):
    print(" Trying to connect o the server")
    checking_ip_address(ip_address)
    tcp_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        destiny=(ip_address,server_port)
        tcp_connection.connect(destiny)
    except ConnectionError as error:
        print("Connection refused. Try again!\n"
              f"Type of erro:{type(error)}")

    return tcp_connection


def close_conenection(tcp_connection):
    print("ending the tcp connection...")
    tcp_connection.close()

def conversation(tcp_connection):
    print("Stating the chat!\nObs: To exite the conversation press:exit")

    while true:
        message = input("You:" )
        if message != '':
            tcp_connection.send(bytes(message,"utf8"))
            if message=='exit':
                break
        recv_message=tcp_connection.recv(buffer).decode("ascii")

        if recv_message != '':
            print(f"Server message:{recv_message}")
            if recv_message=='exit':
                print("The server side just end the connection. Inform exit to end "
                      "the connection")
    print("Exitting..")
    close_conenection(tcp_connection)
    

    return True

if __name__=='__main__':
    print("Welcome to the chat whit socket communication\n")
    connection = connecting()
    conversation(connection)
    try:
        connection.close()
    except ConnectionError as err:
        print("Then TCP Connection is end")
