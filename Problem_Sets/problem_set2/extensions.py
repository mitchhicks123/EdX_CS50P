#main function
def main():
  #ask user for input, strip whitespace & put into lower
  fileName = input("File name: ").lower().strip()

  #use else if clause to check file extension
  if fileName.endswith(".gif"):
    print("image/gif")

  elif fileName.endswith(".jpg") or fileName.endswith(".jpeg"):
    print("image/jpeg")

  elif fileName.endswith(".png"):
    print("image/png")

  elif fileName.endswith(".pdf"):
    print("application/pdf")

  elif fileName.endswith(".txt"):
    print("text/plain")

  elif fileName.endswith(".zip"):
    print("application/zip")

  else:
    print("application/octet-stream")

#call main function
main()