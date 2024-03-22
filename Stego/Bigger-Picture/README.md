# Bigger Picture
## Author : kn1gh7

### Description :
The answer to one of the biggest mysteries known is in this image file, however I am unable to open it :(

Can you help me?

Don't get disappointed if the answer doesn't amuse you, always see the bigger picture!


### Files :
- [chall.svg](chall.svg)

### Solution :
Upon doing exiftool on the .svg file it shows ```File format error```. So we try checking the file signature using [hexed.it](https://hexed.it/).
[](original_hex.png)
On changing the magic bytes for png image
[](changed1.png)
we get the image
[](chall.png)
The name of the chall (even the image) suggests that this isn't the whole picture. We notice that the size of the image is 450 X 180 . So we change the height to 450.
[](changed2.png)
This gives the Bigger Picture with the flag
[](size_matters.png)
TechnexCTF{y3s_1t_d03s}