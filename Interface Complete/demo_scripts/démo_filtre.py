from PIL import Image
before_image=Image.open("./test3.png")
after_image = before_image.convert("L");;
after_image.save("./after.png")




