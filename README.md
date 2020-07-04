# asymetric-encryption-and-decryption
  Asymmetric cryptography, also known as public-key cryptography, is a process that uses a pair of related keys -- one public key and one private key -- to encrypt and decrypt a message and protect it from unauthorized access or use. A public key is a cryptographic key that can be used by any person to encrypt a message so that it can only be deciphered by the intended recipient with their private key. A private key -- also known as a secret key -- is shared only with key's initiator.
  
# How asymmetric cryptography works
Asymmetric encryption uses a mathematically related pair of keys for encryption and decryption: a public key and a private key. If the public key is used for encryption, then the related private key is used for decryption; if the private key is used for encryption, then the related public key is used for decryption.

The two participants in the asymmetric encryption workflow are the sender and the receiver; each has its own pair of public and private keys. First, the sender obtains the receiver's public key. Next, the plaintext -- or ordinary, readable text -- is encrypted by the sender using the receiver's public key; this creates ciphertext. The ciphertext is then sent to the receiver, who decrypts the ciphertext with their private key and returns it to legible plaintext.

# Sending encrypted text over email
  We used yagmail module of python to send email.
# Process
1)sender uses his email, password to send a message to reciever. <br />
2)He enters public key. <br />
ex: 189 <br />
3)This public key itself is converted to a private and unknown key by appending some random number using randint(). <br />
ex: 189657391749 <br />
4)Now the encrypted message email is sent to the reciever and the decrypting key is with the sender only. <br />
5)when the sender gives the private key to reciever, he can enter the encrypted text and privte key to decrypt the message.
