from pytube import YouTube

youtube = YouTube(input("Informe o link do video:"))
diretorio = input("Informe o diretorio:  ")
 
print(f"Titulo: {youtube.title}.")
print(f"Duração: {youtube.length} segundos.")

diret= youtube.streams.get_highest_resolution() 
print("Baixando!")
diret.download(diretorio)
print("Download completo")
