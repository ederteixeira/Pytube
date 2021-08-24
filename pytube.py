from pytube import YouTube

yt = YouTube(input("Informe o link do video:"))
diretorio = input("Informe o diretorio:  ")
 
print(f"Titulo: {yt.title}.")
print(f"Duração: {yt.length} seconds.")

diret= yt.streams.get_highest_resolution() 
print("Baixando!")
diret.download(diretorio)
print("Download completo")