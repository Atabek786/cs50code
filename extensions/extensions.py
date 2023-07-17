prompt = input("File name: ")
prompt = prompt.strip().lower()

if prompt.endswith(".gif"):
    print("image/gif")
elif prompt.endswith(".jpg") or prompt.endswith(".jpeg"):
    print("image/jpeg")
elif prompt.endswith(".png"):
    print("image/png")
elif prompt.endswith(".pdf"):
    print("application/pdf")
elif prompt.endswith(".txt"):
    print("text/plain")
elif prompt.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")